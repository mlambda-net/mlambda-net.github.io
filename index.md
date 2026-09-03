---
layout: home
title: MLambda
description: MLambda builds the stack for software that is verified before it is built — a compiler workbench, a language, an actor runtime, a distributed database, and Turing, an agentic architecture platform.
---

<section class="hero">
  <h1>Software that is verified before it is built.</h1>
  <p class="hero__lede">MLambda builds the stack for correct-by-construction systems: a compiler
  workbench that model-checks a specification before anything is generated from it, a
  language that reaches the machine directly, an actor runtime and a database built out of
  actors, a UI framework, a research microkernel, and neuro-symbolic AI.</p>
  <p class="hero__lede">On top of them sits Turing — an architecture platform where a society of
  LLM agents turns a plain-language description into a formal specification, verifies it, and
  generates the tested, deployable system that follows. The language model acquires; rules
  admit; proofs decide.</p>
  <p class="hero__lede">Two tiers, stated on every page: <span class="tier tier--open">Open · MIT</span>
  on NuGet with public documentation, and <span class="tier tier--commercial">Commercial · early access</span>
  with public documentation and source by arrangement.</p>
</section>

<h2>The stack</h2>
<div class="diagram">{% include stack-diagram.svg %}</div>

<h2>Products</h2>
{% assign all = site.products | sort: "weight" %}
<ul class="grid-cards">
{% for product in all %}{% include product-card.html product=product %}{% endfor %}
</ul>

<h2>Method</h2>
<p class="lede">Every system here is specified in Z, model-checked in TLA+, and only then
implemented — by people or by agents — with the tests derived from the model rather than
invented afterwards. <a href="{{ '/method/' | relative_url }}">How MLambda builds software →</a></p>

<h2>Work with MLambda</h2>
<ul>
  <li><strong>Consulting</strong> — architecture and delivery with the MLambda stack.</li>
  <li><strong>Commercial licence and support</strong> — for the commercial-tier products and supported use of the open ones.</li>
  <li><strong>Early access</strong> — private builds and repositories for teams evaluating the commercial tier.</li>
</ul>
<p><a class="btn" href="{{ '/services/' | relative_url }}">Services</a></p>
