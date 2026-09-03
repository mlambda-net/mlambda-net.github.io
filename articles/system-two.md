---
layout: page
eyebrow: Article · Neuro-symbolic AI
title: System 2 for machines
subtitle: Language models are System 1 — fast, fluent, intuitive, and unable to check themselves. The next level of AI is a System 2 that reasons in logic. MLambda builds that engine.
description: A plain account of what large language models cannot do — verify, plan, know what they know — why the psychology of System 1 and System 2 explains it, why frontier labs are pairing models with formal verifiers, and how MLambda's expert system (sortal, modal, epistemic and deontic logic in Shin) is built as the System 2 that makes AI trustworthy enough to buy.
permalink: /articles/system-two/
image: /images/articles/ns-14-system-two.png
---

<figure class="story-figure">
  <img src="{{ '/images/articles/ns-14-system-two.png' | relative_url }}" alt="System 2 for machines — a fast intuitive language model paired with a slow logical verifier." width="1200" height="627">
</figure>

<p>Daniel Kahneman gave us the most useful map of the mind that a business audience has ever
adopted: <strong>System 1</strong>, fast, automatic, associative, effortless — and
<strong>System 2</strong>, slow, deliberate, logical, effortful. System 1 recognises a face,
finishes a sentence, senses that something is off. System 2 checks the arithmetic, follows a
proof, notices that two beliefs contradict each other. Neither is optional. A mind with only
System 1 is fluent and confidently wrong; a mind with only System 2 never gets anything done.</p>

<p>A large language model is a System 1. That is not an insult — it is the most precise thing
one can say about it, and it is the key to what it can and cannot do, and therefore to what it
is worth. This article is about the missing half, why the field is now building it, and what
MLambda has built.</p>

<h2>What a language model actually is</h2>

<p>A language model predicts the next token given the tokens before it, over a distribution
learned from an enormous corpus. Everything it does — answering, coding, summarising — is that
one act, repeated. The consequences are structural, not bugs to be patched:</p>

<ul>
  <li><strong>It cannot verify.</strong> Verification means holding an answer against a
  standard independent of how the answer was produced. A model checking its own output is
  running the same process again; a second sample is not a second opinion. The research
  community has said this plainly: Kambhampati and colleagues' ICML position paper concludes
  that autoregressive language models cannot, by themselves, plan or self-verify — and that
  self-verification is, after all, a form of reasoning.</li>
  <li><strong>It cannot plan.</strong> Planning requires maintaining a state, applying rules,
  and rejecting branches that violate constraints. Models produce plausible-looking plans and
  lose track of the state that makes them valid; follow-up work found they can plan reliably
  only when an external system tells them what is legal at each step.</li>
  <li><strong>It does not know what it knows.</strong> Ask a model how confident it is and you
  receive a number produced the way every other token is produced. It has no epistemic state —
  no distinction between what it was told, what it inferred, and what it made up. That is the
  mechanism of hallucination: not a failure of the objective but a property of it. The most
  probable continuation is often false, and nothing in the process can tell.</li>
  <li><strong>It cannot be consistent.</strong> Two answers to two phrasings of one question
  can contradict each other, and the model has no representation in which the contradiction
  exists. Consistency is a relation between statements; a token predictor has no statements,
  only strings.</li>
  <li><strong>It cannot decide the undecidable, and does not know where the line is.</strong>
  Recent work characterising how models reason about program termination — the halting
  problem in miniature — finds them confidently answering questions no procedure can settle.
  System 1 has no sense of its own boundary.</li>
</ul>

<p>Every one of these is a System 2 faculty. None of them arrives by scaling System 1.</p>

<h2>Why the direction is already set</h2>

<p>The clearest signal is what the frontier laboratories did when they wanted results that had
to be <em>right</em>. DeepMind's AlphaGeometry pairs a language model with a symbolic deduction
engine; AlphaProof pairs a model with the Lean proof assistant and a search that proves or
disproves each candidate formally. Together they reached silver-medal level on the 2024
International Mathematical Olympiad — the model proposing, a formal system deciding. Reported
follow-ups in 2025 pushed formal provers to gold-medal Olympiad performance and to solving
every problem on the Putnam competition. None of this was achieved by a larger model alone. It
was achieved by giving System 1 a System 2 that cannot be fooled.</p>

