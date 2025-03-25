---
layout: page
permalink: /results/
title: Research results
description: Selected publications presented in chronological order.
years: [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2016]
nav: true
nav_order: 1
---

<!-- _pages/research_results.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">


  <h4 class="year">3D Machine learning</h4>
  <h5 class="year">Representation learning for 3D meshes </h5>

  {% bibliography -f papers -q @*[category_1=GDL]* %}


  <h4 class="year">Computational modelling for Biomedical Engineering</h4>

  {% bibliography -f papers -q @*[category_1=BME]* %}

</div>
