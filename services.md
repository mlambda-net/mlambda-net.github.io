---
layout: page
title: Work with MLambda
subtitle: Three ways to engage. Terms are agreed per engagement.
description: Consulting, commercial licence and support, and early access to the MLambda stack.
permalink: /services/
wide: true
---

<ul class="services">
{% for e in site.data.services.engagements %}
  <li class="service" id="{{ e.id }}">
    <h2 class="service__name">{{ e.name }}</h2>
    <p>{{ e.summary }}</p>
    <ul>{% for i in e.includes %}<li>{{ i }}</li>{% endfor %}</ul>
    <p class="muted">{{ e.start }}</p>
    <p><a class="btn" href="mailto:{{ site.data.company.email }}?subject={{ e.name | uri_escape }}">{{ site.data.company.email }}</a></p>
  </li>
{% endfor %}
</ul>
