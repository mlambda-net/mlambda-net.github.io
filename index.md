---
layout: home
title: MLambda
description: MLambda builds the stack for software that is verified before it is built — a compiler workbench, the Aleph language, an actor runtime, a distributed database, and Turing, an agentic architecture platform.
---

<section class="hero hero--split">
  <div>
    <span class="eyebrow">Software engineering, done as engineering</span>
    <h1>Software that is verified before it is built.</h1>
    <p class="hero__lede">A specification is a theorem. An implementation is its proof. MLambda builds
    the stack that makes that literal — <strong>Turing</strong>, an architecture platform where LLM
    agents turn a plain-language description into a formal model, check it, and generate the
    system that follows; <strong>Aleph</strong>, a pure language in which whole classes of defects
    cannot be written; and a runtime, a database and a UI framework built the same way.</p>
    <div class="hero__actions">
      <a class="btn btn--primary" href="mailto:{{ site.data.company.email }}?subject=Turing%20demonstration">Request a demonstration</a>
      <a class="btn" href="{{ '/products/' | relative_url }}">Products</a>
    </div>
  </div>
  <figure class="shot">
    <img src="{{ '/images/turing/04-model.png' | relative_url }}" alt="Turing composing a Guimel domain model from requirements: entities, commands, events, specifications and an aggregate whose handler allows, requires and emits." width="1894" height="910" loading="eager">
    <figcaption class="mono">Turing — the domain model, composed from the requirements. Where a shape was not stated, it says so.</figcaption>
  </figure>
</section>

<section class="section">
  <h2>Why it matters</h2>
  <p class="section__lede">Most software is built first, tested afterwards, and trusted on faith. Generating it faster does not change that.</p>
  <ul class="thesis">
    <li>
      <h3>The problem</h3>
      <p>Defects are found where they are most expensive — in production — because nothing in the
      process could rule them out earlier. AI code generation raises the volume of code without
      raising the guarantee on any line of it.</p>
    </li>
    <li>
      <h3>The wedge</h3>
      <p>Verification before construction. Requirements become a formal model; the model is
      checked for safety, liveness and consistency; the implementation is derived from it and its
      tests are obligations the model already implies. Agents do the work. Proofs decide.</p>
    </li>
    <li>
      <h3>Why now</h3>
      <p>Language models can finally produce the content — requirements, models, code — at the
      pace a business needs. What they cannot produce is the guarantee. MLambda supplies the part
      that is missing: the mathematics that admits or refuses what the model proposes.</p>
    </li>
  </ul>
</section>

<section class="section">
  <h2>A verifiable model</h2>
  <p class="section__lede">Every MLambda system is checked along four axes before it exists, and built in a language that keeps it that way.</p>
  <ul class="pillars">
    <li class="pillar">
      <span class="pillar__label">Consistency</span>
      <h3>Proved, not promised</h3>
      <p>Specifications in <strong>Z</strong>; models checked in <strong>TLA+</strong> for safety, liveness and temporal properties before a line of code. MLambda.Data's consistency model is a checked specification. Aggregates are derived from invariants, so the boundaries that must hold are the boundaries that exist.</p>
    </li>
    <li class="pillar">
      <span class="pillar__label">Security</span>
      <h3>Refusal is part of the model</h3>
      <p>Who may act, on what, under which guard, and what is emitted when the guard fails — <strong>declared in the domain</strong>, not patched in later. Actors isolate state by construction; cluster nodes speak over <strong>mTLS</strong>; the data gateway authenticates with JWT and routes by role.</p>
    </li>
    <li class="pillar">
      <span class="pillar__label">Performance</span>
      <h3>Measured against the target</h3>
      <p>An actor runtime with reactive messaging; a <strong>log-structured storage engine</strong> with Bloom-filtered reads; Aleph compiled to <strong>native code via LLVM</strong> with a direct FFI and SIMD. Every generated system carries benchmarks — throughput, latency, allocation — and design estimates are compared with what verification measures.</p>
    </li>
    <li class="pillar">
      <span class="pillar__label">Memory and mutation</span>
      <h3>Defects with nowhere to occur</h3>
      <p>Aleph is <strong>pure and immutable by default</strong>: no shared mutable state to race on, no null, no unchecked failure — errors are typed values, cases are matched exhaustively, effects are explicit. Coordination is software-transactional memory and channels, not locks. The bugs mutable languages spend their lifetimes chasing are not expressible.</p>
    </li>
  </ul>
