---
slug: hilbert
title: Hilbert
tagline: A mathematics language — formulas written as on paper, compiled to C# for reals and to ONNX graphs for tensors.
tier: commercial
status: in development; documentation public
docs: https://www.mlambda.net/MLambda.Hilbert/
packages: []
tech: [Language design, Computer algebra, Tensors, Einstein summation, ONNX, C#, Proof checking]
weight: 8
---

## What it is

A language for people who do mathematics, not programming. A definition is written the way it
appears on paper — `def radians(d) ≔ d · π / 180` — and a doorway, `fn convert(a) ↦ radians(a)`, is
what a program calls. The compiler turns each doorway into C#: plain arithmetic over reals, and an
ONNX graph over vectors, matrices and tensors, run on the calling thread when the input is small and on
ONNX Runtime when it is large. One line of Hilbert becomes an overload for every kind of value its
operations accept.

The compiler knows no identities and no derivatives. `sin² + cos² = 1` and the chain rule are laws a
library states and a reader can open, and a theorem is checked by rewriting at build time. Its one
contraction is `einsum` — Einstein's summation convention, the notation he introduced in 1916 to write
general relativity — and every other operation is defined in Hilbert on top of it.

## What is built

The compiler and runtime, integrated with MSBuild so `.hb` files sit beside C# in an ordinary project.
The Prelude — 42 modules and nearly 1,400 definitions written in Hilbert itself — covers linear
algebra (inverse, Cholesky, QR, eigenproblems, SVD, conjugate gradient), descriptive statistics,
distributions, inference and resampling, regression, trees, neural networks, clustering, sequence
models, Markov chains, point processes, diffusions, queues and volatility, and reinforcement learning.
Declarations for trainable models, seeded stochastic processes and typed data frames compile to C#
classes, and companion dialects state logical theories (`.hs`) and machine-checked proofs (`.hp`).

## How to get it

The documentation is public: the language guide, what a tensor is, the story of Einstein's summation,
and a reference for every Prelude definition with examples that were compiled and run. Source is
available through [early access](/services/#early-access).
