---
title: MLambda.OS
tagline: A Minix 3-inspired microkernel for x86-64, specified before it is implemented.
tier: commercial
status: research microkernel
docs: https://mlambda-net.github.io/MLambda.OS
packages: []
tech: [Rust, C, x86-64, Assembly, Microkernel]
weight: 7
---

## What it is

A research microkernel written to own the whole stack down to the hardware: the layer the
runtime, the database and the language ultimately stand on.

## What is built

Specifications and implementation, subsystem by subsystem: CPU feature detection, the GDT
and IDT, paging, protection rings and the syscall boundary; then processes, IPC, memory
management, a filesystem and I/O. Every subsystem is specified first, and the specification
is the authority the implementation is checked against.

## How to get it

The specifications are public. Source is available through
[early access](/services/#early-access).
