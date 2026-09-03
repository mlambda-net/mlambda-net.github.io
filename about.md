---
layout: page
title: About MLambda
subtitle: A software company building the stack for software that is verified before it is built.
description: MLambda is a software company in Heredia, Costa Rica, founded in 2019 by Roy Gonzalez. Compiler tooling, an actor runtime, a distributed database, and an agentic factory.
permalink: /about/
---

<p>MLambda was founded in {{ site.data.company.founded }} in {{ site.data.company.location }},
by <a href="{{ site.data.company.founder.url }}">{{ site.data.company.founder.name }}</a> — a
software architect with eighteen years in distributed systems and a second degree in the
philosophy of formal science. The company exists because of one conviction: most software is
tested after the fact and trusted on faith, and it does not have to be.</p>

<h2>What we build</h2>

<p>A stack whose parts share a premise. <a href="{{ '/products/genesis/' | relative_url }}">Genesis</a>
is a compiler workbench that model-checks a specification before anything is built from it.
<a href="{{ '/products/aleph/' | relative_url }}">Aleph</a> is a language with a native
foreign-function interface. <a href="{{ '/products/actors/' | relative_url }}">MLambda.Actors</a>
is an actor runtime for .NET and <a href="{{ '/products/data/' | relative_url }}">MLambda.Data</a>
a database built entirely out of actors, its consistency model specified in TLA+. On top of them
sits the <a href="{{ '/products/factory/' | relative_url }}">Factory</a>: a society of agents that
turns a plain-language description into a formal specification, verifies it, and generates the
tested, containerised system that follows from it.</p>

<h2>How we work</h2>

<p>Two tiers, stated on every product page. <strong>Open</strong> products are MIT-licensed and
published on NuGet with public documentation. <strong>Commercial</strong> products have public
documentation and are available under licence or through early access. The
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
