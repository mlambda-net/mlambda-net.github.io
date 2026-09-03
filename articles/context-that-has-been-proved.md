---
layout: page
eyebrow: Article · Thinker, the expert society, Scryer
title: Context that has been proved
subtitle: Retrieval hands a language model passages that look relevant. MLambda hands it an ontology that has been admitted, a verdict that says how much it knows, and statistics it can reason about modally.
description: How MLambda does context-augmented generation — an ontological and semantic network verified by a sortal-modal logic layer (Shin), expert layers that make a language model's answers checkable, a four-valued verdict that is the system's own epistemic state, and Scryer, the statistical substrate whose modal variables the logic can classify.
permalink: /articles/context-that-has-been-proved/
image: /images/articles/ns-11-cag.png
---

<figure class="story-figure">
  <img src="{{ '/images/articles/ns-11-cag.png' | relative_url }}" alt="Context that has been proved — retrieval by similarity versus context assembled from a verified ontology, with the answer checked after generation." width="1200" height="627">
</figure>

<p>Retrieval-augmented generation is the industry's answer to a model that makes things up:
find the passages that look relevant, put them in front of the model, hope the answer stays
inside them. It helps. It does not change what the model is doing, which is predicting tokens
in the presence of some text. The passages were chosen by similarity. Nothing checked that
they were true, consistent with each other, or complete; nothing checks the answer against
them afterwards except another model.</p>

<p>MLambda's approach is often described as context-augmented generation, and the phrase is
fair as long as you are precise about the context. The context is not text that resembles the
question. It is a knowledge base that has been <em>admitted</em> — every statement in it passed
a verification gate before it was allowed in — organised as an ontology with a formal
semantics, and the answer is analysed against that knowledge after the model has spoken. The
model gathers. The proofs decide. This is what that means for questions and answers.</p>

<h2>Two networks wearing one store</h2>

<p>Thinker — the reasoning layer inside Turing — keeps its knowledge as two graphs that are
deliberately drawn apart. The <strong>ontological network</strong> is about kinds: what may
exist and what it owes. Sorts and their subsumption (<code>sort Employee : Person</code>),
disjointness (<code>exclusive</code>), relations with typed argument sorts, chaining rules,
duties and eventual states. The <strong>semantic network</strong> is about things: individuals,
the facts asserted of them, the links between them, and who claims what. Drawing them together
buries both — a sort with forty instances would drown the subsumption lattice that explains
it — so they are kept as two views on one store.</p>

<p>The formalism is written down, not implied. A signature of concept, role, individual and
agent names; a statement language stratified into three layers — L0 facts (<code>IsA</code>,
<code>Link</code>), L1 the sortal TBox (subsumption, signatures, exclusion, unary rules), L2
the modal layer (agent claims, obligations, liveness); and a model-theoretic semantics for L0
and L1 that is exactly RDFS plus disjointness plus role domain and range — a named sub-fragment
of the description logic the notation is borrowed from. The document also says what is missing:
no concept constructors yet, and term identity is syntactic, so sense disambiguation is not
part of the signature. That candour is the point of writing a formalism at all.</p>

<h2>A sortal-modal logic layer, in Shin</h2>

<p>Rules and facts over these networks are expressed in Shin, and Shin is what makes the three
layers checkable rather than merely stored. The sortal layer is the type system: every
parameter typed, every relation with domain and range, so an ill-sorted claim — a duty owed by
a number, a person who is also an organisation — is rejected as ill-formed before it is
reasoned about. The modal layer is where the interesting verification lives. Epistemic
statements say who knows or believes what, in S5. Deontic statements say what a sort <em>must</em>
have or do, in KD. Temporal statements say what must eventually hold, in LTL. Alethic
statements say what is necessary rather than merely true. Each family has its axioms; the engine
evaluates them over explicit frames it maintains internally; and because the modal operators
are strictly unary at the surface, a claim cannot be smuggled into the knowledge base in a
form the logic cannot distribute over.</p>

<p>So "verifying semantic, deontic and epistemic information" is not a figure of speech here.
It is three families of rules, with formal semantics, running over typed facts, at the
admission gate.</p>

<h2>The gate, the loop, and what the model is allowed to do</h2>

<p>Nothing a language model says enters the knowledge base directly. It proposes, in
controlled English — a deterministic, LLM-free grammar parses that into statements — and every
statement passes the <strong>verification gate</strong>: well-formed, then sortal, then
consistent with what is already admitted. What fails comes back with the reason. When a
question cannot be answered, an <strong>abduction loop</strong> asks what minimal facts would
make it answerable and goes looking for them — through the model, through retrieval, through a
research agent that polls sources in rounds and stops when a round admits nothing. And a
<strong>symbolic reinforcement learner</strong> revises what is believed over time: credit is
assigned by blame along proof trees, trust in sources is tracked, contradictions are repaired
in the AGM sense during a sleep cycle, and repeated patterns are induced into rules. The model
is used everywhere, and it decides nowhere.</p>

<h2>Expert layers</h2>

