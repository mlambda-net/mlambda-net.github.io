---
layout: page
eyebrow: About
title: About MLambda
subtitle: A software company building the stack for software that is verified before it is built.
description: MLambda is a software company in Heredia, Costa Rica, founded in 2019 by Roy Gonzalez. Languages and compilers, an actor runtime, a distributed database, agents, and the applications built on them.
permalink: /about/
---

<p>MLambda was founded in {{ site.data.company.founded }} in {{ site.data.company.location }}.</p>

<h2>Where it came from</h2>

<p>The mission predates the company. As an enterprise architect applying TOGAF across
consulting and product work, the founder kept meeting the same gap: the architecture was
sound, and the software drifted from it anyway, because nothing but people connected the two.
The answer he set out to build was a system that <strong>understands architecture as TOGAF
describes it</strong>, expresses every domain as a <strong>domain-specific language</strong>, and
runs it on an <strong>actor framework built for reactive domain-driven design</strong>. MLambda was
founded in 2019 to build exactly that — first the actor runtime, then the compiler workbench
the languages needed, then the languages, and now Turing: rational tools that use language
models to gather and validate requirements and symbolic artificial intelligence to derive the
logic, the views, the tests and the verification from them.</p>

<h2>What we build</h2>

<p>A stack whose parts share a premise, every layer written here, in
<a href="{{ '/products/genesis.html' | relative_url }}">MLambda.Genesis</a>.
<a href="{{ '/products/aleph.html' | relative_url }}">Aleph</a> is a pure language with its own native
compiler. <a href="{{ '/products/hilbert.html' | relative_url }}">Hilbert</a> and
<a href="{{ '/products/shin.html' | relative_url }}">Shin</a> hold every formula and every rule, and
<a href="{{ '/products/tensor.html' | relative_url }}">Hilbert.Tensor</a> computes them on the GPU.
<a href="{{ '/products/actors/' | relative_url }}">MLambda.Actors</a> is the actor runtime and
<a href="{{ '/products/data/' | relative_url }}">MLambda.Data</a> a database built entirely out of actors, its
consistency model specified in TLA+. <a href="{{ '/products/max.html' | relative_url }}">Max</a> agents decide by
logic and perceive with <a href="{{ '/products/neuron.html' | relative_url }}">Neuron</a>'s models, and
<a href="{{ '/products/turing.html' | relative_url }}">Turing</a> turns a plain-language description into an
architecture, a model and its design. On top of them run the services and the
<a href="{{ '/products/' | relative_url }}">applications</a> a company uses.</p>

<h2>How we work</h2>

<p>Every change passes the same gates before it moves: tests derived from the model, a quality bar of
0 warnings, security A, reliability A and coverage of at least 95 %, and every screen proved against its prototype
(<a href="{{ '/products/quality.html' | relative_url }}">quality and delivery</a>). Products are released in the
<a href="https://store.mlambda.net/">MLambda Store</a> or available through early access. The
<a href="{{ '/method/' | relative_url }}">method</a> page describes how systems get built here;
the <a href="{{ '/services/' | relative_url }}">services</a> page describes how to work with us.</p>

{% if site.data.company.legal_name != "" %}
<p class="muted">{{ site.data.company.legal_name }}.</p>
{% endif %}

<h2>Contact</h2>

<ul>
  <li><a href="mailto:{{ site.data.company.email }}">{{ site.data.company.email }}</a></li>
  <li><a href="{{ site.data.company.github }}">github.com/mlambda-net</a></li>
</ul>
