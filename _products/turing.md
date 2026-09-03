---
slug: turing
title: MLambda Turing
tagline: The architecture platform. Describe a system in plain language; get back one that was verified before it was built.
tier: commercial
status: in active development; demonstrations by arrangement
docs: https://genesis.mlambda.net
packages: []
tech: [C#, .NET 10, LLM agents, Guimel, Z notation, TLA+, Reqnroll, Docker, Kubernetes]
weight: 1
---

## What it is

An application factory built on the Genesis workbench. A project name and a prose
description go in; a formal domain, a model-checked specification, and a generated, tested,
containerised system come out. It is not a prompt with a code generator behind it: the
language model acquires content, rules admit it, and what is missing is derived rather than
guessed.

## What is built

**Turing** is the front half — the workbench you see below: backlog, requirements, use cases,
model, screens, source, scenes and chat tracing in one surface — plus a society of agents
that negotiates the domain and **Gears**, the build engine that coordinates them through
declared workflows. **Bet** is the back half: it emits the actor system, the data layer and
the UI from the specification, and **Tsadi** derives the test obligations from the model
instead of searching for them. **Thinker** is the reasoning layer underneath both — pluggable
LLM providers and retrieval acquire knowledge; a deterministic grammar formalises it; a
forward-chaining engine proves over it; a proof kernel re-checks; a symbolic reinforcement
learner improves what is believed over time. The LLM never answers. Only proofs do.

Alongside it, **MLambda.Actor.Agent** packages the same method as a Claude Code plugin: 17 specialised agents
 — research, conceptualisation, formation into Z, production planning,
sequence modelling, failure analysis, TLA+ verification, code generation, BDD testing,
benchmarking, cleanup, cluster deployment, integration demo, application architecture,
topology deployment, diagnostics, release — that take a business description to a deployed
actor system on the MLambda runtime.

## The story

What follows is one small system — a to-do list — going through Turing, as the workbench
shows it.

{% include story-figure.html src="/images/turing/01-backlog.png" w=1919 h=893 alt="The Turing backlog: features grouped as planned and unplanned, each with goals and quantified objectives, and a banner reading 'not sound yet'." caption="Backlog — features, goals, quantified objectives; the domain is 'not sound yet', so Design, Implement and Deploy wait." %}

**It begins with a backlog that knows what it does not know.** Features carry goals and
quantified objectives — *95% of tasks created conform to defined attributes* — because a
requirement without a scale and a target cannot be verified, only argued about. The banner
at the top is the first thing Turing tells you: the domain is not yet sound. Design,
Implement and Deploy are there, and they will not run until it is.

{% include story-figure.html src="/images/turing/02-requirements.png" w=1912 h=919 alt="A requirement in Turing: a ubiquitous language listing persona, command, value, specification, event and entity, then use case UC-01 with trigger, intent, guard, refusal, normal course and alternative." caption="Requirements — the ubiquitous language, then each use case with its guard and its refusal." %}

**Then the words are fixed.** A requirement in Turing starts with the ubiquitous language:
these are the terms the system is described in, *and no others*. Each is typed — persona,
command, value, specification, event, entity — and each says where it came from. The use
case that follows has a trigger, an intent, a guard, and a refusal: what happens when the
title is blank is not an edge case someone remembers later; it is part of the requirement.

{% include story-figure.html src="/images/turing/03-use-cases.png" w=1909 h=912 alt="A use-case diagram drawn by Turing from the requirements alone: a User actor, a Create a New Task use case, and a Title Missing extension." caption="Use cases — drawn from the requirements alone, with the documentation table beneath." %}

**The diagram is derived, not drawn.** One actor, two use cases, an extension for the
refusal — generated from the requirements alone, with the documentation table filled in by
the same analysis that wrote the requirement. If the picture and the words ever disagreed,
one of them would be wrong; here they cannot, because one is computed from the other.

{% include story-figure.html src="/images/turing/04-model.png" w=1894 h=910 alt="The Guimel domain model composed by Turing: personas, a context with entity, events, commands, specifications, a repository and an aggregate whose handler allows, requires and emits." caption="Model — the Guimel domain, composed from the requirements. Where a shape was not stated, the model says so rather than inventing one." %}

**Then it becomes a model — and the model refuses to guess.** The domain is composed into
Guimel: personas, a context, entities, events, commands, specifications, a repository, an
aggregate whose handler *allows* a persona, *requires* a specification and *emits* an event
on refusal. Read the comments. *Shape not stated: nothing says what TaskCreationFailed
carries, so it carries only the identity of what it is about. Name its fields in the
requirement.* A missing requirement is an unfulfilled obligation. The system points at it;
it does not paper over it.

{% include story-figure.html src="/images/turing/05-screens.png" w=1914 h=908 alt="The Pencil screen editor in Turing: a palette of actions, canonical layouts and collections, a wireframe for a task view, a tree, and a suggestions panel citing measured co-occurrence statistics." caption="Screens — Pencil composes wireframes from canonical layouts and suggests from measurement, citing its evidence." %}

**Screens are composed, and the suggestions cite their evidence.** Pencil builds the
interface from canonical layouts and a component palette. Its suggestions are not taste:
*Pagination accompanies Table in 95% of this repository's own wireframes* — source named,
measured or estimated stated. An observation that would change nothing says so and takes
no action.

{% include story-figure.html src="/images/turing/06-source.png" w=1919 h=903 alt="Generated source in Turing: a C# TaskActor on MLambda.Actors with a Receive behaviour switching on CreateTask, AssignPriority and ListTasks, alongside .samek specifications, a csproj and a skaffold.yaml." caption="Source — the generated actor on the MLambda runtime, with its specifications, project and deployment beside it." %}

**Only then is there code.** A `TaskActor` on MLambda.Actors — sharded by id, state
restored on activation, a `Receive` behaviour that switches on the commands the model
declared, handlers that return the events the model declared — with the `.samek`
specifications, the project file and the Kubernetes deployment generated beside it. The
comment in the handler says *convention-synthesized*: the body carries no computation the
specification did not already imply. The system you get was true before it existed.

## How to get it

Turing is not yet a public download. Teams evaluating it can
[request early access](/services/#early-access); the architecture and the method book are
public on the Genesis documentation site.