<p>The academic literature has converged on the same shape. Surveys of neuro-symbolic AI
describe a field "gaining renewed attention as a way to overcome the limitations of large
language models in complex reasoning"; the LLM-Modulo framework formalises the arrangement —
the model generates, external verifiers and critics decide, and the loop continues until the
verifiers are satisfied. Work on enterprise agents reports large gains from grounding a model
in an <em>ontology</em> — typed knowledge with rules — over plain retrieval. And Gary Marcus,
the field's most persistent critic of scale-alone, points to AlphaProof as the demonstration
that the future is hybrid.</p>

<p>For an investor this is the important paragraph. The question is no longer whether AI needs
a symbolic System 2. The question is who builds one that is general enough to sit under a
business, not just a maths competition — and that is a systems-engineering problem, not a
model-training problem.</p>

<h2>What a System 2 for machines has to be</h2>

<p>Stated without jargon, a System 2 must be able to do four things to what System 1
proposes:</p>

<ol>
  <li><strong>Type it</strong> — decide what kind of thing a claim is about, and reject claims
  that mix kinds: a duty owed by a number, a person who is also a company. This is
  <em>sortal</em> logic.</li>
  <li><strong>Qualify it</strong> — distinguish what is known from what is believed, and by
  whom; what must be from what merely is; what is obligatory from what is permitted; what
  holds now from what must eventually hold. These are the <em>epistemic</em>, <em>alethic</em>,
  <em>deontic</em> and <em>temporal</em> modal logics, and they are exactly the distinctions a
  business runs on.</li>
  <li><strong>Check it</strong> — for consistency with everything already admitted, and
  against invariants that must never be violated, exhaustively rather than by sampling.</li>
  <li><strong>Explain it</strong> — return the proof behind a yes, the counterexample behind a
  no, and an honest "I don't know" when neither exists.</li>
</ol>

<h2>The engine MLambda built</h2>

<p>This is what Thinker — the reasoning layer inside Turing — is, and what makes it a System 2
rather than another prompt. Knowledge is held as an ontology with a written formal semantics:
an ontological network of kinds and duties, a semantic network of things, a statement language
stratified into facts, a sortal layer, and a modal layer. Rules and facts are expressed in Shin,
a rule language whose engine carries four families of modal logic — epistemic (S5), deontic
(KD), temporal (LTL), alethic — plus forward and backward chaining, truth maintenance,
abduction and explanation. Nothing a model proposes enters the knowledge base until it passes
an admission gate: well-formed, correctly sorted, consistent with what is already there.</p>

<p>The visible result is that every answer carries a verdict a System 1 cannot produce:
<strong>Known</strong> (provable from confirmed axioms), <strong>Believed</strong> with a
confidence equal to its weakest link, <strong>Unknown</strong>, or
<strong>Contradicted</strong> — with a proof or citations attached, and with provenance: who
believes this, and why. The system knows what it knows, how well, and from whom, because that
knowledge is a data structure rather than a feeling. Underneath, for the questions that are
about software itself, sits a native TLA+ model checker that enumerates every reachable state
of a specification and returns a certified counterexample when one exists.</p>

<p>The division of labour is the one the research points to, made operational: <strong>the
language model gathers; the proofs decide.</strong> System 1 is used everywhere and trusted
nowhere. That is not a limitation on the model. It is the arrangement that makes the model
usable for anything that has to be right.</p>

<h2>What this is worth, and to whom</h2>

<p>A System 2 is worth money exactly where a wrong answer costs money. Regulated industries,
where an auditor asks for evidence rather than confidence. Financial systems, where a plausible
trade is not the same as a valid one. Logistics, where a contract that drifts costs real
vehicles real hours. And software engineering itself — the domain where the standard of
correctness is already formal, and where MLambda's Turing applies this engine to turn
requirements into verified systems, with the model helping define the requirement and never
writing the code.</p>

