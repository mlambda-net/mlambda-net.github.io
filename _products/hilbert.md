---
slug: hilbert
title: Hilbert
tagline: A neuro-symbolic transformer that reasons across five systems of logic and learns from each input without retraining.
tier: research
status: research, not yet released
docs: null
packages: []
tech: [Python, PyTorch, Transformers, Graph attention, Fast weights, Meta-learning, Modal logic, Temporal logic]
weight: 8
---

## What it is

Research into neural architectures that carry logic inside them rather than bolting a
reasoner onto the side. The founding observation: a transformer's attention layer is
mathematically an adaptive filter with feedback — which means it can be made to learn from
each input as it arrives.

## What is built

Five levels, each with a different logic: first-order; relational with graph attention;
modal with a multi-world attention matrix; temporal with LTL and dual causal/bidirectional
attention; sortal with ontology-biased attention. Fast weights and episodic memory connect
them; a strange loop after Hofstadter feeds the top level's error signal back down to
refine the lower four at inference time; a genetic layer evolves populations of fast-weight
configurations against gradient descent. The same commitments drive Thinker, the reasoning
layer inside Turing.

## How to get it

There is no public release. Hilbert is active research; results will be published when
they are ready.
