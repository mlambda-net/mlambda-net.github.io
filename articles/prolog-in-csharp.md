---
layout: page
eyebrow: Article · Shin
title: Prolog in C#, declaratively
subtitle: Shin is a rule language whose programs become C# at build time — forward chaining, tabled backward chaining, term rewriting, four modal logics, and a proof tree for every answer.
description: Shin, MLambda's rule-based expert-system language — pattern matching over typed records, a hybrid Rete/SLD/Stratego kernel, modal logics, truth maintenance, explanation and abduction — compiled to C# by a Roslyn source generator, and used to certify the TLA+ checker's own semantics.
permalink: /articles/prolog-in-csharp/
image: /images/articles/ns-08-shin.png
---

<figure class="story-figure">
  <img src="{{ '/images/articles/ns-08-shin.png' | relative_url }}" alt="Shin — rules and queries over typed records, compiled to C#, run by a hybrid inference kernel." width="1200" height="627">
</figure>

<p>Every serious C# codebase eventually grows a rules engine. It starts as a switch statement,
becomes a chain of <code>if</code>s with comments explaining the order, and ends as a class
nobody wants to touch because the logic and the plumbing have fused. The reason is that C# is
a language for saying <em>how</em>; the rules were always a statement of <em>what</em>.</p>

<p>Shin is MLambda's answer: a rule-based expert-system language in which you declare
facts, rules and queries the way you would in Prolog or Datalog — and which compiles, at
build time, into ordinary C# that links against a runtime engine. No interpreter to embed, no
strings to parse at startup. The rules are source; the C# is generated.</p>

<h2>What a Shin program looks like</h2>

<p>Facts are typed records — Haskell-style algebraic data types with product, sum and payloads.
Rules are predicates over them: a <code>when</code> clause that is a full first-order formula
with modal operators, and a <code>then</code> clause that asserts, retracts, emits or binds.
Queries use Prolog's <code>:-</code>, compose rules and other queries, recurse freely, and
return either a truth value, a list comprehension, or a bound last parameter — Prolog's mode
discipline, made explicit.</p>

<p>Here is a rule file from MLambda's own analysis module, deciding whether an analysed
specification says enough to be finished:</p>

<pre><code>record StoryFacts { id: String, name: String, narrative: String, acceptance: String, cases: String }

-- A story with no acceptance cannot be accepted: that is an error, not taste.
rule story_without_acceptance(s: StoryFacts)
  when s is StoryFacts { acceptance: "no", ... }
  then assert SpecFinding { id: s.id, severity: "error", says: "no acceptance scenario" }</code></pre>

<p>Read the comment in the original source: <em>"Whether a trigger is PRESENT is a fact;
whether it is a GOOD trigger is not, and a rule that pretended otherwise would be guessing in
the voice of a checker."</em> That sentence is the whole discipline. Rules decide facts; they
do not impersonate judgment.</p>

<h2>Pattern matching that earns the word</h2>

