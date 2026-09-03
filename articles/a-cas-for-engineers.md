---
layout: page
eyebrow: Article · Genesis Algebra and the CAS rule language
title: A computer algebra system for engineers, in C#
subtitle: Symbolic differentiation, integration, expansion and root-finding as a .NET library — and a typed rule language that compiles new algebra into it.
description: MLambda.Genesis.Algebra and MLambda.Lang.CAS — a symbolic algebra library over a seven-constructor expression type, and a Hindley–Milner-typed rewrite-rule language that Roslyn compiles into it. What it does, how it is built, and its stated limits.
permalink: /articles/a-cas-for-engineers/
image: /images/articles/ns-09-cas.png
---

<figure class="story-figure">
  <img src="{{ '/images/articles/ns-09-cas.png' | relative_url }}" alt="A CAS for engineers — an expression ADT, pure algebra functions, and rewrite rules compiled to C#." width="1200" height="627">
</figure>

<p>Engineers reach for a computer algebra system for one reason: the formula is the
specification, and the numbers are what you get after. A control law, a load model, a
consistency invariant — you want to differentiate it, simplify it, solve it, and only then
evaluate it. Most of the time that means leaving your stack for Mathematica, Maple or SymPy,
and carrying the result back by hand.</p>

<p>MLambda.Genesis.Algebra brings the algebra into .NET, as a library you can call from the same
code that uses the result. And the CAS rule language lets you extend it in a notation that is
closer to the mathematics than to C#.</p>

<h2>Seven constructors</h2>

<p>Everything stands on one algebraic data type, <code>Expr</code>, with seven constructors:
<code>Num</code>, <code>Sym</code>, <code>Add</code>, <code>Mul</code>, <code>Pow</code>,
<code>Neg</code> and <code>FuncCall</code>. That is deliberately minimal, in the tradition of
Davenport, Siret and Tournier. Subtraction is not primitive — <code>a − b</code> is
<code>Add(a, Neg(b))</code> — and division is <code>Mul(a, Pow(b, −1))</code>, so the single
rule <code>x^a · x^b = x^(a+b)</code> handles division without a special case. Fewer
constructors means every transformation downstream has fewer cases to get right.</p>

<p>Around the type: a lexer, a recursive-descent parser, a pretty-printer and a numeric
evaluator, so you can go from text to tree and back.</p>

<h2>What the library does</h2>

<p>Each algorithm is a pure function from <code>Expr</code> to <code>Expr</code>. Nothing is
mutated; nothing is shared between calls.</p>

<ul>
  <li><strong>Simplify</strong> — canonical forms, constant folding, power combination.</li>
  <li><strong>Differentiate</strong> — <code>D(expr, x)</code>, with the chain rule driven by a
  function registry that knows the derivatives and antiderivatives of the built-ins
  (<code>sin</code>, <code>cos</code>, <code>exp</code>, <code>ln</code>, <code>sqrt</code>) and
  accepts user-registered functions.</li>
  <li><strong>Integrate</strong> — symbolic antiderivatives, with polynomial factorisation used
  for partial fractions.</li>
  <li><strong>Expand</strong> — distribute products over sums.</li>
  <li><strong>Solve</strong> — real roots of a polynomial equation: coefficient extraction,
  then dispatch on degree — linear, quadratic in closed form, higher degrees by factoring.</li>
  <li><strong>Polynomial arithmetic</strong> — GCD by the Euclidean algorithm and factorisation
  over the rationals, after Knuth and after Geddes, Czapor and Labahn.</li>
  <li><strong>Taylor series</strong> to a given order about a point, and an <strong>AC
  matcher</strong> that matches modulo associativity and commutativity, so <code>a + b</code>
  and <code>b + a</code> are the same pattern.</li>
</ul>

<pre><code>var expr  = MathParser.Parse("x^2 + 2*x + 1");
var deriv = Differentiator.D(expr, new Sym("x"));   // 2 * x + 2
var roots = Solver.Solve(expr, new Sym("x"));       // [-1]</code></pre>

