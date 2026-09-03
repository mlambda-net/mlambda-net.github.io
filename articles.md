---
layout: page
eyebrow: Articles
title: Writing from MLambda
subtitle: On verification before construction, neuro-symbolic AI, actors, and languages in which the common corruptions cannot be written.
description: Articles from MLambda on neuro-symbolic AI, Turing, actor-native data, and the Aleph language.
permalink: /articles/
wide: true
---

{% assign posts = site.pages | where_exp: "p", "p.url contains '/articles/' and p.url != '/articles/'" | sort: "path" | reverse %}
<ul class="grid-cards">
{% for a in posts %}
  <li>
    <a class="card" href="{{ a.url | relative_url }}">
      {% if a.image %}<div class="card__art"><img src="{{ a.image | relative_url }}" alt="" width="1200" height="627" loading="lazy" style="display:block;border-radius:4px"></div>{% endif %}
      <span class="card__meta">{{ a.eyebrow }}</span>
      <h3 class="card__title">{{ a.title }}</h3>
      <p class="card__tagline">{{ a.subtitle }}</p>
    </a>
  </li>
{% endfor %}
</ul>
