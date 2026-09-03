---
layout: page
eyebrow: Article · Aleph
title: Nowhere to occur
subtitle: What a pure language does to a bug — and why MLambda built one that still reaches the machine.
description: Aleph is a pure, lazy, immutable-by-default language with Hindley–Milner types, exhaustive matching, STM and a native FFI to C, LLVM and WebAssembly. This is what that combination removes, and what it honestly does not.
permalink: /articles/nowhere-to-occur/
image: /images/articles/ns-06-aleph.png
---

<figure class="story-figure">
  <img src="{{ '/images/articles/ns-06-aleph.png' | relative_url }}" alt="Nowhere to occur — the defects a pure language cannot express, and the machine it still reaches." width="1200" height="627">
</figure>

<p>There are two ways to deal with a class of bugs. You can find them — tests, reviews,
sanitisers, production incidents — or you can make them inexpressible. The first is a cost you
pay forever. The second is a design decision you make once. Aleph is a language built around
the second kind of decision, and this article is about what it removes and, just as
importantly, what it does not.</p>

<h2>What cannot be written</h2>

<p><strong>Shared mutation.</strong> Aleph is pure and immutable by default. A value, once
constructed, is what it is; a function returns a new one. That single property removes the
entire family of data races — two threads writing the same location, a reader seeing a
half-updated structure — because there is no location being updated. Coordination, when you
need it, is software-transactional memory (<code>atomically</code>, <code>retry</code>,
<code>orElse</code>) and channels, not locks.</p>

<p><strong>Null.</strong> There is no null. Absence is a constructor of an algebraic data type,
and the type system will not let you use a value without saying what happens when it is
absent.</p>

<p><strong>The unhandled case.</strong> Pattern matching is exhaustive. Add a constructor to a
type and every match that forgot it is a compile error, not a runtime surprise six months
later.</p>

<p><strong>The unchecked failure.</strong> The SDK has no exceptions. Errors are typed values
with a recovery policy attached; a function that can fail says so in its type, and the caller
must decide. <code>Disposable</code> resources propagate their disposal through the whole
computation, so a leaked handle is not something you forget — it is something you cannot
express.</p>

<p><strong>The implicit effect.</strong> Effects are sequenced explicitly. <code>let _ = …</code>
never runs — the linter tells you — because Aleph is lazy, and an effect you did not thread is
an effect that did not happen. This is unfamiliar for a week and then you cannot go back: every
side effect in a program is visible in its structure.</p>

<p>Under all of this is Hindley–Milner type inference with algebraic data types and traits for
ad-hoc polymorphism. You write almost no type annotations, and the compiler knows almost
everything.</p>

<h2>What it still reaches</h2>

<p>The usual price of purity is distance from the machine. Aleph refuses to pay it. Programs
compile to LLVM IR and then to native executables, or run through an in-process JIT and a
REPL. And the foreign-function interface is native: <code>import "c"</code>,
<code>import "asm"</code>, <code>import "llvm"</code>, <code>import "wasm"</code>. The SDK's
filesystem module discriminates real error cases by calling POSIX <code>access(2)</code>
directly — no runtime standing between the program and the system call. There is SIMD, with
vector types and lane operations. Foreign imports are module-private, and the discipline is
simple: wrap them in pure functions at the boundary, so the unsafety has an address.</p>

<h2>What it does not remove — said plainly</h2>

<p>I would rather you trust the previous sections, so here is the honest remainder. Aleph does
not currently have a tracing garbage collector; a real allocator and GC are on the roadmap, and
until they land, memory management is not something the language guarantees the way Rust's
borrow checker does. Top-level let-polymorphism is still being added, so the SDK carries
per-type wrappers in a few places. Sixty-one tests across eight suites is a real test suite for
a v1.2 SDK and not a large one. The claim is precise: <em>whole classes of defects cannot be
expressed</em>. It is not "bug-free", and it never will be — Gödel saw to that.</p>

<h2>Why a company built a language</h2>

<p>Because the point of MLambda is software that is verified before it is built, and
verification is worthless if the thing you generate afterwards can quietly become wrong. Turing
proves a specification; Bet builds from it; the generated system then has to <em>stay</em>
correct in the hands of people who will modify it. A language in which the common corruptions
are inexpressible is how you keep the guarantee after the generator has left the room. Genesis
is the workbench Aleph's compiler is built in; MLambda's rendering of <em>Category Theory for
Programmers</em> is being written in Aleph as its first large program, each chapter's laws
checked by property tests. The language is used the way it is meant: as mathematics you can
run.</p>

<hr>

<p class="muted"><a href="{{ '/products/aleph/' | relative_url }}">Aleph</a> v1.2.0. The syntax
reference is public on <a href="https://genesis.mlambda.net/#/languages/aleph">genesis.mlambda.net</a>;
the compiler and SDK through <a href="{{ '/services/#early-access' | relative_url }}">early access</a>.</p>
