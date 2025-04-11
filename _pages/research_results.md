---
layout: page
permalink: /results/
title: research results
description: Selected publications presented in chronological order.
years: [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2016]
nav: true
nav_order: 1
toc:
  sidebar: left
---

<!-- _pages/research_results.md -->

### table of contents
- [3D Machine learning and Computer Vision](/results/#GDL)
- [AI & Machine Learning in the Built Environment](/results/#AIBE)
- [Doctoral Dissertation](/results/#PHD)
- [Computational Modelling and Simulation in Biomedical Engineering](/results/#BME)
- [Machine Learning for Healthcare and Medicine](/results/#MLHM)
- [Model Compression and Acceleration in DNNs](/results/#MCA)
- [Sparse Modelling for Data Imputation](/results/#MCDI)

<div class="publications">

  <h4 class="year" id="GDL" style="padding-top:2em">3D Machine learning  
  and Computer Vision</h4>

  {% bibliography -f papers -q @*[category_1=GDL || category_2=GDL]* %}


  <h4 class="year" id="AIBE" style="padding-top:2em">AI & Machine Learning in the Built Environment</h4>

  {% bibliography -f papers -q @*[category_1=AIBE || category_2=AIBE]* %}

  <h4 class="year" id="PHD" style="padding-top:2em">Doctoral dissertation</h4>

  <p>Research in:</p>
  <ul>
    <li><strong>Computational Modelling and Simulation in Biomedical Engineering</strong></li>
    <li><strong>AI and Machine Learning in Healthcare and Medicine</strong></li>
  </ul>

  {% bibliography -f papers -q @*[category_1=PHD || category_2=PHD]* %}

  <h4 class="year" id="BME" style="padding-top:2em">Computational Modelling and Simulation in Biomedical Engineering</h4>

  {% bibliography -f papers -q @*[category_1=BME || category_2=BME]* %}

  <h4 class="year" id="MLHM" style="padding-top:2em">Machine Learning for Healthcare and Medicine</h4>

  {% bibliography -f papers -q @*[category_1=MLHM || category_2=MLHM  || category_3=MLHM]* %}


  <h4 class="year" id="MCA" style="padding-top:2em">Efficient AI, Model Compression and Acceleration in DNNs</h4>

  {% bibliography -f papers -q @*[category_1=MCA || category_2=MCA]* %}

  <h4 class="year" id="MCDI" style="padding-top:2em">Sparse Modelling for Data Imputation</h4>

  {% bibliography -f papers -q @*[category_1=MCDI || category_2=MCDI]* %}


</div>