<p>Matching in Shin is structural over records: bare-name variables bind, <code>as</code> binds
the whole match, <code>...</code> takes the rest, <code>{ name, ... }</code> is field shorthand,
and <code>|</code> gives value disjunction inside a pattern. Every parameter is typed — a
concrete record type or a type variable in the ML style (<code>'a</code>) — and
<code>(c: Class)</code> is sugar that desugars into a type-constraint conjunct, so the unifier
always knows what it is unifying. Rules with the same name and different parameter types
dispatch by backtracking on pattern failure: overloading with no dispatch machinery, just
Prolog. A singleton-variable diagnostic catches the typo you would otherwise ship.</p>

<h2>Three engines under one knowledge base</h2>

<p>Most rule systems pick one evaluation strategy. Shin's kernel is a hybrid, and each part is
there because it earns its keep. <strong>Forward chaining</strong> is semi-naive Datalog
evaluation — the algorithm behind Soufflé and DDlog — deriving consequences as facts arrive.
<strong>Backward chaining</strong> is SLD resolution with tabling, so recursive queries
terminate, and stratified negation as failure, with unstratifiable programs rejected at build
time rather than looping at run time. <strong>Term rewriting</strong> is a Stratego-style
strategy interpreter — innermost, outermost, and the classic combinators — over typed term
trees.</p>

<p>The knowledge base underneath all three is an immutable persistent structure (HAMT-backed).
Every assert returns a new version with structural sharing. Reads are lock-free, tabling is
trivially safe because a memo key is a goal plus a version, and you get time-travel for free:
any earlier state of the world is still a valid value.</p>

<h2>The intelligence kit</h2>

<p>On top of the kernel: justification-based truth maintenance, so retracting a premise
cascade-retracts everything that depended on it. Aggregation, incremental over the delta.
Defeasible rules with explicit strength and <code>defeats</code>. Probabilistic facts with
confidence propagation. Meta-rules that inspect the engine's own execution traces to ask
whether a program is sound, complete, terminating or consistent. And two constructs Prolog
never had as first-class citizens: <code>explain</code>, which returns the proof tree behind an
answer, and <code>abduce</code>, which returns the minimal set of facts that would make a goal
true. When the reasoning layer inside Turing refuses a proposal, the refusal comes with its
proof.</p>

<p>Four families of modal logic are available in <code>when</code> clauses and assertions:
temporal (LTL), epistemic (S5), deontic (KD) and alethic (S5). They are strictly unary at the
surface — <code>necessary (P and Q)</code> is a syntax error; you must distribute it — which
forces correct distribution and keeps the parser honest. The engine evaluates them over
explicit Kripke frames it maintains internally; the language surface stays small.</p>

<h2>Metaprogramming: rules become C# at build time</h2>

<p>This is the part that makes Shin usable in an ordinary .NET solution. A <code>.shin</code>
file is compiled by a Roslyn incremental source generator during MSBuild. The generator
parses, desugars to a core AST, normalises the first-order formulas into Horn clauses — Kripke
encoding for the modal operators, CNF, skolemisation — and emits C#: a <code>Tags</code> class,
a sealed record per fact type, and an engine class that registers the rules with the runtime.
The generated file for the rule above is called <code>Specification_staticEngine.g.cs</code>
and reads like code a careful engineer would have written. Build-time diagnostics
(<code>SHIN0001</code>–<code>SHIN0099</code>) catch the untyped parameter, the unstratifiable
negation, the modal operator in the wrong position — before anything runs.</p>

<p>The consequence is that a C# project can contain Prolog-style knowledge as source, with
IntelliSense-adjacent tooling, versioned in git, checked in CI, and callable from ordinary
code as typed methods returning <code>IAsyncEnumerable&lt;Binding&gt;</code>. Declarative
where the logic is declarative, imperative where it isn't, and the boundary is a file
extension.</p>

<h2>Theorem proving, and proving the prover</h2>

<p>The deepest use of Shin inside MLambda is on the TLA+ checker in Genesis. A model checker's
verdict rests on its semantics — how it evaluates an LTL formula over a lasso, how it reduces a
TLA+ expression. If the checker and the certifier share that code, a bug in one is a bug in
both, and the certification proves nothing. So the verdict-bearing semantics are being
expressed a second time, <strong>as Shin rules</strong>: LTL over a lasso as a least fixpoint
over position facts, and TLA+'s operational semantics as a rewrite system of about thirty rules
normalised by Shin's own innermost strategy. Every reported violation is then evaluated through
both the C# evaluator and the Shin semantics, and if they disagree, the checker throws rather
than reports. Two independent implementations of the meaning, agreeing, is how you trust a
verdict — and one of them is a declarative program in a language that compiles to C#.</p>

<p>Shin is also used to analyse Shin: data-flow, constraint-based and abstract-interpretation
analyses from Nielson, Nielson and Hankin, written as Shin rules over Shin programs, because a
Datalog engine is already a least-fixpoint engine and that is exactly what a monotone framework
needs.</p>

<h2>Where it sits</h2>

<p>Shin is one of the eleven Genesis packages and ships MIT on NuGet. Inside Turing it is the
reasoning layer's proof engine — the thing that decides, after the language model has
proposed. It is research-grade and multi-year by design; the runtime's stated priority order is
correctness, then latency, then throughput, then memory, and optimisation waits until the engine
is provably conformant to its formal semantics. That order is the reason it is trusted with
verdicts.</p>

<hr>

<p class="muted"><a href="{{ '/products/genesis/' | relative_url }}">Genesis</a> — MIT, on NuGet.
Documentation at <a href="https://genesis.mlambda.net">genesis.mlambda.net</a>.</p>
