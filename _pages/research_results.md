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


  <h4 class="year">Geometric Deep Learning</h4>
  {% bibliography -f papers -q @*[category=GDL]* %}


</div>
