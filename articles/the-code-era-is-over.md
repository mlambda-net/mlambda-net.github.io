---
layout: page
eyebrow: Article · Metaprogramming, Guimel, Samek, Bet
title: The code era is over
subtitle: Software engineering information belongs in the requirements, the domain language and the architecture model — not in the code. Genesis is the foundry that makes the code a consequence.
description: Why MLambda treats code as derived rather than written — requirements in a ubiquitous language, a domain model in Guimel, an architecture in Samek inferred by rules, and deterministic pattern machinery that emits the system. The IR makes knowledge language-agnostic; the LLM helps define requirements and never writes the code.
permalink: /articles/the-code-era-is-over/
image: /images/articles/ns-13-knowledge-era.png
---

<figure class="story-figure">
  <img src="{{ '/images/articles/ns-13-knowledge-era.png' | relative_url }}" alt="The code era is over — requirements to Guimel to Samek to emitted code, with the knowledge held above the code." width="1200" height="627">
</figure>

<p>For seventy years the information that defines a software system has lived in its code.
The requirements were written, then the code was written, and from the moment the second act
began the code was the truth and the requirements were a memory. Every architect knows what
happens next: the diagram is right, the document is right, and the system quietly stops being
either. The knowledge is in the code, and the code is the one artefact that no one can read
whole.</p>

<p>That era is ending, and not because language models can type faster. It is ending because
domain-specific languages, intermediate representations and deterministic metaprogramming have
matured to the point where the code can be a <em>consequence</em> of the knowledge instead of
its hiding place. MLambda's Genesis is a foundry built for exactly that: the information lives
in the requirements, the domain language and the architecture model, and the code is derived
from them by provable rules. What follows is how, and — as always here — where the edges are.</p>

<h2>Where the information lives now</h2>

<p>In Turing, a system exists first as requirements written in a <strong>ubiquitous language</strong>:
the terms the business is described in, and no others — each typed as a persona, a command, an
event, a value, a specification, an entity, and each saying which analysis declared it. That is
the layer a language model is allowed to help with. It gathers, proposes, critiques; a
deterministic grammar formalises what it says; the admission gate accepts or refuses it. This
is the one place the model earns its keep, because a good requirement, well understood in the
shared language, is the whole input. Everything below is inference.</p>

<h2>Guimel: the domain, as a language</h2>

<p>Admitted requirements are composed into <strong>Guimel</strong>, a domain-specific language
for reactive, event-sourced microservice systems. One Guimel source projects onto five views of
the same system: the static domain (values, entities, events, commands, specifications,
repositories), the dynamic topology (aggregates as actors with supervision and sharding),
behaviour (handlers as morphisms, <code>Cmd::command → Outcome::event</code>, with predicates,
post-state and triggers in Z-primed form), the user interface (components and views), and the
personas that may act. The language is mutation-free — state change is a functional record
update, <code>self' = { ...self, … }</code> — and kind-tagged, so a handler reads as a contract
rather than a procedure. An aggregate <em>is</em> an actor; a policy <em>is</em> a saga; the
dynamic view is not a second declaration but a projection of the first.</p>

<p>This is the intermediate representation that makes the knowledge language-agnostic. A
<code>.gm</code> file does not know it will become C#. It knows what the system is.</p>

<h2>Samek: the architecture, inferred</h2>

<p>From Guimel, rules infer <strong>Samek</strong> — the state machines and protocol models of
the target architecture. This is the step people find hardest to believe, so it is worth
stating what the inference is. The method's claim is that the aggregation is derivable: an
invariant spanning two entities forces them into one aggregate, so the connected components
of the invariant graph <em>are</em> the aggregates. Boundaries are not chosen by taste; they
are computed from what must hold. The same machinery produces the TLA+ model that is checked
before construction, the Mermaid diagrams, and the prototype — with a Z-checker behind the
handlers so that a behaviour that violates its own predicates is refused, not emitted.</p>

<h2>Bet: deterministic patterns, no model in the loop</h2>

<p>Then construction. Bet is the symbolic construction system, and its architecture notes say
the sentence that matters most: <strong>no language model is involved</strong>. Hand it a
<code>.gm</code> and the whole pipeline runs offline and deterministically — the same domain
produces the same solution, every time. That reproducibility is why the <code>.gm</code> file,
not the prose that produced it, is the platform's pivot.</p>

<p>Bet derives a blueprint, transpiles it, checks the tree it produced, and then runs the tests
it wrote itself. Its emitters are pattern machinery: twenty C# code templates, thirteen
infrastructure templates (Docker, compose, Helm, Kubernetes, Skaffold, nginx), six test
templates; a React prototype transpiler; Mermaid; Samek; TLA+. Rules in Shin decide what to
emit — a sortal-epistemic pattern language, if you like, because the patterns are typed over
sorts and the admission of what they consume was epistemically qualified. The generated actor
carries the comment that is the whole philosophy: <em>convention-synthesized — the body carries
no computation the specification did not already imply.</em></p>

<p>The machine, in other words, obeys a distributed architecture — actors, supervision,
sharding, gateways, sagas, the cluster deployment — because the architecture was <em>stated</em>
in a language whose semantics are patterns it can execute. That is what metaprogramming means
here: not code that writes code, but knowledge with enough structure that code follows from it
by rules you can read.</p>

<h2>What the human does, and what the machine does</h2>

<p>The division is clean and it is not "no humans". The human states the requirements in the
shared language, grounds every waiver — because a waiver is a belief and closes nothing until a
person's scope statement grounds it — and writes the scaffold: which domain, which personas,
which invariants must never be violated. The machine abstracts the patterns, infers the
aggregation and the topology, checks the model, emits the system, derives the tests, and
refuses what it cannot justify. The language model sits on the human side of that line,
helping the requirement become precise. It never sees the code. The code is inference from a
good requirement.</p>

<h2>Where the edges are</h2>

<p>Three, stated plainly. The C# target is the one that exists; Bet's design claim of a
language-agnostic model rendered to any language is, in the platform's own status register, an
epic marked planned with no code yet, "untested until a second target exists" — Java and Go are
the design, not the delivery. The generated systems are analysed hard, and the analysis finds
real defects in the emitters — the shop findings attributed thirty-five test failures to eight
defects, three of them in Bet's own templates — which is the process working, not the process
finished. And Genesis itself is version 0.x on NuGet: a foundry in daily use, not a product with
a support line. The thesis does not depend on any of this being done; it depends on the
direction being right, and the direction is the one every other part of this stack is built to
serve.</p>

<h2>The knowledge era</h2>

<p>When the code is derived, the code stops being where the truth lives. Change the requirement
and the model, the architecture, the tests and the code change with it, consistently, because
they were never separate things — they were projections. Read the Guimel and you have read the
system. Read the refusals and you have read what the system would not accept. The engineering
information is in the engineering artefacts, which is where every other engineering discipline
has always kept it, and the code is the thing the foundry pours.</p>

<p>That is the era MLambda is building for. Not fewer engineers — engineers who write what a
system <em>is</em>, in languages made for saying so, and let provable machinery say the rest.</p>

<hr>

<p class="muted"><a href="{{ '/products/turing/' | relative_url }}">Turing</a> is the platform;
<a href="{{ '/products/genesis/' | relative_url }}">Genesis</a> is the foundry (MIT, on NuGet).
Guimel, the method book and Bet's architecture are documented at
<a href="https://genesis.mlambda.net">genesis.mlambda.net</a>.</p>
