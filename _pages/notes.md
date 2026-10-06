---
layout: default
permalink: /notes/
title: notes
description: State of the Art reports
nav: true
nav_order: 5
---

<!-- Edit the links in _data/notes.yml - this page only renders them. -->

<div class="post">

  <div class="header-bar">
    <h1>{{ page.title }}</h1>
    <h2>{{ page.description }}</h2>
  </div>

{% for group in site.data.notes.groups %}

{% if group.title %}

## {{ group.title }}

{% endif %}

{% if group.description %}{{ group.description }}{% endif %}

<div class="notes-grid">
  {% for link in group.links %}
    {% assign external = false %}
    {% if link.url contains '://' %}{% assign external = true %}{% endif %}
    <a
      class="notes-card"
      href="{% if external %}{{ link.url }}{% else %}{{ link.url | relative_url }}{% endif %}"
      {% if external %}target="_blank" rel="noopener noreferrer"{% endif %}
    >
      <span class="notes-name">{{ link.name }}</span>
      {% if link.description %}<span class="notes-desc">{{ link.description }}</span>{% endif %}
      {% if external or link.tag %}
        <span class="notes-foot">
          {% if external %}<span class="notes-host">{{ link.url | remove_first: 'https://' | remove_first: 'http://' | split: '/' | first | remove_first: 'www.' }}</span>{% else %}<span class="notes-host"></span>{% endif %}
          {% if link.tag %}<span class="notes-tag">{{ link.tag }}</span>{% endif %}
        </span>
      {% endif %}
    </a>
  {% endfor %}
</div>

{% endfor %}

</div>

<style>
  /* the grid needs breathing room under the header-bar rule */
  .notes-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.25rem;
    margin: 2.5rem 0;
  }

  .notes-card {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    height: 100%;
    padding: 1.1rem 1.2rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 12px;
    background-color: var(--global-card-bg-color);
    color: var(--global-text-color);
    text-decoration: none;
    transition:
      transform 0.2s ease,
      border-color 0.2s ease,
      box-shadow 0.2s ease;
  }

  .notes-card:hover,
  .notes-card:focus-visible {
    transform: translateY(-3px);
    border-color: var(--global-theme-color);
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
    text-decoration: none;
    color: var(--global-text-color);
  }

  .notes-card:focus-visible {
    outline: 2px solid var(--global-theme-color);
    outline-offset: 2px;
  }

  .notes-name {
    font-weight: 600;
    line-height: 1.3;
    color: var(--global-theme-color);
  }

  .notes-desc {
    font-size: 0.9rem;
    line-height: 1.45;
    color: var(--global-text-color);
  }

  /* pins the footer to the bottom so cards in a row line up */
  .notes-foot {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.5rem;
    margin-top: auto;
    padding-top: 0.5rem;
    font-size: 0.75rem;
    color: var(--global-text-color-light);
  }

  .notes-host {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .notes-tag {
    flex: 0 0 auto;
    padding: 0.1rem 0.5rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 999px;
    text-transform: lowercase;
  }

  @media (prefers-reduced-motion: reduce) {
    .notes-card {
      transition: none;
    }

    .notes-card:hover,
    .notes-card:focus-visible {
      transform: none;
    }
  }
</style>