<h2>Open by construction</h2>

<p>The algebra does not own its rules. The extension point is one interface:</p>

<pre><code>public interface IRewriteSystem
{
    IEnumerable&lt;RewriteRule&gt; Rules { get; }
}
public sealed record RewriteRule(string Name, Func&lt;Expr, Expr&gt; Apply);</code></pre>

<p>Anything that yields <code>Expr → Expr</code> transformations — hand-written or generated —
contributes rules, and a host composes systems by concatenating them and applying a strategy:
innermost-first, outermost-first, or in parallel. That is what makes the next part possible.</p>

<h2>A language for the rules</h2>

<p>Writing rewrite rules as C# lambdas over a tree works, but it does not look like the
mathematics, and the type of "an expression that matches <code>Pow(f, Num(n))</code>" is not
something C# will check for you. So Genesis has a second language, CAS, for exactly this:</p>

<pre><code>module Calculus {
    let isConst (e : Expr) : Bool =
        match e with
        | Num(_) -> true
        | _      -> false

    rule D : Expr -> Expr {
        | Num(_)            -> Num(0)
        | Sym("x")          -> Num(1)
        | Sym(_)            -> Num(0)
        | Add(f, g)         -> Add(D(f), D(g))
        | Mul(f, g)         -> Add(Mul(D(f), g), Mul(f, D(g)))
        | Pow(f, Num(n))    -> Mul(Mul(Num(n), Pow(f, Num(n-1))), D(f))
        | _                 -> Num(0)
    }
}</code></pre>

<p>A module holds helpers — pure functions used in guards — and rules: pattern arms with optional
<code>when</code> guards, constructor deconstruction, wildcards, literals and bindings, plus a
small functional calculus for the right-hand sides (lambdas, <code>let</code>,
<code>if</code>, <code>match</code>). The type system is a simplified Hindley–Milner —
Damas and Milner's Algorithm W — extended with the distinguished type <code>Expr</code> and
type variables, so an arm that returns the wrong kind of thing is a type error in the rule
file, not a runtime surprise in the algebra.</p>

<p>The pipeline is the same shape as every Genesis language: lexer, parser, type checker,
emitter, pretty-printer — and then Roslyn, which compiles the emitted C# to an assembly
implementing <code>IRewriteSystem</code>. The rules become code without anyone writing the
code. Load the assembly, concatenate its rules with the built-ins, choose a strategy, and the
algebra now knows your domain's identities.</p>

<h2>Why this is in an architecture platform</h2>

<p>Because Turing's method has a mathematical stage. Gilb's Planguage gives every quality
requirement a scale, a meter and a target — quantities, not adjectives — and the method book's
chapter on "the mathematical definition" is where those quantities become expressions the
platform can reason about: derived, simplified, compared against measurement. An architecture
platform that treats software as mathematics needs algebra it can run, and it needs it in the
language the rest of the platform is written in.</p>

<h2>Stated limits</h2>

<p>The polynomial machinery works over <code>double</code> coefficients with a
<code>10⁻¹⁵</code> threshold — floating point, not exact rationals — and the solver returns real
roots. The CAS type checker's unifier does not yet perform the occurs check. These are the
honest edges of a v0.x library that is used in earnest but is not claiming to replace Maple.
What it claims is narrower and true: symbolic differentiation, integration, expansion,
root-finding and user-defined rewrite systems, as pure functions, in a NuGet package, with a
typed rule language that compiles into it.</p>

<hr>

<p class="muted"><code>dotnet add package MLambda.Genesis.Algebra</code> — MIT, part of
<a href="{{ '/products/genesis/' | relative_url }}">Genesis</a>. Documentation for the algebra,
the math expression language and the CAS rule language at
<a href="https://genesis.mlambda.net">genesis.mlambda.net</a>.</p>
