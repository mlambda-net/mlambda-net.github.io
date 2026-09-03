---
layout: page
eyebrow: Article · CAS language, runtime, Scryer
title: The formula is the model
subtitle: A typed algebra language that compiles into your project, a symbolic runtime that differentiates and integrates as pure functions, and the statistics to put stochastic work beside it — built to be carried to other languages.
description: Using Genesis's CAS language and algebra runtime for engineering and actuarial work — read data from a model, adjust, derive and integrate in expressions, compile to C# today, with a language-agnostic design whose second emission target is on the public roadmap; and Scryer's symbolic statistics for stochastic analysis.
permalink: /articles/the-formula-is-the-model/
image: /images/articles/ns-12-cas-engineering.png
---

<figure class="story-figure">
  <img src="{{ '/images/articles/ns-12-cas-engineering.png' | relative_url }}" alt="The formula is the model — a CAS rule compiled through a typed AST into the algebra runtime, with Scryer's statistics beside it." width="1200" height="627">
</figure>

<p>In most engineering and actuarial code, the mathematics lives in two places at once. There
is the formula — in a paper, a spreadsheet, a regulator's document — and there is the code
that is supposed to implement it. They drift. A sensitivity gets hand-differentiated and the
sign is wrong. A present-value rule changes and three implementations change at three
different times. The numbers come out, and nobody can point to the expression they came
from.</p>

<p>The alternative is to make the formula the model: write the mathematics once, in a notation
close to how it is written on the whiteboard; let a type checker verify it; derive what needs
deriving symbolically rather than by hand; and compile the result into the project that has
the data. Genesis has the pieces for that, and this article is about using them — including
what runs today, what is designed but not yet built, and where the honest edges are.</p>

<h2>Reading data from the model, in an expression</h2>

<p>Everything stands on a small expression type — seven constructors — and a set of pure
functions over it. Parse an expression from text, or build one in code; differentiate it with
respect to a variable; integrate it; simplify, expand, solve for roots; expand it as a Taylor
series about a point. Each function takes an <code>Expr</code> and returns a new one. Nothing
is mutated, so a model is a value you can pass around, version, and diff.</p>

<pre><code>var pv     = MathParser.Parse("c * (1 + i)^(-t)");        // present value of a cash flow
var dPV_di = Differentiator.D(pv, new Sym("i"));           // sensitivity to the rate, symbolically
Console.WriteLine(MathPrinter.Print(dPV_di));         // the derivative, as an expression</code></pre>

<p>"Adjust" is a rewrite; "derive" is <code>D</code>; "integrate" is <code>Integrate</code>;
and reading data from the model is evaluating the expression against your bindings
with the numeric evaluator that ships beside the parser. The point is not that these
operations exist — every CAS has them — but that they are library calls in the same process
as your data, returning expressions you can inspect, not opaque numbers.</p>

<h2>Writing the rules the way you think them</h2>

<p>The interesting mathematics in a domain is rarely the built-ins. It is the identities and
transformations specific to the work: how a cash-flow object becomes a discounted value, how a
hazard rate becomes a survival function, which simplifications a regulator's formula permits.
For that, Genesis has the CAS rule language:</p>

<pre><code>module Reserve {
    let discount (i : Number) (t : Number) : Number = (1 + i) ^ (0 - t)

    rule PV : Expr -> Expr {
        | Cash(t, c)          -> Mul(c, Pow(Add(Num(1), Sym("i")), Neg(t)))
        | Add(a, b)           -> Add(PV(a), PV(b))
        | Mul(Num(k), a)      -> Mul(Num(k), PV(a))
        | _ as e              -> e
    }
}</code></pre>

<p>A module holds helpers and rules; a rule is pattern arms with optional guards, over the
expression type. The type system is a simplified Hindley–Milner, so an arm that returns the
wrong kind of thing is an error in the rule file, not a wrong number six months later. The
compiler produces a class implementing <code>IRewriteSystem</code>; you load it, concatenate
its rules with the built-in algebra, choose a rewriting strategy, and the system now knows
your domain's identities as well as it knows the product rule.</p>

<h2>Portable by construction — and what that means today</h2>

