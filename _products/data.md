---
title: MLambda.Data
tagline: A distributed database in which every component is an actor — and the consistency model is a checked TLA+ specification.
tier: commercial
status: in development
docs: https://data.mlambda.net
packages: []
tech: [C#, .NET 10, LSM storage, B-tree, Bloom filters, Consistent hashing, CRDT, TLA+]
weight: 5
---

## What it is

An actor-native distributed database on the MLambda.Actors runtime. Storage, indexes,
filesystem, query planning and authorisation are all actors; there is no shared mutable
state and there are no mutexes in the data path. Correctness comes from message ordering,
not from locks.

## What is built

A log-structured storage engine — write-ahead log with CRC32 integrity, sorted in-memory
memtable, immutable SSTables, throttled background compaction. Indexes for sorted range
queries, constant-time point lookups, probabilistic existence checks and full-text search.
A schema registry with versioning. A cluster layer that places data on a consistent hash
ring and replicates metadata through CRDT gossip. Three deployment topologies — standalone,
hybrid, cluster — selected by configuration. The consistency model is specified in TLA+ and
model-checked; a research whitepaper accompanies the documentation.

## How to get it

Architecture, consistency model, formal specification and whitepaper are public at
data.mlambda.net. Builds are available through [early access](/services/#early-access);
production use under [commercial licence](/services/#commercial-licence-and-support).
