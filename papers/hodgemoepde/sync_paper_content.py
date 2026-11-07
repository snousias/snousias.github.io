"""Typeset the manuscript's text as HTML without paraphrasing or copy editing."""
from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image
import re
import subprocess
import hashlib
import json

ROOT = Path(__file__).resolve().parent
SOURCE = Path(r'C:/Users/int/Dropbox/Workspace/01_3DMLCV_part_B/hodgeformer/experiments/regression_pdes_tetrahedral/paper/hodge_moe_pde_v8_NEURIPS_cleanup')
PAPER = 'static/papers/Hodge_Routed_MoE_PDE.pdf'
page = BeautifulSoup((ROOT / 'index.html').read_text(encoding='utf-8'), 'html.parser')
source_hashes = {}

def read(name):
    p = SOURCE / name
    raw = p.read_bytes()
    source_hashes[name] = hashlib.sha256(raw).hexdigest()
    return raw.decode('utf-8')

def uncomment(text):
    return re.sub(r'(?<!\\)%[^\n]*', '', text)

def argument(text, start):
    assert text[start] == '{'
    depth = 1
    i = start + 1
    while depth:
        if text[i] == '{' and text[i-1] != '\\': depth += 1
        if text[i] == '}' and text[i-1] != '\\': depth -= 1
        i += 1
    return text[start+1:i-1], i

arxiv = read('arxiv.tex')
macros = '\n'.join(line for line in arxiv.splitlines() if line.startswith('\\newcommand'))
bibliography = read('arxiv.bbl')
bibitems = list(re.finditer(r'\\bibitem\[.*?\]\{([^}]+)\}', bibliography))
citation_numbers = {m[1]: n+1 for n, m in enumerate(bibitems)}
warnings = []

def pandoc(tex):
    result = subprocess.run(['pandoc', '--from=latex', '--to=html5', '--mathjax', '--wrap=none', '--shift-heading-level-by=1'], input=macros+'\n'+tex, text=True, capture_output=True, encoding='utf-8', check=True)
    if result.stderr.strip(): warnings.append(result.stderr.strip())
    soup = BeautifulSoup(result.stdout, 'html.parser')
    for citation in soup.select('.citation'):
        keys = citation['data-cites'].split()
        citation.clear()
        for n, key in enumerate(keys):
            if n: citation.append(', ')
            link = soup.new_tag('a', href=PAPER)
            link.string = '['+str(citation_numbers[key])+']'
            citation.append(link)
    return str(soup)

figures = {}
figure_captions = {}

