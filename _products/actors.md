---
title: MLambda.Actors
tagline: A reactive actor runtime for .NET with supervision, clustering, gossip membership and mTLS.
tier: open
status: v2.2 on NuGet
docs: https://actors.mlambda.net
packages:
  - name: MLambda.Actors
    url: https://www.nuget.org/packages/MLambda.Actors
tech: [C#, .NET, System.Reactive, gRPC, Kubernetes, Helm, mTLS]
weight: 4
---

## What it is

An actor-model framework for .NET, MIT-licensed. Concurrency is made tractable by removing
shared state instead of guarding it: every actor owns its state, every interaction is a
message, and every response is an `IObservable<T>`.

## What is built

A root/system/user/temp guardian hierarchy with parent–child supervision; one-for-one and
all-for-one strategies; runtime behaviour switching with become and unbecome; message
stashing and replay; death-watch; lifecycle hooks; dependency-injection registration. Beyond
one process it clusters — gossip-based membership, mTLS between nodes, gRPC transport — and
the same actor code runs standalone, hybrid or clustered on configuration alone. Helm charts
are published for Kubernetes deployment.

## How to get it

```
dotnet add package MLambda.Actors
```

Documentation and the quick start are at actors.mlambda.net. Supported use is available under
[commercial licence and support](/services/#commercial-licence-and-support).
