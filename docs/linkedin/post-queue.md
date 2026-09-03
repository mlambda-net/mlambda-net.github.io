# LinkedIn post queue — one per day, mornings

Audience: Anyone. Paste as-is; each is under 1,300 characters. Days are relative to the day
after the article post ("The LLM never answers") went out. Links are live.

---

## Day 1 — Refusal is a result (Turing walk-through)

Watch a system refuse to be built wrong.

I put the smallest system I could think of — a to-do list — through Turing, our architecture platform, and counted the refusals.

The backlog said "not sound yet" and would not let design run. The requirement would not leave the blank-title case unspecified — the guard and the refusal are part of the requirement, not an edge case for later. The domain model would not invent a payload it wasn't told about: "shape not stated — name its fields in the requirement." The screen editor declined to act on an observation that changed nothing. And the generated actor carries a comment that is the whole philosophy: convention-synthesized — no computation the specification did not imply.

Four gates in front of every line of code. Each one can say no. That's what "verified before it is built" means in practice.

Six screenshots, one small system: https://www.mlambda.net/articles/refusal-is-a-result/

#SoftwareArchitecture #FormalMethods #DDD #AI #OpenToWork

---

## Day 2 — 18 years, one lesson

Eighteen years as an architect taught me one thing I couldn't unlearn.

A trading platform where a lost message is a lost order. DHL's logistics core, where an integration that drifts from its contract costs real trucks real hours. Enterprise products where the architecture diagram was right and the code quietly stopped matching it.

The lesson: nothing connects an architecture to its software except people and time. Both run out.

So I spent six years building the thing that connects them — a runtime, a compiler workbench, a language, a database, and now Turing, where the model is not documentation about the software; it's what the software is generated and verified from.

I'm open to architect / principal roles (remote), and to talking with teams and investors who need software they can trust. https://www.mlambda.net

#SoftwareArchitecture #DistributedSystems #DDD #OpenToWork

---

## Day 3 — No locks

MLambda.Data has no mutexes in its data path. Not fewer. None.

Every component is an actor: the write path, the read path, every index, compaction, the filesystem underneath. An actor owns its state and handles one message at a time, so there's no shared mutable state to guard — correctness comes from message ordering, not exclusion. Failure has a design, not a hope: guardians decide whether a crashed actor restarts, takes its siblings with it, or escalates.

And the consistency model isn't a paragraph in the docs. It's a TLA+ specification that has been run through a model checker. "Reads see all acknowledged writes" is a temporal property that either holds over the state space or produces a counterexample.

Why build a database this way: https://www.mlambda.net/articles/no-locks/

#Databases #DistributedSystems #ActorModel #FormalMethods #DotNet

---

## Day 4 — Nowhere to occur (Aleph)

There are two ways to deal with a class of bugs: find them forever, or make them inexpressible once.

Aleph, the language we built at MLambda, takes the second path. Pure and immutable by default, so there is no shared mutation to race on. No null — absence is a constructor. Exhaustive pattern matching — add a case and every match that forgot it fails to compile. Typed errors with recovery policies instead of exceptions. Explicit effects.

And it still reaches the machine: LLVM to native, a JIT and a REPL, and a native FFI — import "c", "asm", "llvm", "wasm" — with POSIX one call away.

What it removes, and honestly what it doesn't yet: https://www.mlambda.net/articles/nowhere-to-occur/

#ProgrammingLanguages #Compilers #FunctionalProgramming #LLVM

---

## Day 5 — Why I built an actor runtime for .NET

In 2019 I couldn't find a team that thought about concurrency the way physicists think about state, so I built the runtime I wanted and released it.

MLambda.Actors: a guardian hierarchy with supervision strategies, become/unbecome, message stashing, death-watch, every response an IObservable<T>. Beyond one process it clusters — gossip membership, mTLS between nodes, gRPC transport — and the same code runs standalone, hybrid or clustered on configuration alone.

