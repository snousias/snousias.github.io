---
layout: page
permalink: /repositories/
title: repositories
description: Github profile and repositories
nav: true
nav_order: 4
---

{% if site.data.repositories.github_users %}

## GitHub users

<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for user in site.data.repositories.github_users %}
    {% include repository/repo_user.liquid username=user %}
  {% endfor %}
</div>

---

{% if site.repo_trophies.enabled %}
{% for user in site.data.repositories.github_users %}
{% if site.data.repositories.github_users.size > 1 %}

  <h4>{{ user }}</h4>
  {% endif %}
  <div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% include repository/repo_trophies.liquid username=user %}
  </div>

---

{% endfor %}
{% endif %}
{% endif %}

{% if site.data.repositories.github_repos %}



<div class="repositories-grid">
  {% for repo in site.data.repositories.github_repos %}
    <div class="repository-item">
      {% include repository/repo.liquid repository=repo %}
    </div>
  {% endfor %}
</div>

<style>
.repositories-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.repository-item {
  background: var(--global-card-bg-color, #fff);
  border: 1px solid var(--global-divider-color, #e0e0e0);
  border-radius: 12px;
  padding: 1rem;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.repository-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
  border-color: var(--global-theme-color, #007bff);
}

.repository-item .repo {
  padding: 0;
  margin: 0;
}

.repository-item .repo img {
  border-radius: 8px;
  transition: transform 0.3s ease;
}

.repository-item:hover .repo img {
  transform: scale(1.02);
}

@media (max-width: 768px) {
  .repositories-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .repository-item {
    padding: 0.75rem;
  }
}
</style>
{% endif %}
