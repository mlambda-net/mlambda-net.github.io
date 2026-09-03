---
layout: page
eyebrow: Article · Verification and program analysis
title: The intelligence LLMs are missing
subtitle: A language model predicts the next token over a manifold. Finding a bug is a different act — logic and mathematics — and MLambda's model checker, analysers and derived tests are built to supply it.
description: How MLambda verifies software — a native TLA+ model checker on Shin with certified counterexamples, static and dynamic analysis whose verdicts are rules, test obligations derived from the model, mutation scored exactly — and why this, not more probability, is what lets an LLM find bugs better than a person.
permalink: /articles/the-intelligence-llms-are-missing/
image: /images/articles/ns-10-verification.png
---

<figure class="story-figure">
  <img src="{{ '/images/articles/ns-10-verification.png' | relative_url }}" alt="The intelligence LLMs are missing — prediction over a manifold versus verification by logic and mathematics." width="1200" height="627">
</figure>

<p>Ask a language model whether a function has a bug and it will answer with the confidence of
a colleague and the epistemics of a weather forecast. It is predicting the most probable next
token over a manifold shaped by everything it has read. That is a remarkable thing to be able
to do, and it is not the same act as knowing. A bug is a statement that is false about a
program — an invariant that some reachable state violates, a case the code does not handle, an
obligation the tests never check. Establishing that is logic and mathematics. No amount of
probability becomes it.</p>

<p>This is the intelligence language models are missing, and it is the intelligence MLambda
builds. Not to replace the model — it is very good at proposing — but to give it a faculty it
cannot grow on its own: the ability to <em>verify</em>. What follows is what that faculty
consists of, as built.</p>

<h2>A model checker that lives in a logic engine</h2>

<p>Genesis has a native TLA+ model checker. It takes a real TLA+ subset — <code>.tla</code> with
a <code>.cfg</code> — or a Shin-flavoured dialect, <code>.mtla</code>, that shares Shin's modal
vocabulary (<code>always</code>, <code>eventually</code>, <code>leadsto</code>). It checks
safety and liveness: invariants, deadlock, and temporal properties — <code>&lt;&gt;P</code>,
<code>P ~&gt; Q</code>, <code>[]&lt;&gt;P</code>, <code>&lt;&gt;[]P</code> — under weak and strong
fairness, and it produces counterexample traces. It is consumable as NUnit tests, as a library,
and from the command line.</p>

<p>What makes it unusual is where the verification logic lives. C# does only what a Datalog
engine fundamentally cannot: parsing, evaluating TLA+ expressions to enumerate successor
states, and building property automata. <strong>Every verification decision is a Shin
rule</strong> over a fact encoding of the state graph. This is not an aesthetic choice. Model
checking is reachability as a least fixpoint plus property checks, and Shin's semi-naive
forward chaining <em>is</em> a least-fixpoint engine — reachability is a two-rule program.
Tabled resolution makes queries over cyclic state graphs terminate. Stratified negation and
aggregation express deadlock detection and per-component fairness checks directly. And because
Shin is a modal logic engine, the counterexample the checker reports is re-evaluated by the
LTL evaluator over the trace before it is believed. A counterexample you cannot certify is a
rumour.</p>

<p>The scale is stated honestly: research-grade, on the order of ten thousand to a hundred
thousand states, with correctness ahead of latency ahead of throughput. That is the right
order for a checker whose job is to be trusted.</p>

<h2>Proving the prover</h2>

<p>A checker's verdict rests on its semantics: how it evaluates an LTL formula over a lasso,
how it reduces a TLA+ expression. If the checker and its certifier share that code, a bug in
one is a bug in both and the certification proves nothing. So the verdict-bearing semantics are
expressed a second time, independently, as Shin rules — LTL over a lasso as a least fixpoint
over position facts, TLA+'s operational semantics as a rewrite system of about thirty rules
normalised by Shin's own innermost strategy. Every reported violation is evaluated through both
the C# evaluator and the Shin semantics. <strong>If they disagree, the checker throws</strong>
rather than reports. Two independent implementations of the meaning, agreeing, is what "complete
and consistent" means operationally — not a claim about the checker, but a gate it cannot pass
without earning.</p>

<h2>Static analysis whose verdicts are rules</h2>

<p>Ayin — the Hebrew letter, "eye" — is the module that examines everything Bet generates. Its
static analyses follow one discipline: C# reads and flattens; Shin decides. A C# reader walks a
solution and emits facts — a project references a project, a symbol has a name, a file declares
a type. A <code>.shin</code> file says which combinations of facts are findings and how much
they matter. The layer analysis is a good example: the rules state that <em>actors → gateway</em>
is illegal, <em>repository → gateway</em> is illegal, <em>any ring of references</em> is illegal,
and — in prose above the rules — exactly which directions are deliberately <em>not</em>
enforced and why. Policy changes far more often than the code that reads XML, and only one of
the two should have to change with it.</p>

<p>The same shape covers naming, solution structure, syntax, Docker (pinned base images,
non-root, health checks), and Helm (lint, schema, resource limits, probes). And the artefact
inventory the analyses are measured against is explicit: fifty-eight template-produced artefact
families across six technologies, each with a static column and a dynamic column, so coverage is
a checklist rather than an impression.</p>

