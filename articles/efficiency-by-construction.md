---
layout: page
eyebrow: Article · MLambda.Actors and MLambda.Data
title: Efficiency by construction
subtitle: Where the speed in an actor-native stack actually comes from — and which of those gains are structural rather than tuned.
description: How MLambda.Actors and MLambda.Data get their performance from architecture rather than optimisation — reactive responses, ephemeral actors, topology transparency, gossip membership, zero-parse and zero-copy data paths, and an LSM engine whose costs are stated plainly.
permalink: /articles/efficiency-by-construction/
image: /images/articles/ns-07-efficiency.png
---

<figure class="story-figure">
  <img src="{{ '/images/articles/ns-07-efficiency.png' | relative_url }}" alt="Efficiency by construction — the structural gains of an actor-native runtime and database." width="1200" height="627">
</figure>

<p>There are two kinds of performance. The kind you tune — a cache here, a buffer there, a
hot loop rewritten — and the kind you get by construction, because the architecture has no
place for the cost to occur. The first kind erodes as the system changes. The second kind is
permanent. This article is about the second kind, in two systems: MLambda.Actors, the
runtime, and MLambda.Data, the database built on it.</p>

<h2>The runtime: what an actor doesn't have to do</h2>

<p><strong>No lock is ever taken on behalf of your state.</strong> An actor owns its state and
handles one message at a time, so there is no contention on it, no deadlock possible over it,
no cache line bouncing between cores because two threads want the same field. Concurrency is
the number of actors, not the number of threads let into one.</p>

<p><strong>Every response is an <code>IObservable&lt;T&gt;</code>, not a
<code>Task&lt;T&gt;</code>.</strong> This is not stylistic. Retry with exponential backoff,
timeouts with a cached fallback, fan-out to several actors with merged results, backpressure
when a downstream is overwhelmed — with tasks each of these is bespoke plumbing that buries the
business logic. With Rx they are operators. The runtime composes them; you don't write them,
and the code that isn't written is code that isn't slow.</p>

<p><strong>Ephemeral actors remove the mailbox funnel.</strong> A standard actor processes
sequentially, so under a hundred simultaneous requests the hundredth waits for ninety-nine —
tail latency grows linearly with concurrency. MLambda's <code>[Ephemeral]</code> attribute
tells the framework to process a request-handling actor's messages concurrently, each in its
own short-lived instance, without giving up the actor model's guarantees for the actors that
hold state. One attribute, declared where the concurrency belongs, instead of manually spawned
children in every handler.</p>

<p><strong>Topology transparency costs nothing at runtime and everything at design time.</strong>
An actor obtains a reference with one call — <code>ctx.Ref&lt;OrderActor&gt;()</code> — whether
the target is in the same process, on the same node, or across a cluster. Standalone, hybrid
and clustered are configuration, not code paths. The performance consequence is that a local
message is a reference handed over, with no serialisation, and the code cannot accidentally do
worse.</p>

<p><strong>Membership is gossip, not a coordinator.</strong> No ZooKeeper, no etcd, no leader
to elect and no quorum to lose. A three-phase exchange — SYN, ACK, ACK2, after Scuttlebutt —
runs every second with random peers, and information reaches every node in O(log N) rounds.
Route tables are CRDTs, so partitions heal by merging rather than by arbitration. Each node
talks to a small random subset per round regardless of cluster size, which is what "scales
linearly" means when it is true.</p>

<p>A BenchmarkDotNet suite ships in the repository — actor creation, mailbox throughput,
message throughput. We do not publish numbers from it here, because a number without the
machine, the message size and the topology beside it is marketing, not measurement. The
structural claims above are what a number would be measuring.</p>

<h2>The database: costs that never enter the path</h2>

<p>MLambda.Data inherits everything above and adds three structural advantages its performance
documentation spells out.</p>

<p><strong>Zero parsing.</strong> A traditional database parses, binds, plans and then
executes every request — even prepared statements pay a wire protocol. MLambda.Data's requests
are typed messages dispatched to actors: there is no query text to parse and no plan to build
for a point read or a point write. The documentation puts the per-request overhead it
eliminates at roughly 50–200 microseconds of parsing and planning — a fixed cost that
dominates exactly the small, high-frequency operations a transactional system lives on.</p>

<p><strong>Zero-copy locally.</strong> When sender and receiver are on the same node, the
message is passed by reference: no serialisation, no buffer, no copy. A conventional
client-server round trip serialises and deserialises twice each way — four hops. A local actor
call is zero; a remote one is two.</p>

<p><strong>Lock-free, as above.</strong> The write path, the read path, every index, compaction
and the filesystem are actors. There is no mutex in the data path to contend on.</p>

<h2>What the engine costs, stated plainly</h2>

<p>The storage engine is log-structured, and its documentation states its latency budget rather
than hiding it. A write appends to a write-ahead log with CRC32 integrity, inserts into a sorted
in-memory memtable (a skip list, under a microsecond), and updates the indexes (under a
microsecond each). The fsync on the log dominates: 0.1–1 ms on SSD, 5–10 ms on spinning disk —
which is why the documentation says, without hedging, that production wants SSDs.</p>

<p>A read checks a Bloom filter, then the memtable, then the SSTable index — all in memory,
under a microsecond each — and touches disk only on a cache miss. A cache-hit read is under
five microseconds end to end. The Bloom filter's memory-for-accuracy trade is tabulated: ten
bits per entry gives roughly a 0.8% false-positive rate at 1.25 MB per million keys, and you
can move it either way.</p>

<p>Compaction — the maintenance an LSM engine cannot avoid — runs in the background under a
throttle (a configurable MB/s ceiling and a cap on concurrent tasks) and a circuit breaker, so
maintenance cannot starve foreground reads and writes. Write amplification is documented per
strategy — size-tiered for write-heavy, levelled for read-heavy — with the trade-offs in both
directions.</p>

<h2>The numbers, and what they are</h2>

<p>The performance page states expected single-node figures — on the order of 50–100 thousand
point writes per second at 1 KB rows with quorum consistency on SSD; 200–500 thousand cached
point reads per second; a million-plus Bloom checks — and a scaling table in which throughput
grows roughly linearly with nodes for partitioned workloads, tapering toward 8–10× at ten nodes
as quorum coordination and O(N log N) gossip traffic take their share. These are <strong>design targets and analysis</strong>, published so that they can be held against measurement, not
benchmarks we are asking you to take on trust. The point of stating them is the same as the
point of the TLA+ specification beside them: a claim you can check is worth more than a claim
you can only admire.</p>

<hr>

<p class="muted"><a href="{{ '/products/actors/' | relative_url }}">MLambda.Actors</a> is MIT on NuGet;
<a href="{{ '/products/data/' | relative_url }}">MLambda.Data</a> is in development with its
architecture, consistency model and performance analysis public at
<a href="https://data.mlambda.net">data.mlambda.net</a>.</p>
