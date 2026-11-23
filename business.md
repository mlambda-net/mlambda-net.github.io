---
layout: page
eyebrow: For business
title: Software your company can rely on
subtitle: Applications that work together out of the box, and systems designed and built for your business — every one written in mathematics and proved before it reaches you.
description: MLambda for business — CRM, ERP, a service desk, integrations, marketing and logistics apps, and custom systems designed from a description of your business, all proved before release.
permalink: /business/
wide: true
---

{%- assign products = site.products | where_exp: "p", "p.tagline" | sort: "order" -%}

<section class="section" style="margin-top:1rem">
  <ul class="ideas">
    <li><span class="ideas__n">Proved</span><h3>Correct before release</h3><p>Every rule is logic, every test is derived from the model, and every change clears 0 warnings, security A and reliability A.</p></li>
    <li><span class="ideas__n">Together</span><h3>Apps that talk by events</h3><p>No app calls another: Make hears their events and runs the flows that join them, so a won deal becomes a customer in the ERP on its own.</p></li>
    <li><span class="ideas__n">Yours</span><h3>One deployment per client</h3><p>Your own kernel, your own data, your own sign-in, deployed and watched as microservices.</p></li>
  </ul>
</section>

<section class="section">
  <div class="section__head"><div><span class="eyebrow">Applications</span><h2>Run the business</h2></div></div>
  <ul class="grid-cards">
  {%- for product in products %}{% if product.category == "app" %}{% include product-card.html product=product %}{% endif %}{% endfor %}
  </ul>
</section>

<section class="section">
  <div class="section__head"><div><span class="eyebrow">Services</span><h2>What every app stands on</h2></div></div>
  <ul class="grid-cards">
  {%- for product in products %}{% if product.category == "service" %}{% include product-card.html product=product %}{% endif %}{% endfor %}
  </ul>
</section>

<section class="section">
  <div class="section__head"><div><span class="eyebrow">Built for you</span><h2>Your system, from a description</h2></div>
  <a class="btn btn--ghost" href="{{ '/products/turing.html' | relative_url }}">Turing →</a></div>
  <ol class="steps">
    <li><strong>Describe</strong><span>A paragraph about your business: what it sells, who works in it, what goes wrong.</span></li>
    <li><strong>Architect</strong><span>Turing discovers the contexts, epics and stories, and the architectural canon (TOGAF, SEI, DDD) judges each one with you.</span></li>
    <li><strong>Design</strong><span>A clickable prototype of every screen, and the domain model, services and data behind it.</span></li>
    <li><strong>Build and prove</strong><span>Written in Aleph and Hilbert, tested from the model, every screen proved against its prototype.</span></li>
    <li><strong>Run it</strong><span>Deployed for you, watched by Helios, integrated with the apps you already have.</span></li>
  </ol>
</section>

<section class="section cta">
  <h2>See it on your own business</h2>
  <p>Tell us what your company does; we will show you the architecture, the screens and the apps that fit.</p>
  <div class="hero__actions">
    <a class="btn btn--primary" href="mailto:{{ site.data.company.email }}?subject=MLambda%20for%20my%20business">Ask for a demonstration</a>
    <a class="btn" href="https://store.mlambda.net/">The MLambda Store</a>
  </div>
</section>
