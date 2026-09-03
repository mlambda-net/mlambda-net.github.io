---
layout: page
title: Work with MLambda
subtitle: Four ways to engage, starting with seeing it run. Terms are agreed per engagement.
description: A Turing demonstration, consulting, commercial licence and support, and early access to the MLambda stack.
permalink: /services/
wide: true
---

<ul class="services">
{% for e in site.data.services.engagements %}
  <li class="service{% if e.primary %} service--primary{% endif %}" id="{{ e.id }}">
    <h2 class="service__name">{{ e.name }}</h2>
    <p>{{ e.summary }}</p>
    <ul>{% for i in e.includes %}<li>{{ i }}</li>{% endfor %}</ul>
    <p class="muted">{{ e.start }}</p>
    <p><a class="btn{% if e.primary %} btn--primary{% endif %}" href="mailto:{{ site.data.company.email }}?subject={{ e.name | uri_escape }}">{{ site.data.company.email }}</a></p>
  </li>
{% endfor %}
</ul>
