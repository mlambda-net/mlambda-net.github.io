---
layout: page
eyebrow: Article · MLambda.Data
title: No locks
subtitle: What happens when you build a distributed database entirely out of actors — and specify its consistency model before you trust it.
description: MLambda.Data has no mutexes in its data path. Every component is an actor, correctness comes from message ordering, and the consistency model is a TLA+ specification that has been checked, not described.
permalink: /articles/no-locks/
image: /images/articles/ns-05-no-locks.png
---

<figure class="story-figure">
  <img src="{{ '/images/articles/ns-05-no-locks.png' | relative_url }}" alt="No locks — every component an actor; correctness from message ordering; consistency checked in TLA+." width="1200" height="627">
</figure>

<p>Every database you have used protects its internals with locks. Latches on pages, mutexes
around the write-ahead log, reader-writer locks on the index. Locks are how shared mutable
state stays sane under concurrency, and the history of database engineering is, in large part,
the history of making them cheaper and holding them for less time.</p>

<p>MLambda.Data has none. Not fewer — none, in the data path. It is not a stunt; it is what
falls out when you take the actor model seriously enough to build a storage engine from it.</p>

<h2>Actors all the way down</h2>

<p>An actor owns its state and talks to the world only through messages, handled one at a time.
That single rule dissolves the problem locks exist to solve: if there is no shared mutable
state, there is nothing to guard. So in MLambda.Data, everything that would normally be a
protected data structure is an actor with a mailbox.</p>

<p>The write path is a <code>WriteActor</code> that appends to a write-ahead log (CRC32 on every
record), updates a sorted in-memory memtable, and notifies the index actors. The read path is a
<code>ReadActor</code> that consults a Bloom filter, then the memtable, then the immutable
SSTables on disk. Compaction is a <code>CompactionActor</code> that merges SSTables in the
background under a throttle, so it cannot starve foreground work. Indexes are actors too — a
B-tree for range queries, a hash index for point lookups, an inverted index for full-text
search — each updated by message, each answering by message. Beneath them, a distributed
filesystem: a <code>NamespaceActor</code> for the registry, <code>FileActor</code>s for blocks,
<code>BlockActor</code>s for physical I/O.</p>

<p>Ordering, not exclusion, is what keeps this correct. A message is processed after the one
before it and before the one after; the actor's state at any moment is a function of the
messages it has handled. Concurrency comes from having many actors, not from letting many
threads into one.</p>

<h2>Supervision instead of hope</h2>

<p>The other thing you get from actors is a story for failure. Every storage actor has a
guardian — <code>EngineGuardian</code>, <code>StorageGuardian</code>, <code>IndexGuardian</code>,
<code>FilesystemGuardian</code> — and a guardian's job is to decide what happens when a child
crashes: restart it, restart its siblings, or escalate. A corrupted SSTable reader does not
take down the engine; it is restarted by its supervisor, and the write-ahead log is the source
of truth it recovers from. The failure modes are designed, not discovered.</p>

<h2>The cluster is the same idea, larger</h2>

<p>Across machines, a <code>RingManager</code> places data on a consistent hash ring, a
<code>ClusterAdapter</code> discovers members, and cluster metadata is replicated through
gossip using CRDTs — data types that merge without coordination, so nodes converge without a
leader deciding for them. The same actors run in three topologies — standalone, hybrid,
cluster — chosen by configuration alone; the code does not change.</p>

<h2>Consistency you can check, not read about</h2>

<p>Here is the part I care about most. Every database publishes a consistency model. Almost
none publish a proof. MLambda.Data's consistency model is written as a <strong>TLA+
specification</strong> and run through the TLC model checker, which enumerates every reachable
state of the protocol looking for one that violates an invariant. When a document says "reads
see all acknowledged writes", that sentence corresponds to a temporal property that either
holds over the state space or produces a counterexample. It is not prose. It is a checked
claim.</p>

<p>That is the same discipline the rest of the MLambda stack is built on: specify, check, then
build. It is why MLambda.Data can be the data layer for systems that Turing generates — the
generator can trust it for the same reason you can.</p>

<hr>

<p class="muted"><a href="{{ '/products/data/' | relative_url }}">MLambda.Data</a> is in
development. Architecture, the consistency model, the formal specification and a research
whitepaper are public at <a href="https://data.mlambda.net">data.mlambda.net</a>. Builds through
<a href="{{ '/services/#early-access' | relative_url }}">early access</a>.</p>
