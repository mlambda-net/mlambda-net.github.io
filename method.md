---
layout: page
title: How MLambda builds software
subtitle: Specified in Z, checked in TLA+, and only then built — by people or by agents — with the tests derived from the model.
description: The BEAM method and the agentic pipeline behind every MLambda system — formal specification, model checking, generation, derived tests, and measured deployment.
permalink: /method/
wide: true
---

<div class="prose">
<p>Most software is built first and tested afterwards, and the tests are whatever someone
thought to write. Everything at MLambda inverts that. A system exists first as a formal
specification; the specification is model-checked; the implementation follows from it; and
the tests are obligations derived from the model, not guesses about it.</p>
</div>

<h2>The pipeline</h2>
<div class="diagram">{% include pipeline-diagram.svg %}</div>

<div class="prose">
<p><strong>Research</strong> decomposes a business domain into a knowledge graph of processes,
events, data flows, decisions and human roles. <strong>Conceptualisation</strong> turns that
into an actor topology with an explicit supervision hierarchy, human boundaries and interface
surfaces. <strong>Formation</strong> refines colloquial requirements into a purified Z
specification. <strong>Verification</strong> generates an executable TLA+ specification from it
and runs the TLC model checker until every safety, liveness and temporal property holds —
correction loops go back to Formation, not forward to code. <strong>Planning</strong> derives
five artifact plans — mobile UI, web UI, API gateway, backend, infrastructure. Only then:
generation, BDD tests derived from the model, benchmarks, deployment, and measurement whose
evidence returns to the research gap list.</p>

<h2>Four claims the method rests on</h2>

<ul>
  <li><strong>A missing requirement is an unfulfilled obligation</strong> — deduced from the knowledge base, not guessed by a model.</li>
  <li><strong>A waiver is a belief, and closes nothing</strong> until a scope statement a person wrote grounds it.</li>
  <li><strong>The aggregation is derivable</strong>: an invariant spanning two entities forces them into one aggregate, so the connected components of the invariant graph <em>are</em> the aggregates.</li>
  <li><strong>Design estimates, verification measures</strong>, and the difference between them is what the method learns.</li>
</ul>

<h2>The agentic layer</h2>

<p>The pipeline is run by agents. In <a href="{{ '/products/turing/' | relative_url }}">Turing</a>,
a society of agents — a roster, expert agents, code agents — is coordinated by
<strong>Gears</strong>, a build engine that drives declared workflows and writes each agent's
report. As a Claude Code plugin, <strong>MLambda.Actor.Agent</strong> runs the same method with
17 specialised agents, one per stage, from a business description to an actor system deployed
on Kubernetes.</p>

<p>What keeps an LLM-driven pipeline honest is the reasoning layer, <strong>Thinker</strong>.
Language models acquire content — through pluggable providers and retrieval — and a
deterministic grammar formalises what they propose. A forward-chaining engine proves over
the formalised knowledge, a proof kernel re-checks every proof, and a symbolic reinforcement
learner improves what is believed over time. <strong>The LLM never answers; only proofs do.</strong>
The method borrows TOGAF for what exists, Gilb's Planguage for what must hold, and reactive
domain-driven design for what to build.</p>

<p>The full method is documented in the twelve-chapter method book on
<a href="https://genesis.mlambda.net">genesis.mlambda.net</a>.</p>
</div>
