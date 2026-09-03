---
slug: aleph
title: Aleph
tagline: A functional language that reaches the machine directly — C, assembly, LLVM and WebAssembly through a native FFI.
tier: commercial
status: v1.2.0
docs: https://genesis.mlambda.net/#/languages/aleph
packages: []
tech: [Compiler design, Type systems, FFI, LLVM, WebAssembly, POSIX]
weight: 3
---

## What it is

A programming language designed and implemented at MLambda: grammar, type checker, code
generation and a standard library. Programs compile to native code and can call C,
assembly, LLVM IR and WebAssembly through `import "c"`, `import "asm"`, `import "llvm"` and
`import "wasm"`, so a program can reach a POSIX system call with no runtime in the way.

## What is built

The compiler, and an SDK covering error and recovery policy, resource disposal with full
propagation, a JSON algebraic data type with per-type codecs, equality dictionaries, a
filesystem module that discriminates real error cases through `access(2)`, and a test
framework with TAP output and property testing. Sixty-one tests across eight suites. A
literate rendering of *Category Theory for Programmers* is being written in Aleph as its
first large program.

## How to get it

The syntax reference is public on the Genesis documentation site. The compiler and SDK are
available through [early access](/services/#early-access).
