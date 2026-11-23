---
layout: home
title: MLambda
description: MLambda builds sophisticated software end to end with neuro-symbolic AI — written in Aleph and Hilbert, mathematical languages, and proved by mathematics before it ships.
---

<section class="hero hero--split">
  <div>
    <span class="eyebrow">Neuro-symbolic software engineering</span>
    <h1>Software built end to end by AI, and proved by mathematics.</h1>
    <p class="hero__lede">Language models propose; logic and mathematics decide. MLambda writes software in
    <strong>Aleph</strong> and <strong>Hilbert</strong>, mathematical languages that AI handles well and a machine can
    check, and proves every rule, test and screen before it ships. The power of mathematical abstraction, used to
    build software that is sophisticated and still correct.</p>
    <div class="hero__actions">
      <a class="btn btn--primary" href="{{ '/business/' | relative_url }}">For business</a>
      <a class="btn" href="{{ '/developers/' | relative_url }}">For developers</a>
      <a class="btn btn--ghost" href="{{ '/research/' | relative_url }}">Research →</a>
    </div>
  </div>
  {% include carousel.html slides=site.data.showcase title="MLambda products" class="carousel--hero" %}
</section>

<section class="section">
  <ul class="doors">
    <li><a class="door" href="{{ '/business/' | relative_url }}">
      <span class="door__kicker">For business</span>
      <h3>Applications that work together, and systems built for you</h3>
      <p>CRM, ERP, a service desk, integrations, marketing and logistics, each proved before release; or your own
      system, designed from a description of your business.</p>
      <span class="door__go">The apps and how we build →</span>
    </a></li>
    <li><a class="door" href="{{ '/developers/' | relative_url }}">
      <span class="door__kicker">For developers</span>
      <h3>A mathematical stack, from the compiler up</h3>
      <p>Aleph and its native compiler, Hilbert and Shin for mathematics and logic, a tensor engine on the GPU, actors,
      a database, agents and the tools that prove every change.</p>
      <span class="door__go">The languages and the platform →</span>
    </a></li>
    <li><a class="door" href="{{ '/research/' | relative_url }}">
      <span class="door__kicker">Research</span>
      <h3>Why neural needs symbolic</h3>
      <p>Models are fluent and unreliable; mathematics is reliable and slow to write. Put together, each covers what
      the other lacks. The thesis, the method and the essays.</p>
      <span class="door__go">The ideas behind it →</span>
    </a></li>
  </ul>
</section>

<section class="section">
  <span class="eyebrow">The approach</span>
  <h2>Three ideas, one system</h2>
  <ul class="ideas">
    <li>
      <span class="ideas__n">01</span>
      <h3>Neuro-symbolic</h3>
      <p>Neural models read, perceive and draft. Symbolic logic, rules in <a href="{{ '/products/shin.html' | relative_url }}">Shin</a>,
      decides what is allowed, what follows and what is missing. An agent can be fluent without being reckless.</p>
    </li>
    <li>
      <span class="ideas__n">02</span>
      <h3>A mathematical language</h3>
      <p>AI is good at mathematics. So the code is written in <a href="{{ '/products/aleph.html' | relative_url }}">Aleph</a>,
      pure and strongly typed, and every formula in <a href="{{ '/products/hilbert.html' | relative_url }}">Hilbert</a>:
      abstractions a model can produce and a compiler can check.</p>
    </li>
    <li>
      <span class="ideas__n">03</span>
      <h3>Mathematical verification</h3>
      <p>Tests are derived from the model, not guessed. Every change passes 0 warnings, security A, reliability A and
      coverage of at least 95 %, and every screen is proved against its prototype.</p>
    </li>
  </ul>
</section>

<section class="section">
  <span class="eyebrow">End to end</span>
  <h2>From a description to a running system</h2>
  <ol class="steps">
    <li><strong>Describe</strong><span>A paragraph about the business. <a href="{{ '/products/turing.html' | relative_url }}">Turing</a> discovers its contexts, epics, features and stories.</span></li>
    <li><strong>Architect</strong><span>The architectural canon (TOGAF, SEI, DDD) judges every item; accepted items become services, a domain model, data and screens.</span></li>
    <li><strong>Write the mathematics</strong><span>The system is written in Aleph, Hilbert and Shin; <a href="{{ '/products/max.html' | relative_url }}">Max</a> agents and <a href="{{ '/products/neuron.html' | relative_url }}">Neuron</a> do the neural work.</span></li>
    <li><strong>Prove</strong><span>Tsadi derives the tests, Ayin judges the code, Litush polishes it, Playground proves each screen side by side.</span></li>
    <li><strong>Ship and watch</strong><span>Katharsis releases it, Arkhos deploys it as microservices, Helios watches every request. <a href="{{ '/products/quality.html' | relative_url }}">How →</a></span></li>
  </ol>
</section>

<section class="section">
  <ul class="proof">
    <li><span class="proof__num">~70</span><span class="proof__label">repositories in one family, all our own</span></li>
    <li><span class="proof__num">9</span><span class="proof__label">targets the Aleph compiler emits</span></li>
    <li><span class="proof__num">0 · A · A</span><span class="proof__label">warnings, security, reliability, on every change</span></li>
    <li><span class="proof__num">95 %</span><span class="proof__label">coverage of the derived tests, at least</span></li>
  </ul>
</section>

<section class="section">
  <div class="section__head">
    <div>
      <span class="eyebrow">Products</span>
      <h2>For the business</h2>
    </div>
    <a class="btn btn--ghost" href="{{ '/business/' | relative_url }}">All the apps →</a>
  </div>
  {%- assign picks = "crm,muse,make,erp" | split: "," %}
  <ul class="grid-cards">
  {%- for slug in picks %}{% assign rp = "_products/" | append: slug | append: ".md" %}{% assign product = site.products | where: "relative_path", rp | first %}{% if product %}{% include product-card.html product=product %}{% endif %}{% endfor %}
  </ul>
</section>

<section class="section">
  <div class="section__head">
    <div>
      <span class="eyebrow">Platform</span>
      <h2>For developers</h2>
    </div>
    <a class="btn btn--ghost" href="{{ '/developers/' | relative_url }}">The whole platform →</a>
  </div>
  {%- assign picks = "aleph,hilbert,tensor,max" | split: "," %}
  <ul class="grid-cards">
  {%- for slug in picks %}{% assign rp = "_products/" | append: slug | append: ".md" %}{% assign product = site.products | where: "relative_path", rp | first %}{% if product %}{% include product-card.html product=product %}{% endif %}{% endfor %}
  </ul>
</section>

<section class="section cta">
  <h2>See it build a system</h2>
  <p>Describe a business in a paragraph and watch Turing turn it into an architecture, a model and its screens.</p>
  <div class="hero__actions">
    <a class="btn btn--primary" href="mailto:{{ site.data.company.email }}?subject=MLambda%20demonstration">Ask for a demonstration</a>
    <a class="btn" href="{{ '/about/' | relative_url }}">The company</a>
  </div>
</section>
