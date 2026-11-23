---
layout: page
eyebrow: For developers
title: A mathematical stack, from the compiler up
subtitle: Languages a model can write and a machine can check, a runtime made of actors, agents whose decisions are logic, and the tools that prove every change — all written here.
description: MLambda for developers — Aleph and its native compiler, Hilbert, Shin and Tensor for mathematics and logic, Samek, Aphrodite and Dream, actors, a database, Max and Neuron, and the quality tools.
permalink: /developers/
wide: true
---

{%- assign products = site.products | where_exp: "p", "p.tagline" | sort: "order" -%}

<section class="section" style="margin-top:1rem">
  <ul class="ideas">
    <li><span class="ideas__n">Why mathematics</span><h3>AI writes it, a compiler checks it</h3><p>Models are good at mathematics. A pure, typed language turns what they write into something a compiler can refuse, instead of something a reviewer has to trust.</p></li>
    <li><span class="ideas__n">Four languages</span><h3>Each kind of work its own</h3><p>General logic in Aleph, every rule and formula in Hilbert, every screen in Aphrodite, every test in Dream.</p></li>
    <li><span class="ideas__n">Native</span><h3>One binary, nine targets</h3><p>LLVM to x86-64, ARM64, RISC-V and WebAssembly; the GPU through each system's own driver.</p></li>
  </ul>
</section>

{%- assign groups = "language,intelligence,runtime,quality" | split: "," %}
{%- for g in groups %}
{%- assign c = site.data.categories | where: "id", g | first %}
<section class="section">
  <div class="section__head"><div><span class="eyebrow">{{ c.name }}</span><h2>{{ c.lede }}</h2></div></div>
  <ul class="grid-cards">
  {%- for product in products %}{% if product.category == g %}{% include product-card.html product=product %}{% endif %}{% endfor %}
  </ul>
</section>
{%- endfor %}

<section class="section cta">
  <h2>Start with Aleph</h2>
  <p>The language and its native compiler, for Windows and Linux: build, test and verify from your terminal.</p>
  <div class="hero__actions">
    <a class="btn btn--primary" href="https://store.mlambda.net/">Get Aleph in the Store</a>
    <a class="btn" href="{{ '/products/aleph.html' | relative_url }}">Aleph, in detail</a>
  </div>
</section>
