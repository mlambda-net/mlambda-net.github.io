---
layout: page
eyebrow: Research
title: Why neural needs symbolic
subtitle: Language models are fluent and unreliable; mathematics is reliable and slow to write. MLambda's research is about putting the two together so each covers what the other lacks.
description: MLambda's research — the neuro-symbolic thesis, the method of verification before construction, the essays, and the science workbench.
permalink: /research/
wide: true
---

<section class="section" style="margin-top:1rem">
  <ul class="ideas">
    <li><span class="ideas__n">The thesis</span><h3>Models propose, mathematics decides</h3><p>A model reads, perceives and drafts; a theory in Shin decides what is allowed and what follows. The answer comes with its reasons.</p></li>
    <li><span class="ideas__n">The method</span><h3>Verified before it is built</h3><p>A specification is a theorem and the implementation its proof: models checked, tests derived, every change judged. <a href="{{ '/method/' | relative_url }}">The method →</a></p></li>
    <li><span class="ideas__n">The evidence</span><h3>A whole stack built this way</h3><p>A compiler, a database, an operating system, agents and applications, each written in the languages it argues for.</p></li>
  </ul>
</section>

<section class="section">
  <div class="section__head"><div><span class="eyebrow">Essays</span><h2>Writing</h2></div>
  <a class="btn btn--ghost" href="{{ '/articles/' | relative_url }}">All essays →</a></div>
  {%- assign posts = site.pages | where_exp: "p", "p.url contains '/articles/' and p.url != '/articles/'" | sort: "path" | reverse %}
  <ul class="essays">
  {%- for a in posts limit: 6 %}
    <li><a href="{{ a.url | relative_url }}">
      <span class="essays__kicker">{{ a.eyebrow | remove: "Article · " }}</span>
      <span class="essays__title">{{ a.title }}</span>
      <span class="essays__line">{{ a.subtitle }}</span>
    </a></li>
  {%- endfor %}
  </ul>
</section>

<section class="section">
  <div class="section__head"><div><span class="eyebrow">In practice</span><h2>Where the ideas run</h2></div></div>
  {%- assign products = site.products | where_exp: "p", "p.tagline" | sort: "order" %}
  {%- assign picks = "turing,max,neuron,shin,tensor,science" | split: "," %}
  <ul class="grid-cards">
  {%- for slug in picks %}{% assign rp = "_products/" | append: slug | append: ".md" %}{% assign product = site.products | where: "relative_path", rp | first %}{% if product %}{% include product-card.html product=product %}{% endif %}{% endfor %}
  </ul>
</section>
