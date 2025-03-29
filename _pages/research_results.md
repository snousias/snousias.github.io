---
layout: page
permalink: /results/
title: research results
description: Selected publications presented in chronological order.
years: [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2016]
nav: true
nav_order: 1
---

<!-- _pages/research_results.md -->

### table of contents
- [Representation learning for 3D meshes](/results/#GDL)
- [AI & Machine Learning in the Built Environment](/results/#AIBE)
- [Computational Modelling and Simulation in Biomedical Engineering](/results/#BME)
- [Machine Learning for Healthcare and Medicine](/results/#MLHM)
- [Intelligent Cyber-Physical Systems and Efficient AI](/results/#CPS)

<div class="publications">

  <h4 class="year" id="GDL" style="padding-top:2em">3D Machine learning  
  and Computer Vision</h4>
  <h5 class="year">Representation learning for 3D meshes </h5>

  {% bibliography -f papers -q @*[category_1=GDL]* %}


  <h4 class="year" id="AIBE" style="padding-top:2em">AI & Machine Learning in the Built Environment</h4>

  {% bibliography -f papers -q @*[category_1=AIBE]* %}

  <h4 class="year" id="BME" style="padding-top:2em">Computational Modelling and Simulation in Biomedical Engineering</h4>

  {% bibliography -f papers -q @*[category_1=BME]* %}

  <h4 class="year" id="MLHM" style="padding-top:2em">Machine Learning for Healthcare and Medicine</h4>

  {% bibliography -f papers -q @*[category_1=MLHM]* %}

  <h4 class="year" id="CPS" style="padding-top:2em">Intelligent Cyber-Physical Systems and Efficient AI</h4>

  {% bibliography -f papers -q @*[category_1=CPS]* %}



</div>
