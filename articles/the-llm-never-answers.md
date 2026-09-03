---
layout: page
eyebrow: Article · Neuro-symbolic AI
title: The LLM never answers. Only proofs do.
subtitle: Why the only way to let language models build software you can trust is to put a symbolic layer in charge of what they say.
description: Neuro-symbolic AI at MLambda — how Thinker lets language models gather knowledge while an inference engine, a proof kernel and a model checker decide what is admitted; and Hilbert, a transformer that carries five logics inside it.
permalink: /articles/the-llm-never-answers/
image: /images/articles/ns-01-gathers-decides.png
---

<figure class="story-figure">
  <img src="{{ '/images/articles/ns-01-gathers-decides.png' | relative_url }}" alt="Diagram: the neural side acquires content; an admission gate formalises it; the symbolic side — inference engine, proof kernel, model checker — decides." width="1200" height="627">
</figure>

<p>Large language models are extraordinary at one thing and poor at another, and most of the
industry is trying to get the second thing out of the first. They are extraordinary at
<em>acquiring content</em>: reading a requirement, proposing a model, drafting a function,
critiquing a design, at a pace and breadth no team can match. They are poor at
<em>guaranteeing</em> any of it. A model's confidence is a property of its output distribution,
not of the world. Ask it whether a schema is consistent and it will answer fluently either way.</p>

<p>Software is the domain where that gap costs the most, because software is the one artefact
we already know how to reason about exactly. We have had the mathematics for fifty years:
type systems, formal specification, model checking, proof. What we have never had is a way to
produce the raw material — the requirements, the models, the candidate code — fast enough to
be worth proving. Now we do. Which means the question is no longer whether an LLM can write
software. It is who gets to decide that what it wrote is true.</p>

<h2>Two kinds of intelligence, one rule</h2>

<p>Neuro-symbolic AI is often described as a hybrid, as if the point were to blend two
techniques. At MLambda it is a division of labour with a single, non-negotiable rule:
<strong>the neural layer acquires, the symbolic layer decides, and the neural layer never
answers.</strong></p>

<p>Inside Turing, our architecture platform, that rule is a component called Thinker. Language
models — pluggable, with retrieval — read what a person wrote about their business and propose:
here is a persona, here is a command, here is what must never happen twice. Nothing they say is
believed. Each proposal passes through a deterministic grammar that formalises it into a
controlled language, and a verification gate that admits it only if it is well-formed against
the ontology. What is admitted enters a knowledge base; what is not is returned with the reason.</p>

<p>From there, only symbolic machinery runs. Shin, a stratified forward-chaining engine, proves
over the admitted knowledge. A proof kernel re-checks every proof it produces — the prover is
not trusted either. When a requirement implies something the person never said, the engine
derives it and names it as an obligation; it does not ask the LLM to guess. And a symbolic
reinforcement learner adjusts what the system believes over time — not by nudging weights but by
revising rules whose consequences were refuted.</p>

<p>The output is not an answer. It is a proof, or a refusal with a witness.</p>

<h2>Refusal is a result</h2>

<p>This is the part that takes people a moment. In a conventional AI pipeline a refusal is a
failure mode — the thing you prompt around. Here it is the product working. When Turing's model
checker walks every reachable state of a specification and finds the one that violates an
invariant, it does not soften the finding or propose a workaround. It sends the counterexample
back to the requirements. Nothing goes forward to code. The specification is corrected, the
proof is re-run, and only when every safety, liveness and temporal property holds does anything
get generated.</p>

<p>That ordering — prove, then build — is the whole difference between a system that is
<em>tested</em> and one that is <em>verified</em>. Tests are cases somebody remembered. A model
checker does not remember; it enumerates.</p>

<h2>Putting the logic inside the network</h2>

<figure class="story-figure">
  <img src="{{ '/images/articles/ns-02-hilbert.png' | relative_url }}" alt="Diagram of Hilbert: five stacked levels — first-order, relational, modal, temporal, sortal — with a strange loop feeding the top level's error back to the bottom." width="1200" height="627">
</figure>

<p>Thinker keeps the two layers separate and lets the symbolic one govern. Our research
programme asks the harder question: can the logic live <em>inside</em> the network?</p>

<p>Hilbert begins from an observation about attention itself. An attention layer is,
mathematically, an adaptive filter with feedback: the input tokens are the signal, the query,
key and value matrices are the filter weights, the gradient is the error term, and the
optimiser plays the role of the update rule. Adaptive filters learn from each sample as it
arrives. Transformers, as normally trained, do not. Hilbert makes them.</p>

<p>Its architecture is five levels, each carrying a different logic: first-order, with a
contrastive consistency loss; relational, with graph attention over structure; modal, with a
multi-world attention matrix; temporal, with linear temporal logic and dual causal and
bidirectional attention; and sortal, with attention biased by an ontology. Fast weights and
episodic memory connect the levels, so the network can update per input without a training
pass. And a strange loop, after Hofstadter, feeds the top level's error signal back down to
refine the lower four at inference time — the system reasoning about its own reasoning,
mechanically. A genetic layer evolves populations of fast-weight configurations alongside
gradient descent, so exploration and refinement run against each other.</p>

<p>Hilbert is research. It has no public release, and it may fail. But it is the same
commitment as Thinker pursued one level deeper: not a neural system with a reasoner attached,
but a system in which reasoning is what the network does.</p>

<h2>What it means for the people who build software</h2>

<figure class="story-figure">
  <img src="{{ '/images/articles/ns-03-turing-loop.png' | relative_url }}" alt="Diagram of Turing: describe, gather, prove, generate — with refusals looping back from prove to gather." width="1200" height="627">
</figure>

<p>Domain-driven design and distributed architecture are the two things an LLM cannot do on its
own. Both require holding a whole system's invariants in mind and deciding what is true across
them — exactly the faculty a language model lacks and a symbolic layer has. Turing does not
replace the architect. It puts the architect's method — TOGAF's cycle for what exists, Gilb's
quantified requirements for what must hold, reactive domain-driven design for what to build —
inside the loop, where the LLM cannot skip it.</p>

<p>Describe a system in plain language. Agents gather and validate the requirements. Symbolic AI
derives the domain model, the views, the tests and the verification. Only then is the system
generated, on an actor runtime, with its tests as obligations the model already implied. The
language model gathers. The proofs decide.</p>

<p>That is what we mean by treating software as engineering: a specification is a theorem, an
implementation is its proof, and nothing is admitted on faith — least of all by a machine that
is very good at sounding sure.</p>

<hr>

<p class="muted">MLambda builds Turing, the Genesis workbench, the Aleph language, the
MLambda.Actors runtime and MLambda.Data. <a href="{{ '/products/turing/' | relative_url }}">See
Turing run</a>, read <a href="{{ '/method/' | relative_url }}">the method</a>, or
<a href="mailto:{{ site.data.company.email }}?subject=Turing%20demonstration">request a
demonstration</a>.</p>
