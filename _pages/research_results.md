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

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

  <h4 class="year" style="padding-top:2em">3D Machine learning  
  and Computer Vision</h4>
  <h5 class="year">Representation learning for 3D meshes </h5>

  {% bibliography -f papers -q @*[category_1=GDL]* %}


  <h4 class="year" style="padding-top:2em">AI & Machine Learning in the Built Environment</h4>

  {% bibliography -f papers -q @*[category_1=AIBE]* %}

  <h4 class="year" style="padding-top:2em">Computational modelling for Biomedical Engineering</h4>

  {% bibliography -f papers -q @*[category_1=BME]* %}

  <h4 class="year" style="padding-top:2em">Machine Learning for Healthcare and Medicine</h4>

  {% bibliography -f papers -q @*[category_1=MLHM]* %}

    <h4 class="year" style="padding-top:2em">Intelligent Cyber-Physical Systems and Efficient AI</h4>

  {% bibliography -f papers -q @*[category_1=CPS]* %}

      <h4 class="year" style="padding-top:2em">Heritage Science</h4>

  {% bibliography -f papers -q @*[category_1=HTG]* %}


</div>