def figure(block):
    label = re.search(r'\\label\{([^}]+)\}', block)[1]
    filename = re.search(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', block)[1]
    caption_start = block.index('\\caption{') + len('\\caption')
    caption_tex, _ = argument(block, caption_start)
    caption_html = pandoc(caption_tex)
    caption_soup = BeautifulSoup(caption_html, 'html.parser')
    if caption_soup.p:
        caption_soup.p.unwrap()
    name = Path(filename).name
    image_name = 'overview_landscape.png' if name == 'overview_landscape.pdf' else name
    image_path = ROOT/'assets/images'/image_name
    width, height = Image.open(image_path).size
    href = 'static/papers/overview_landscape.pdf' if name == 'overview_landscape.pdf' else 'assets/images/'+image_name
    fig = BeautifulSoup('<figure class="paper-figure"><a target="_blank" rel="noopener noreferrer"><img decoding="async" loading="lazy"/></a><figcaption></figcaption></figure>', 'html.parser')
    fig.figure['id'] = label
    fig.a['href'] = href
    fig.a['aria-label'] = 'Open figure at full resolution'
    fig.img.attrs.update(src='assets/images/'+image_name, width=str(width), height=str(height), alt=caption_soup.get_text(' ',strip=True))
    if name == 'overview_landscape.pdf':
        del fig.img['loading']
        fig.img['fetchpriority'] = 'high'
    fig.figcaption.append(caption_soup)
    if name == 'compare_models.png':
        # These labels and mean errors are typeset beneath the panels in the source.
        labels = [('CFD reference', '---'), (r'\mathrm{rel}\text{-}L_2(p)=0.026', r'\mathrm{rel}\text{-}L_2(\nut)=0.063'), (r'\mathrm{rel}\text{-}L_2(p)=0.030', r'\mathrm{rel}\text{-}L_2(\nut)=0.116'), (r'\mathrm{rel}\text{-}L_2(p)=0.066', r'\mathrm{rel}\text{-}L_2(\nut)=0.144'), (r'\mathrm{rel}\text{-}L_2(p)=0.085', r'\mathrm{rel}\text{-}L_2(\nut)=0.155')]
        row = fig.new_tag('div', attrs={'class': 'model-labels'})
        for i, pair in enumerate(labels):
            col = fig.new_tag('span')
            col.append(BeautifulSoup(pandoc(pair[0]+'\n\n'+pair[1] if i == 0 else '$'+pair[0]+'$\n\n$'+pair[1]+'$'), 'html.parser'))
            row.append(col)
        fig.a.insert_after(row)
    figures[label] = fig.figure
    figure_captions[label] = caption_tex
    return str(fig)

placeholder_blocks = {}

def prepare(tex):
    tex = uncomment(tex)
    # Overview is already displayed above the abstract; suppress its conditional include.
    tex = re.sub(r'\\ifdefined\\overviewafterabstract\\else\s*\\input\{sections/overview\}\s*\\fi', '', tex)
    tex = re.sub(r'\\ifdefined\\arxivqualinresults\\else\s*\\input\{sections/S07_qualitative_vertex_only\}\s*\\fi', '', tex)
    def replace_figure(m):
        key = 'PAPERFIGUREBLOCK' + str(len(placeholder_blocks))
        placeholder_blocks[key] = figure(m[0])
        return '\n\n'+key+'\n\n'
    tex = re.sub(r'\\begin\{figure\}(?:\[[^\]]*\])?[\s\S]*?\\end\{figure\}', replace_figure, tex)
    tex = tex.replace(r'\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}lrccccccc@{}}', r'\begin{tabular}{lrccccccc}').replace(r'\end{tabular*}', r'\end{tabular}')
    return tex

converted_sections = []
def add_section(name, tex=None):
    original = read('sections/'+name) if tex is None else tex
    html = pandoc(prepare(original))
    for key, block in placeholder_blocks.items():
        html = html.replace('<p>'+key+'</p>', block)
    converted_sections.append((name, original, html))
    return html

abstract = read('sections/00_abstract.tex').replace(r'\begin{abstract}', r'\section{Abstract}\label{abstract}').replace(r'\end{abstract}', '')
overview_source = read('sections/overview.tex')
caption, _ = argument(overview_source, overview_source.index('\\caption{')+len('\\caption'))
overview = figure(r'\begin{figure}\includegraphics{figures/overview_landscape.pdf}\caption{'+caption+r'}\label{fig:arch}\end{figure}')

contents = [add_section('00_abstract.tex', abstract)]
for name in ['04_experiments.tex', 'qualitative_case.tex']:
    contents.append(add_section(name))

# Retain the existing publication header, resource links, overview, and footer.
main = page.main
main.clear()
teaser = BeautifulSoup('<section class="hero teaser"><div class="container is-max-desktop"><div class="hero-body"></div></div></section>', 'html.parser')
teaser.select_one('.hero-body').append(BeautifulSoup(overview, 'html.parser'))
main.append(teaser)
for (name, original, html) in converted_sections:
    section = page.new_tag('section', attrs={'class': 'section', 'data-source': 'sections/'+name})
    container = page.new_tag('div', attrs={'class': 'container is-max-desktop content paper-text'})
    container.append(BeautifulSoup(html, 'html.parser'))
    section.append(container)
    main.append(section)

# Resolve TeX cross-references as web links; reference labels are presentation only.
targets = {t['id']: t for t in page.select('[id]')}
equation_labels = {label for math in page.select('.math.display') for label in re.findall(r'\\label\{([^}]+)\}', math.get_text())}
source_titles = {}
for path in (SOURCE/'sections').glob('*.tex'):
    text = uncomment(path.read_text(encoding='utf-8'))
    for match in re.finditer(r'\\(?:sub)*section\*?\{([^}]+)\}\s*\\label\{([^}]+)\}', text):
        source_titles[match[2]] = match[1]

for anchor in page.select('a[data-reference]'):
    key = anchor['data-reference']
    if key in targets or key in equation_labels:
        target = targets.get(key)
        if target and target.name in ['h2','h3','h4']:
            anchor.string = target.get_text(' ',strip=True)
        elif key.startswith('tab:'):
            anchor.string = 'Table '+str(list(t['id'] for t in page.select('[id^="tab:"]')).index(key)+1)
        elif key.startswith('fig:'):
            anchor.string = 'Figure '+str(list(t['id'] for t in page.select('figure[id]')).index(key)+1)
        else:
            anchor.string = 'Equation'
    else:
        anchor['href'] = PAPER
        anchor.string = source_titles.get(key, 'Supplementary material')

for heading in main.select('h2'):
    heading['class'] = ['title', 'is-5', 'has-text-centered']
for heading in main.select('h3'):
    heading['class'] = ['title', 'is-6', 'section-heading']
for table in main.select('table'):
    wrapper = page.new_tag('div', attrs={'class': 'table-scroll', 'role': 'region', 'aria-label': 'Paper results table', 'tabindex': '0'})
    table.wrap(wrapper)
    for row in table.select('tbody tr'):
        if 'Hodge-routed MoE' in row.get_text(): row['class'] = ['ours']
for math in main.select('.math.display'):
    # Pandoc retains the equation environment inside display delimiters.
    # Transfer its labels to HTML anchors and retain the equation body verbatim.
    value = math.get_text()
    labels = re.findall(r'\\label\{([^}]+)\}', value)
    value = re.sub(r'\\label\{[^}]+\}', '', value)
    value = value.replace(r'\begin{equation}', '').replace(r'\end{equation}', '')
    math.string = value
    wrapper = page.new_tag('div', attrs={'class': 'equation'})
    math.wrap(wrapper)
    for label in labels:
        anchor = page.new_tag('span', id=label)
        wrapper.insert_before(anchor)

# Pandoc expands manuscript math macros. Define the same macros as a fallback.
config = page.find('script', src=None)
config.string = r'''
window.MathJax = {
  tex: {
    inlineMath: [['\\(', '\\)']], displayMath: [['\\[', '\\]']],
    macros: {ux: 'u_x', uy: 'u_y', nut: '\\nu_t', CL: 'C_L', rhoL: '\\rho_L', gate: 'g', simplex: '\\Delta^{K}', relL: '\\text{rel-}L_2'}
  },
  options: {skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']}
};
'''

def normalize(text):
    return ' '.join(text.split())

def prose_only(fragment):
    soup = BeautifulSoup(str(fragment), 'html.parser')
    for node in soup.select('.math, .citation, a[data-reference]'):
        node.decompose()
    return normalize(soup.get_text(' ', strip=True))

def math_only(fragment):
    soup = BeautifulSoup(str(fragment), 'html.parser')
    values = []
    for node in soup.select('.math'):
        value = re.sub(r'\\label\{[^}]+\}', '', node.get_text())
        value = value.replace(r'\begin{equation}', '').replace(r'\end{equation}', '')
        values.append(normalize(value))
    return values

for name, original, html in converted_sections:
    actual = page.select_one('[data-source="sections/'+name+'"]')
    assert prose_only(html) == prose_only(actual), 'Prose changed: '+name
    assert math_only(html) == math_only(actual), 'Mathematics changed: '+name

(ROOT/'index.html').write_text(str(page).rstrip()+'\n',encoding='utf-8')
(ROOT/'paper-content-provenance.json').write_text(json.dumps({'source_directory':str(SOURCE),'conversion':'Pandoc LaTeX to HTML; no paraphrasing or copy editing','source_sha256':source_hashes},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'source_sections': len(converted_sections), 'figures': len(page.select('figure')), 'tables': len(page.select('table')), 'references': len(bibitems), 'prose_and_equation_preservation':'PASS', 'pandoc_warnings': warnings},ensure_ascii=True))
