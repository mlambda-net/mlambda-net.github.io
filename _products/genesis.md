---
slug: genesis
title: Genesis
tagline: A compiler workbench for building languages — and for verifying what they describe before it exists.
tier: open
status: published on NuGet
docs: https://genesis.mlambda.net
packages:
  - name: MLambda.Genesis.Parser
    url: https://www.nuget.org/packages/MLambda.Genesis.Parser
  - name: MLambda.Genesis.Algebra
    url: https://www.nuget.org/packages/MLambda.Genesis.Algebra
  - name: All Genesis packages
    url: https://www.nuget.org/packages?q=MLambda.Genesis
tech: [C#, .NET 10, Parser combinators, EBNF, ASDL, TLA+, Symbolic algebra]
weight: 2
---

## What it is

A .NET meta-language workbench. Grammars become executable parsers; schemas become typed
syntax trees; specifications become model-checked properties. It is the foundation the
Aleph compiler, Turing and MLambda's own domain languages are built on.

## What is built

Eleven packages, MIT-licensed: a monadic parser-combinator library with full LINQ support;
an EBNF grammar compiler that emits executable combinators; an ASDL schema parser that
generates C# syntax-tree types; a generator tool (`mlambda-gen`) that turns EBNF plus ASDL
into a language front-end; Shin, a stratified forward-chaining rule language and runtime; a
TLA+ checker and prover with LTL evaluation; a mathematical expression language; a symbolic
algebra system that differentiates, integrates, expands and solves; a CAS rule DSL; and a
SQL front-end with analyser and code generator. Front-ends exist for C#, CSS, JavaScript,
HTML, Guimel, SQL, LLVM IR and Aleph.

## How to get it

```
dotnet add package MLambda.Genesis.Parser
dotnet add package MLambda.Genesis.Algebra
```

Documentation, architecture and the twelve-chapter method book are at genesis.mlambda.net.
