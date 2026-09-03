---
title: MLambda.UI
tagline: A reactive MVVM framework that never calls a render method — one view, painted by ImGui, Blazor or Avalonia.
tier: commercial
status: in development
docs: https://mvvm.mlambda.net
packages: []
tech: [C#, Rx.NET, ImGui, Blazor WebAssembly, Avalonia, Material 3]
weight: 6
---

## What it is

A backend-agnostic UI framework for C#. Components describe an atom tree; rendering engines
walk it and paint. The same view code runs on the desktop through ImGui, in the browser
through Blazor WebAssembly, and natively through Avalonia, unchanged.

## What is built

Reactive state on `Observable<T>` and `Computed<T>`; an enforced Control → ViewModel → View
→ Design separation; **Morphe**, an algebraic styling system — Geometry × Color × Font — so
styles compose like expressions rather than cascading; a component catalogue mapped to the
Material 3 specification; three rendering backends. Pencil, the screen editor inside Turing,
is built on it.

## How to get it

Concepts, the Morphe algebra and the component reference are public at mvvm.mlambda.net.
The framework is available through [early access](/services/#early-access).
