---
layout: page
title: projects
permalink: /projects/
description:  Research projects in cyber-physical systems, energy efficiency, digital health, and cultural heritage preservation
nav: true
years: [2026,2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2016]
nav_order: 3
display_categories: [H2020 - Horizon Europe]
horizontal: false
toc:
  sidebar: left
---

> **Note:** The projects listed below represent my participation as a staff researcher.

<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

{% assign sorted_projects = site.projects | sort: "importance" %}

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>


<div class="publications">

  <h4 class="year" id="GDL" style="padding-top:2em">3D Machine learning  
  and Computer Vision</h4>

{% bibliography -f papers -q @*[category_1=GDL || category_2=GDL]* %}

  <h4 class="year" id="AIBE" style="padding-top:2em">AI & Machine Learning in the Built Environment</h4>

{% bibliography -f papers -q @*[category_1=AIBE || category_2=AIBE]* %}

  <h4 class="year" id="PHD" style="padding-top:2em">Doctoral dissertation</h4>

  <p><strong>PhD in Analysis, Modelling and Simulation for mHealth Applications</strong></p>
  <p><strong>Research topics:</strong></p>
  <ul>
    <li><strong>Computational Modelling and Simulation in Biomedical Engineering</strong></li>
    <li><strong>AI and Machine Learning in Healthcare and Medicine</strong></li>
  </ul>

{% bibliography -f papers -q @*[category_1=PHD || category_2=PHD]* %}

  <h4 class="year" id="BME" style="padding-top:2em">Computational Methods in Biomedical Engineering</h4>

{% bibliography -f papers -q @*[category_1=BME || category_2=BME]* %}

  <h4 class="year" id="MLHM" style="padding-top:2em">Machine Learning for Healthcare and Medicine</h4>

{% bibliography -f papers -q @*[category_1=MLHM || category_2=MLHM  || category_3=MLHM]* %}

  <h4 class="year" id="MCA" style="padding-top:2em">Efficient AI, Model Compression and Acceleration in DNNs</h4>

{% bibliography -f papers -q @*[category_1=MCA || category_2=MCA]* %}

  <h4 class="year" id="MCDI" style="padding-top:2em">Sparse Modelling for Data Imputation</h4>

{% bibliography -f papers -q @*[category_1=MCDI || category_2=MCDI]* %}

  <h4 class="year" id="Gamification" style="padding-top:2em">Application : Gamification</h4>

{% bibliography -f papers -q @*[category_1=Gamification || category_2=Gamification]* %}

</div>