<p>Here is the claim, stated carefully. The CAS pipeline is lexer → parser → type checker →
emitter → pretty-printer → compiler. Everything up to the emitter is language-independent:
the typed AST does not know what it will become. <strong>Today there is one emitter, and it
produces C#</strong>, compiled by Roslyn into an assembly that any .NET language can call
directly. That is what ships.</p>

<p>The design intent is that an emitter is a plug-in, not a rewrite: the same typed AST
rendered to Go, Python, Rust, Java or JavaScript is a second emitter and a runtime port of
the algebra's pure functions — not a second language and not a second type checker. Genesis is
a language workbench whose whole purpose is grammars and schemas that generate front-ends, so
this is the shape it is built for. And the platform's own roadmap says where it stands:
Genesis's public status register lists a <em>second emission target</em> as an epic that is
<strong>planned, with no code yet</strong>, with the honest note that a language-agnostic
intermediate model "is untested until a second target exists". So: portable by construction,
one target delivered, the second on the roadmap. If you need the algebra from another language
today, you call the .NET assembly across a process boundary; if you need it native there, that
is the roadmap item, and it is the kind of work the platform exists to make routine.</p>

<h2>Stochastic work: putting statistics beside the algebra</h2>

<p>Actuarial and engineering models are rarely deterministic all the way down. Claims arrive as
distributions; measurements come as intervals; a parameter is "usually here, sometimes there".
MLambda.Scryer is the platform's statistical substrate, and its symbolic half is built for
exactly this kind of data: Edwin Diday's symbolic data analysis, with <strong>interval-valued
variables</strong> (never collapsed to a scalar), <strong>multi-valued variables</strong>, and
<strong>modal variables</strong> — distributions over categories — plus histograms, symbolic
covariance and correlation, the Gowda–Diday dissimilarity for interval objects, and clustering
of symbolic objects with dispersion-based outlier detection. Beside it, the classical tools:
PCA, k-means and DBSCAN, hierarchical clustering with a dendrogram you cut at a height,
nearest neighbours, and ordinary least squares that returns R², residuals and the diagnostics
that let you distrust it.</p>

<p>Two properties matter for stochastic analysis in particular. First, <strong>determinism</strong>:
every place a random choice happens takes an explicit seed and builds its own generator —
never a shared or time-based one — and the tests assert that the same seed reproduces
byte-identical output. A reserve calculation that cannot be reproduced is not a calculation.
Second, the symbolic types are the bridge to the algebra: a modal variable is a distribution
the logic layer can carry as belief with a strength, and an interval is a value the algebra can
propagate rather than a point it has to pretend to know.</p>

<p>What Scryer does not yet have, it says in its own architecture notes: no Monte Carlo or
simulation engine as such, no regularised regression, no online variants, no spatial index for
DBSCAN at large n, no GPU path, and a benchmark table that records the two operations still
below scalar parity rather than hiding them. A stochastic simulation built on Scryer today is
one you assemble from its deterministic, seeded primitives and the algebra's expressions — the
substrate is there; the packaged simulator is not, and this article will not pretend
otherwise.</p>

<h2>Where it belongs</h2>

<p>Reserves and present values, where a discount rule should exist once. Loss models, where a
distribution is the data and an interval is the honest answer. Sensitivities, where the
derivative should be derived, not typed. Engineering models of load and capacity, where the
formula in the standard is the specification and the code must be shown to match it. In all of
these the discipline is the same as everywhere else at MLambda: the mathematics is written
once, checked by a type system, executed as pure functions, and reproducible by seed — and the
numbers are what you get after.</p>

<hr>

<p class="muted"><code>dotnet add package MLambda.Genesis.Algebra</code> — MIT, part of
<a href="{{ '/products/genesis/' | relative_url }}">Genesis</a>. The CAS language, the algebra
and the math expression language are documented at
<a href="https://genesis.mlambda.net">genesis.mlambda.net</a>; Scryer is a module of
<a href="{{ '/products/turing/' | relative_url }}">Turing</a>. For an engagement on a model of
yours, <a href="{{ '/services/' | relative_url }}">write to us</a>.</p>
