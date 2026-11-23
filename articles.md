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
<ul class="essays essays--all">
{%- for a in posts %}
  <li><a href="{{ a.url | relative_url }}">
    {%- if a.image %}<img class="essays__img" src="{{ a.image | relative_url }}" alt="" loading="lazy">{% endif %}
    <span class="essays__kicker">{{ a.eyebrow | remove: "Article · " }}</span>
    <span class="essays__title">{{ a.title }}</span>
    <span class="essays__line">{{ a.subtitle }}</span>
  </a></li>
{%- endfor %}
</ul>