It's MIT, on NuGet at v2.2, with docs at actors.mlambda.net. It's also the runtime everything else at MLambda stands on, including what Turing generates.

dotnet add package MLambda.Actors — https://www.mlambda.net/products/actors/

#DotNet #ActorModel #DistributedSystems #OpenSource

---

## Day 6 — The mission

For years I applied TOGAF by hand and watched the same thing happen: the architecture was right, and the software still drifted from it.

The mission became one sentence: build a system that understands architecture the way TOGAF describes it, expresses each domain as a domain-specific language, and runs it on an actor framework built for reactive domain-driven design.

That system is Turing. Rational tools: DSLs that call on language models to gather and validate requirements, then hand them to symbolic AI — an inference engine, a proof kernel, a model checker — to derive the logic, the views, the tests and the verification.

This is the application I dreamed of building for many years. I'm building it now — and I'd like to build it with people who need it. https://www.mlambda.net

#EnterpriseArchitecture #TOGAF #DDD #AI #Founders

---

## Day 7 — Hilbert

Can the logic live inside the network instead of bolted onto the side?

That's the research question behind Hilbert. It starts from an observation: an attention layer is, mathematically, an adaptive filter with feedback — tokens are the signal, Q/K/V are the weights, the gradient is the error. Adaptive filters learn from each sample. Transformers, as trained, don't. Hilbert makes them.

Five levels, five logics — first-order, relational, modal, temporal, sortal — connected by fast weights, with a strange loop that feeds the top level's error back down at inference time.

It's research. It may fail. But it's the same rule pursued one level deeper: the language model gathers, the proofs decide. https://www.mlambda.net/articles/the-llm-never-answers/

#NeuroSymbolicAI #MachineLearning #AI #Research

---

## Day 8 — What a demo looks like

Here's what happens when you ask me for a Turing demonstration.

You send two or three sentences about a system and the invariant that worries you most. We take it through the workbench live: backlog with quantified objectives, requirements with their ubiquitous language and refusals, the derived use cases, the domain model, the screens, the generated source on the actor runtime. The refusals are the interesting part — you'll see exactly what the model won't accept and why.

Then you get a written note on what an engagement on your system would involve. No slides.

Fintech, logistics, regulated software, or a team adopting AI code generation and wondering what it produces — write to roy.gonzalez@mlambda.net. https://www.mlambda.net/services/

#SoftwareArchitecture #AI #FormalMethods #Fintech #Logistics

---

## Day 9 — For hiring managers

If you're hiring an architect, here is what I bring, without the adjectives.

Eighteen years on systems that had to stay correct under load — a US trading platform, DHL's logistics core, enterprise products. Domain-driven design, event-driven and actor-model architectures, TOGAF. C#/.NET first; Go, Rust, Python; Kubernetes, Helm, Terraform, AWS.

And the part that's rarer: I've built a compiler workbench, a language, an actor runtime, a distributed database with a checked consistency model, and an agentic platform that generates verified systems. When I say a design will hold, I can usually show the proof.

Remote, US or Latin America, English and Spanish. Architect / principal / staff. https://yordivad.github.io

#OpenToWork #SoftwareArchitect #PrincipalEngineer #DotNet #Remote

---

## Day 10 — Software as mathematics

A specification is a theorem. An implementation is its proof.

That's not a metaphor at MLambda; it's the method. Requirements become a model in Z. The model is checked in TLA+ for safety, liveness and consistency. The implementation is derived from it, on a runtime built for it, in a language where the common corruptions can't be written. The tests are obligations the model already implied, not cases someone remembered.

My training is half software engineering and half philosophy of formal science, and that pairing is the whole of the work. Nothing is admitted on faith — least of all by a machine that is very good at sounding sure.

If that's how you think software should be built, let's talk. https://www.mlambda.net/method/

#FormalMethods #SoftwareEngineering #AI #DDD #OpenToWork
