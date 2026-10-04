---
layout: page
permalink: /star/
title: STAR
description: State of the Art reports
nav_order: 7
---

<!-- Edit the links in _data/star.yml - this page only renders them. -->

{% for group in site.data.star.groups %}

{% if group.title %}

## {{ group.title }}

{% endif %}

{% if group.description %}{{ group.description }}{% endif %}

<div class="star-grid">
  {% for link in group.links %}
    {% assign external = false %}
    {% if link.url contains '://' %}{% assign external = true %}{% endif %}
    <a
      class="star-card"
      href="{% if external %}{{ link.url }}{% else %}{{ link.url | relative_url }}{% endif %}"
      {% if external %}target="_blank" rel="noopener noreferrer"{% endif %}
    >
      <span class="star-name">{{ link.name }}</span>
      {% if link.description %}<span class="star-desc">{{ link.description }}</span>{% endif %}
      {% if external or link.tag %}
        <span class="star-foot">
          {% if external %}<span class="star-host">{{ link.url | remove_first: 'https://' | remove_first: 'http://' | split: '/' | first | remove_first: 'www.' }}</span>{% else %}<span class="star-host"></span>{% endif %}
          {% if link.tag %}<span class="star-tag">{{ link.tag }}</span>{% endif %}
        </span>
      {% endif %}
    </a>
  {% endfor %}
</div>

{% endfor %}

<style>
  .star-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.25rem;
    margin: 1.5rem 0 2.5rem;
  }

  .star-card {
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

  .star-card:hover,
  .star-card:focus-visible {
    transform: translateY(-3px);
    border-color: var(--global-theme-color);
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
    text-decoration: none;
    color: var(--global-text-color);
  }

  .star-card:focus-visible {
    outline: 2px solid var(--global-theme-color);
    outline-offset: 2px;
  }

  .star-name {
    font-weight: 600;
    line-height: 1.3;
    color: var(--global-theme-color);
  }

  .star-desc {
    font-size: 0.9rem;
    line-height: 1.45;
    color: var(--global-text-color);
  }

  /* pins the footer to the bottom so cards in a row line up */
  .star-foot {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.5rem;
    margin-top: auto;
    padding-top: 0.5rem;
    font-size: 0.75rem;
    color: var(--global-text-color-light);
  }

  .star-host {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .star-tag {
    flex: 0 0 auto;
    padding: 0.1rem 0.5rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 999px;
    text-transform: lowercase;
  }

  @media (prefers-reduced-motion: reduce) {
    .star-card {
      transition: none;
    }

    .star-card:hover,
    .star-card:focus-visible {
      transform: none;
    }
  }
</style>