<p>Turing's agents are experts, and each expert is a mind of this kind — its own knowledge
base, its own compiled rule packs, its own ontology. Seven of them today: Gilb (quantified
requirements), Project (backlog), ECommerce, UX, Design (domain-driven design), Solution,
Analysis — 378 admitted statements between them, exported from the running minds into
documentation that is regenerated, never hand-edited. When a question about a domain arrives,
it is not one model with one prompt. It is the relevant expert's ontology assembled into a
context pack, the model asked in the presence of that context, and the answer analysed against
the expert's knowledge before it is reported. The exported knowledge page notes something worth
repeating: every expert's semantic network is empty. Three hundred and seventy-eight statements,
and not one about an individual — because what an expert knows is <em>kinds and duties</em>,
and the individuals arrive with each project. The ontology is the expertise.</p>

<h2>An answer that says what it is</h2>

<p>This is where the difference from retrieval becomes visible to a user. Every answer Thinker
gives is epistemically qualified, with a four-valued verdict:</p>

<ul>
  <li><strong>Known</strong> — provable from human-confirmed axioms alone.</li>
  <li><strong>Believed</strong>, with a confidence — provable, but the proof uses learned
  knowledge, and the confidence reported is the weakest belief in the support, never a stronger
  one.</li>
  <li><strong>Unknown</strong> — neither the statement nor its negation is provable. The system
  can honestly say "I don't know."</li>
  <li><strong>Contradicted</strong> — both are derivable; an integrity constraint is violated,
  and this is the signal the repair loop acts on.</li>
</ul>

<p>Ask <em>why</em>, and you get the proof. Ask <em>who believes that</em>, and you get the
provenance. When the verdict stays Unknown after research, a second tier composes a
<strong>grounded</strong> answer: it generates only from retrieved passages and validates
coverage — and it is labelled as grounded, with citations, never with a proof. Retrieval is in
the system, in other words, but it is the fallback below proof, and it says so.</p>

<h2>Meta-cognition, without the mysticism</h2>

<p>A language model cannot reliably report its own epistemic state. Ask it how sure it is and
you get a number generated the way everything else is generated. Here the epistemic state is a
data structure. The system knows whether a claim rests on axioms or on learning, how strong the
weakest link is, which source it came from, whether it conflicts with anything, and it can
inspect its own execution traces to ask whether a rule program is sound, complete, terminating
or consistent. Beliefs are Beta distributions updated by evidence; trust in a source is a
model; the reply kinds include Introspection. Call it meta-cognition if you like — it is
knowing what you know, how well, and from whom — but it is built from ordinary logic and
bookkeeping, and that is why it is trustworthy.</p>

<h2>Scryer: statistics the logic can reason about</h2>

<p>Knowledge is not all symbolic. Requirements have measurements, systems have behaviour under
load, and expert judgment is often a distribution rather than a fact. MLambda.Scryer is the
platform's mathematical substrate for that: SIMD-accelerated vectors and matrices; clustering
(k-means, DBSCAN, hierarchical with dendrograms); PCA; regression that returns its diagnostics
so you can distrust it; nearest-neighbour classification; and — the part that matters for
reasoning — Edwin Diday's <strong>symbolic data analysis</strong>: interval-valued variables,
multi-valued variables, and <strong>modal variables</strong>, which are distributions over
categories rather than single values.</p>

<p>That last kind is the bridge. A modal variable says "this attribute is <em>usually</em> X,
<em>sometimes</em> Y" as a distribution; Shin's probabilistic facts carry confidence; its
alethic layer distinguishes what is necessary from what is merely the case. So statistical
information from Scryer can be admitted as belief with a strength, classified by the sortal
layer, and asked about modally: is this property necessary for the sort, or only frequent in
the sample? Thinker's heuristic layer already represents concept-graph edge weights as
symbolic values — points, intervals, distributions — and uses formal concept analysis and
manifolds over them to prune context. The numbers become something the logic can hold, not
something the model has to eyeball.</p>

<p>Scryer's own documentation includes measured performance numbers, including one place where
the vectorised primitive measured <em>slower</em> than a plain loop, said plainly rather than
hidden. That is the same temperament as everything above.</p>

<h2>What changes for the person asking</h2>

<p>You ask a question. The relevant expert's ontology is assembled into the context. The model
answers in its presence. The answer is analysed against the knowledge — parsed, admitted or
refused, proved if it can be — and comes back labelled Known, Believed with a confidence,
Unknown, or Contradicted, with a proof or citations attached. If it is wrong, you can see why
and where. If the system does not know, it tells you, instead of producing the most probable
paragraph. That is context-augmented generation as MLambda means it: the context is proved
before it is used, and the answer is checked after it is given.</p>

<hr>

<p class="muted">Thinker and the expert society are part of <a href="{{ '/products/turing/' | relative_url }}">Turing</a>;
Shin is a <a href="{{ '/products/genesis/' | relative_url }}">Genesis</a> package. Architecture,
the ontology formalism and the exported knowledge at
<a href="https://genesis.mlambda.net">genesis.mlambda.net</a>.</p>