<h2>Dynamic analysis that distinguishes "wrong" from "does not work"</h2>

<p>Ayin's dynamic side builds the solution, runs the generated tests, runs the containerised
smoke test, and reads the results — and again the verdict is a rule. Two things in its rule
files show the level of care. The compile phase and the run phase are kept distinct, because a
finding in the first means "it is wrong" and a finding in the second means "it does not work",
and conflating them misleads. And <code>SuiteCoverage</code> records three numbers — tests
discovered on disk, tests executed, whether a results file was produced at all — because
"executed zero" is ambiguous in a way that is dangerous: a suite with no tests, a suite whose
tests were all filtered out, and a suite whose host died before writing results all reach the
results file as the same nothing. The analysis was changed after a solution holding twenty
untouched tests rendered as "the suite executed no tests" at a warning. That is what it looks
like when a tool is built by someone who has been misled by tools.</p>

<p>The emitted TLA+ is model-checked. The emitted Playwright suite is executed. Samek state
machines are simulated for reachability, deadlock and determinism. Dynamic analysis, in Ayin,
means the artefact actually ran and something checkable was measured.</p>

<h2>Tests as obligations, not as guesses</h2>

<p>Generated tests have a specific failure mode: a generated test that asserts nothing still
passes, so "tests are green" is evidence about nothing. Tsadi — "justice" — is the answer. It
is a language for specifying generators, properties, sages and coverage goals, and a module of
specialists that derive test obligations <em>from the model</em> rather than searching for
cases. A test in this system is not something a person remembered to write. It is an obligation
the specification implies, and its absence is a finding.</p>

<p>Mutation testing is scored the same way, and the scoring is a small masterpiece of honesty.
Classical mutation testing compiles and runs the suite once per mutant, which is why it has a
reputation for being unaffordable. Ayin asks a cheaper question with an exact answer: does the
mutant change the set of obligations Tsadi derives from the blueprint? If it does not, the two
blueprints yield identical tests and no derived test can distinguish them — the mutant
<strong>survives, certainly</strong>, without anything being compiled or run. The report leads
with survivors, because that number is measured; "killed" is reported as an upper bound, because
whether the suite actually fails depends on things the analysis cannot see. A tool that reported
the kill rate as if it were measured would be overclaiming, and this one declines to.</p>

<h2>Analysing the analyser</h2>

<p>Underneath Ayin sits a reusable kernel: the four families of program analysis from Nielson,
Nielson and Hankin — data flow, constraint-based, abstract interpretation, type and effect —
written as Shin rules over Shin programs. Data flow is implemented end to end: reaching
definitions over the predicate-dependency graph, groundness and mode analysis, with diagnostics
for dead rules, undefined predicates and unsafe variables. The other three ship as compiling,
queryable scaffolds with their lattices and Galois connections documented. Stated as it is,
because a scaffold described as finished would be exactly the kind of claim this article is
against.</p>

<h2>What it found</h2>

<p>The proof of an analysis is what it catches. When Bet's generated shop system was run through
Ayin, the result was 114 tests — 42 passed, 35 failed, 37 not executed. A person looking at that
sees a red build. The analysis produced a defect table: eight defects, with the failures and
abstentions attributed to them exactly — <em>11 + 10 + 7 + 7 = 35 of 35, none unexplained;
11 + 11 + 15 = 37 of 37, none unexplained</em> — each with its emitter location and a confidence.
It located three true emitter bugs, one in the wrong module (Tsadi, not Bet), and one that no
green build would ever have shown: a handler building an aggregate with an empty identity — a
<strong>false green</strong>, a test passing for the wrong reason. Finding a false green is the
thing a human reviewer almost never does, because a passing test is where the eye stops
looking. The analysis does not have an eye. It has arithmetic that must sum to the total.</p>

<h2>Better than a human, at the part a human is bad at</h2>

<p>This is the sense in which the system finds bugs better than a person. Not by being cleverer
about code — people are extraordinary at that — but by being exhaustive where people are
selective, exact where people estimate, and incapable of the confidence a passing test
inspires. A model checker enumerates every reachable state; a reviewer samples. A derived
obligation is either discharged or not; a written test is whatever someone thought of. A
mutant either changes the obligation set or it doesn't; a kill rate is a story.</p>

<p>And this is what a language model gains when it is put in front of such a system. The model
proposes — a specification, a fix, a test. The checker, the analysers and the derived
obligations decide, with a proof or a counterexample. The model's fluency stops being a risk
and becomes a search strategy over a space where every answer is checked. That is the division
of labour Turing is built on. The language model gathers. The proofs decide. The bugs that get
found are the ones that were <em>there</em>, not the ones that were likely.</p>

<hr>

<p class="muted">The TLA+ checker is part of <a href="{{ '/products/genesis/' | relative_url }}">Genesis</a>
(MIT, on NuGet); Ayin and Tsadi are modules of <a href="{{ '/products/turing/' | relative_url }}">Turing</a>.
Method and architecture at <a href="https://genesis.mlambda.net">genesis.mlambda.net</a>.</p>
