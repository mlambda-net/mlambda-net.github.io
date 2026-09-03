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

---

## Day 11 — Efficiency by construction

There are two kinds of performance: the kind you tune, and the kind the architecture has no place to lose.

MLambda.Actors never takes a lock on your state — an actor owns it and handles one message at a time. Every response is an IObservable, so retry, timeout, fan-out and backpressure are operators, not plumbing. [Ephemeral] actors remove the mailbox funnel under load. A local reference is a reference, not a serialisation. Membership is gossip — O(log N) rounds, no ZooKeeper to lose.

MLambda.Data inherits all of it and adds: zero parsing (typed messages, no plan to build), zero-copy locally (0 serialisation hops instead of 4), and an LSM engine whose costs are stated plainly — cache-hit reads under 5 µs, writes bound by the WAL fsync.

The numbers on the performance page are design targets, published so they can be held against measurement. https://www.mlambda.net/articles/efficiency-by-construction/

#DistributedSystems #Databases #ActorModel #DotNet #Performance

---

## Day 12 — Prolog in C#

Every serious C# codebase grows a rules engine, and it always ends as the class nobody wants to touch.

Shin is my answer: a rule language — typed records, Prolog-style rules and queries, structural pattern matching — that compiles to C# at build time through a Roslyn source generator. The rules are source; the C# is generated; diagnostics fire in the build.

Under it, a hybrid kernel: forward chaining (semi-naive Datalog), backward chaining (tabled SLD with stratified negation), and Stratego-style term rewriting — over an immutable knowledge base where every version stays valid. Four modal logics. Truth maintenance. explain returns the proof tree; abduce returns the facts that would make a goal true.

The deepest use: the TLA+ checker's verdict semantics expressed a second time as Shin rules, re-evaluated against the C# evaluator. If they disagree, the checker throws. Two independent meanings agreeing is how you trust a verdict. https://www.mlambda.net/articles/prolog-in-csharp/

#Prolog #Datalog #DotNet #FormalMethods #Compilers #AI

---

## Day 13 — A CAS for engineers

For an engineer, the formula is the specification and the numbers are what you get after.

MLambda.Genesis.Algebra puts symbolic algebra in .NET: differentiate, integrate, simplify, expand, solve, polynomial GCD and factoring, Taylor series, matching modulo associativity and commutativity — pure functions over a seven-constructor expression type.

And it's open: any IRewriteSystem adds rules. So there's a CAS rule language — pattern arms with guards, Hindley–Milner typed — that Roslyn compiles into the algebra. You write the product rule the way you'd write it on a whiteboard; the C# is generated.

Limits stated plainly on the page: double coefficients, real roots, no occurs check yet. What it claims is narrower and true. dotnet add package MLambda.Genesis.Algebra — MIT. https://www.mlambda.net/articles/a-cas-for-engineers/

#ComputerAlgebra #DotNet #Compilers #Engineering #OpenSource

---

## Day 14 — The intelligence LLMs are missing

Ask a language model whether a function has a bug and it answers with the confidence of a colleague and the epistemics of a weather forecast.

It's predicting the next token over a manifold. A bug is a statement that is false about a program — an invariant some reachable state violates, an obligation no test checks. Establishing that is logic and mathematics. No amount of probability becomes it.

That's the intelligence LLMs are missing, and it's what I build. A native TLA+ model checker whose verification logic is Shin rules — reachability as a least fixpoint — with counterexamples certified before they're believed, and verdict semantics implemented twice so disagreement throws. Static and dynamic analysis whose verdicts are rules, not opinions. Tests derived as obligations from the model. Mutation scored exactly: survivors are measured, kills are an upper bound, and the tool says so.

What it found on one generated system: 114 tests, 35 failures — all 35 explained by eight defects, arithmetic that had to sum — and one false green a passing test would never have shown.

The model gathers. The proofs decide. https://www.mlambda.net/articles/the-intelligence-llms-are-missing/

#FormalMethods #ModelChecking #ProgramAnalysis #AI #SoftwareQuality #TLAplus

---

## Day 15 — Context that has been proved (RAG vs CAG)

RAG hands a model passages that look relevant. Nothing checks they're true, consistent, or complete — and the answer is checked by another model, if at all.

At MLambda we do context-augmented generation with a precise meaning of "context": a knowledge base every statement of which passed a verification gate before it was admitted — well-formed, then sortal, then consistent — organised as an ontology with a written formal semantics.

Two networks: the ontological (kinds, duties) and the semantic (things). Rules and facts in Shin, a sortal-modal logic layer: epistemic (S5), deontic (KD), temporal (LTL), alethic — so "verifying semantic, deontic and epistemic information" is three rule families with axioms, not a slogan.

Seven expert layers — Gilb, Project, ECommerce, UX, Design, Solution, Analysis — 378 admitted statements, each expert's ontology assembled as the context, the model asked in its presence, the answer analysed after. Every answer comes back Known, Believed (with a confidence), Unknown, or Contradicted — with a proof or citations.

That's the meta-cognition an LLM can't do: knowing what it knows, how well, and from whom, as a data structure. And Scryer, our statistical substrate, feeds it modal variables the logic can classify.

https://www.mlambda.net/articles/context-that-has-been-proved/

#AI #RAG #KnowledgeGraphs #NeuroSymbolicAI #ExpertSystems #LLM

---

## Day 16 — The formula is the model

For an engineer or an actuary, the formula is the model. The numbers are what you get after.

Genesis has a CAS rule language: write the derivative, the present-value rule, the sensitivity you care about as pattern arms — the way you'd write them on a whiteboard — Hindley–Milner checks the types, and the compiler emits code you call from your own project. Symbolic differentiate, integrate, simplify, solve, Taylor-expand — as pure functions, in the process that has the data.

Beside it, Scryer: intervals, distributions and modal variables (Diday's symbolic data analysis), PCA, regression that returns its diagnostics, clustering — deterministic by seed, so a result reproduces.

Today it compiles to C# and runs on .NET. It is built so that a second emitter is a plug-in, not a rewrite — one language, one typed AST, one emitter per target — and that second target is on the public roadmap, stated as planned rather than done.

Where it belongs: reserves, loss models, sensitivities, stochastic analysis — anywhere a formula has to be right before it becomes a number. https://www.mlambda.net/articles/the-formula-is-the-model/

#ComputerAlgebra #Actuarial #Engineering #DotNet #Statistics #Compilers
