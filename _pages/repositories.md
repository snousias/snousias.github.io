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
/* Enhanced Repositories Grid Styling */
.repositories-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
  margin: 3rem 0;
  padding: 0 1rem;
}

/* Repository Item Cards */
.repository-item {
  background: var(--global-card-bg-color, #fff);
  border: 2px solid transparent;
  border-radius: 16px;
  padding: 1.5rem;
  position: relative;
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  box-shadow: 
    0 4px 20px rgba(0, 0, 0, 0.08),
    0 2px 8px rgba(0, 0, 0, 0.06);
}

/* Gradient Border Effect */
.repository-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, 
    var(--global-theme-color, #007bff) 0%, 
    rgba(var(--global-theme-color-rgb, 0, 123, 255), 0.7) 50%, 
    var(--global-theme-color, #007bff) 100%);
  border-radius: 16px;
  padding: 2px;
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask-composite: exclude;
  opacity: 0;
  transition: opacity 0.4s ease;
}

/* Hover Effects */
.repository-item:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 
    0 20px 40px rgba(0, 0, 0, 0.15),
    0 8px 16px rgba(0, 0, 0, 0.1),
    0 0 0 1px rgba(var(--global-theme-color-rgb, 0, 123, 255), 0.1);
  border-color: rgba(var(--global-theme-color-rgb, 0, 123, 255), 0.3);
}

.repository-item:hover::before {
  opacity: 1;
}

/* Repository Content Styling */
.repository-item .repo {
  padding: 0;
  margin: 0;
  position: relative;
  z-index: 2;
}

.repository-item .repo a {
  display: block;
  text-decoration: none;
  color: inherit;
}

.repository-item .repo img {
  border-radius: 12px;
  transition: all 0.4s ease;
  width: 100%;
  height: auto;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

.repository-item:hover .repo img {
  transform: scale(1.03);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
}

/* Loading Animation */
.repository-item .repo img {
  animation: fadeInUp 0.6s ease-out forwards;
  opacity: 0;
  transform: translateY(20px);
}

@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Staggered Animation Delay */
.repository-item:nth-child(1) .repo img { animation-delay: 0.1s; }
.repository-item:nth-child(2) .repo img { animation-delay: 0.2s; }
.repository-item:nth-child(3) .repo img { animation-delay: 0.3s; }
.repository-item:nth-child(4) .repo img { animation-delay: 0.4s; }
.repository-item:nth-child(5) .repo img { animation-delay: 0.5s; }
.repository-item:nth-child(6) .repo img { animation-delay: 0.6s; }

/* Glow Effect on Hover */
.repository-item:hover {
  box-shadow: 
    0 20px 40px rgba(var(--global-theme-color-rgb, 0, 123, 255), 0.15),
    0 8px 16px rgba(0, 0, 0, 0.1),
    0 0 20px rgba(var(--global-theme-color-rgb, 0, 123, 255), 0.2);
}

/* Dark Mode Adjustments */
@media (prefers-color-scheme: dark) {
  .repository-item {
    background: var(--global-card-bg-color, #1a1a1a);
    box-shadow: 
      0 4px 20px rgba(255, 255, 255, 0.05),
      0 2px 8px rgba(255, 255, 255, 0.03);
  }
  
  .repository-item:hover {
    box-shadow: 
      0 20px 40px rgba(var(--global-theme-color-rgb, 0, 123, 255), 0.2),
      0 8px 16px rgba(255, 255, 255, 0.1),
      0 0 20px rgba(var(--global-theme-color-rgb, 0, 123, 255), 0.3);
  }
}

/* Responsive Design */
@media (max-width: 1200px) {
  .repositories-grid {
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
  }
}

@media (max-width: 768px) {
  .repositories-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
    margin: 2rem 0;
    padding: 0 0.5rem;
  }
  
  .repository-item {
    padding: 1.25rem;
  }
  
  .repository-item:hover {
    transform: translateY(-4px) scale(1.01);
  }
}

@media (max-width: 480px) {
  .repositories-grid {
    gap: 1rem;
  }
  
  .repository-item {
    padding: 1rem;
    border-radius: 12px;
  }
}

/* Accessibility Improvements */
.repository-item:focus-within {
  outline: 2px solid var(--global-theme-color, #007bff);
  outline-offset: 2px;
}

/* Reduced Motion Support */
@media (prefers-reduced-motion: reduce) {
  .repository-item,
  .repository-item .repo img,
  .repository-item::before {
    transition: none;
    animation: none;
  }
  
  .repository-item:hover {
    transform: none;
  }
}
</style>
{% endif %}
