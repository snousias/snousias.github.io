---
layout: page
permalink: /results/
title: research results
description: Publications presented by categories in reversed chronological order.
years: [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2016]
categories: ["AIBE"]
nav: true
nav_order: 1
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

{%- for c in page.categories %}

  <h2 class="year">{{c}}</h2>
  {% bibliography -f papers -q @*[category={{c}}]* %}

{% endfor %}

</div>