<p>The commercial claim is modest and checkable: MLambda does not sell a smarter model. It
sells the faculty that makes any model's output admissible — the typing, qualifying, checking
and explaining that turn a fluent guess into a claim with a status. Every model on the market
is a System 1. The System 2 is the scarce part, and it is engineered, not trained.</p>

<h2>The scientific spirit, kept</h2>

<p>Two honesties, so that the argument does not overreach. First, "neuro-symbolic" is a
direction with open problems: how much of the symbolic layer can be learned rather than
written, how to keep formalisation from becoming a bottleneck, and how far ontological
grounding generalises beyond the domains it was built for — MLambda's own research line,
Hilbert, exists because those questions are unsettled. Second, a System 2 is only as good as
the knowledge admitted into it; the gate can refuse the ill-formed and the contradictory, but a
consistent falsehood that no axiom contradicts will pass. That is why provenance and
human-grounded axioms are part of the design rather than decoration. Kahneman's point was never
that System 2 is infallible. It was that without it, System 1 does not know when it is wrong —
and neither, today, does a language model on its own.</p>

<h2>Sources</h2>

<ul>
  <li>Daniel Kahneman, <em>Thinking, Fast and Slow</em> (2011) — the System 1 / System 2 account.</li>
  <li>Kambhampati et al., <a href="https://proceedings.mlr.press/v235/kambhampati24a.html">Position: LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks</a>, ICML 2024.</li>
  <li><a href="https://proceedings.iclr.cc/paper_files/paper/2025/file/c1e67cde895c3c91edb43569ad0df260-Paper-Conference.pdf">LLMs Can Plan Only If We Tell Them</a>, ICLR 2025.</li>
  <li><a href="https://opendatascience.com/alphaproof-and-alphageometry-2-solve-advanced-math-problems/">AlphaProof and AlphaGeometry 2</a> — DeepMind's IMO 2024 silver-medal result; <a href="https://arxiv.org/abs/2605.22763">Advancing Mathematics Research with AI-Driven Formal Proof Search</a> for the 2025 Olympiad and Putnam results.</li>
  <li><a href="https://arxiv.org/abs/2505.05758">APOLLO: Automated LLM and Lean Collaboration for Advanced Formal Reasoning</a>.</li>
  <li><a href="https://arxiv.org/abs/2411.04383">Neuro-Symbolic AI: Explainability, Challenges, and Future Trends</a>.</li>
  <li><a href="https://arxiv.org/abs/2604.00555">Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems</a>.</li>
  <li><a href="https://arxiv.org/abs/2601.18987">LLMs versus the Halting Problem: Characterizing Program Termination Reasoning</a>.</li>
  <li>Gary Marcus, <a href="https://garymarcus.substack.com/p/alphaproof-alphageometry-chatgpt">AlphaProof, AlphaGeometry, ChatGPT, and why the future of AI is neurosymbolic</a>.</li>
  <li><a href="https://github.com/LAMDA-NeSy/Awesome-LLM-Reasoning-with-NeSy">Awesome LLM Reasoning with NeSy</a> — a maintained bibliography of the field.</li>
</ul>

<hr>

<p class="muted">Thinker and the expert society are part of <a href="{{ '/products/turing/' | relative_url }}">Turing</a>;
Shin and the TLA+ checker are <a href="{{ '/products/genesis/' | relative_url }}">Genesis</a> packages.
Related: <a href="{{ '/articles/the-llm-never-answers/' | relative_url }}">The LLM never answers</a> ·
<a href="{{ '/articles/context-that-has-been-proved/' | relative_url }}">Context that has been proved</a> ·
<a href="{{ '/articles/the-intelligence-llms-are-missing/' | relative_url }}">The intelligence LLMs are missing</a>.
<a href="mailto:{{ site.data.company.email }}?subject=Turing%20demonstration">Request a demonstration.</a></p>