</section>

<section class="section">
  <h2>Software as mathematics</h2>
  <div class="prose">
  <p>Aleph has a pure functional core — Hindley–Milner inference, algebraic data types, traits —
  and it is used as one: MLambda's rendering of <em>Category Theory for Programmers</em> is written
  in Aleph, each chapter a runnable program whose laws are verified by property tests. The same
  discipline runs through the stack. A system's invariants are stated as a theorem; the
  model checker is the referee; the implementation is admitted only as a proof. That is what
  MLambda means by treating software as engineering: not a metaphor, a method.</p>
  </div>
  <ul class="proof">
    <li><span class="proof__num">11</span><span class="proof__label">Genesis packages on NuGet</span></li>
    <li><span class="proof__num">4</span><span class="proof__label">public documentation sites</span></li>
    <li><span class="proof__num">TLA+</span><span class="proof__label">checked consistency model</span></li>
    <li><span class="proof__num">17</span><span class="proof__label">pipeline agents, one per stage</span></li>
    <li><span class="proof__num">2019</span><span class="proof__label">building since</span></li>
  </ul>
</section>

<section class="section">
  <h2>The stack</h2>
  <div class="diagram">{% include stack-diagram.svg %}</div>
</section>

<section class="section">
  <h2>Products</h2>
  <p class="section__lede">Two tiers, stated on every page: <span class="tier tier--open">Open · MIT</span> on NuGet with public documentation, and <span class="tier tier--commercial">Commercial · early access</span> with public documentation and source by arrangement.</p>
  {% assign all = site.products | sort: "weight" %}
  <ul class="grid-cards">
  {% for product in all %}{% include product-card.html product=product %}{% endfor %}
  </ul>
</section>

<section class="section">
  <h2>Built for</h2>
  <p class="section__lede">Teams for whom a defect is not an inconvenience.</p>
  <ul class="verticals">
    <li><strong>Financial services and trading</strong><span>Order flow, positions and settlement, where latency and fault tolerance are architectural constraints — the founder's background is a mission-critical US trading platform.</span></li>
    <li><strong>Logistics and supply chain</strong><span>Integration-heavy systems with many parties and no tolerance for lost messages; the founder's years on DHL's logistics core.</span></li>
    <li><strong>Regulated and safety-critical software</strong><span>Anywhere an auditor asks for evidence. A checked specification and derived tests are the evidence.</span></li>
    <li><strong>Teams adopting AI code generation</strong><span>Keep the speed; add the guarantee. Turing puts a model checker between the language model and your codebase.</span></li>
  </ul>
</section>

<section class="section">
  <h2>What's next</h2>
  <p class="section__lede">Direction, not dates. Genesis and Turing's backlog is public — every gap has an epic and an issue.</p>
  <ul class="roadmap">
    <li><strong>Turing</strong><span>Execute the generated end-to-end suites; deepen static analysis; a catalogue of business agents; deployment-verification depth; hardening of the web surface; a second emission target.</span></li>
    <li><strong>Aleph</strong><span>Networking through the FFI, TLS, a tracing garbage collector, and let-polymorphism for top-level functions.</span></li>
    <li><strong>Genesis</strong><span>Gears promoted to a top-level module; Thinker's deferred capabilities.</span></li>
  </ul>
  <p><a href="https://genesis.mlambda.net/#/architecture/60-status">Read the status register →</a></p>
</section>

<section class="section">
  <h2>Method</h2>
  <p class="lede">Every system here is specified in Z, model-checked in TLA+, and only then
  implemented — by people or by agents — with the tests derived from the model rather than
  invented afterwards. <a href="{{ '/method/' | relative_url }}">How MLambda builds software →</a></p>
</section>

<section class="section">
  <h2>Work with MLambda</h2>
  <ul>
    <li><strong>Demonstration</strong> — see Turing run on a domain you describe.</li>
    <li><strong>Consulting</strong> — architecture and delivery with the MLambda stack.</li>
    <li><strong>Commercial licence and support</strong> — for the commercial-tier products and supported use of the open ones.</li>
    <li><strong>Early access</strong> — private builds and repositories for teams evaluating the commercial tier.</li>
  </ul>
  <div class="hero__actions">
    <a class="btn btn--primary" href="mailto:{{ site.data.company.email }}?subject=Turing%20demonstration">Request a demonstration</a>
    <a class="btn" href="{{ '/services/' | relative_url }}">Services</a>
  </div>
</section>
