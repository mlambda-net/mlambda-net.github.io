---
layout: page
eyebrow: Article · Turing
title: Refusal is a result
subtitle: One small system going through Turing, and what it looks like when software declines to be built wrong.
description: A to-do list goes through MLambda Turing — backlog, requirements, use cases, model, screens, source — and the most important thing it does along the way is refuse.
permalink: /articles/refusal-is-a-result/
image: /images/articles/ns-04-refusal.png
---

<figure class="story-figure">
  <img src="{{ '/images/articles/ns-04-refusal.png' | relative_url }}" alt="Refusal is a result — a counterexample returns to the requirements, never forward to code." width="1200" height="627">
</figure>

<p>The fastest way to understand what Turing is for is to watch it say no.</p>

<p>Here is the smallest system I could think of — a to-do list. Two features, a handful of
stories, one actor. It is deliberately trivial, because the point is not the system. The point
is the order in which things happen to it, and the moments where the platform stops.</p>

<h2>It starts by telling you it isn't sound</h2>

<figure class="story-figure">
  <img src="{{ '/images/turing/01-backlog.png' | relative_url }}" alt="Turing backlog with quantified objectives and a 'not sound yet' banner." width="1919" height="893" loading="lazy">
</figure>

<p>The backlog looks ordinary until you read the objectives. <em>95% of tasks created conform
to defined attributes. 100% of task definitions include a status.</em> Every feature carries a
goal and a number, because a requirement without a scale and a target cannot be verified, only
argued about — that is Tom Gilb's insight, and Turing enforces it as a data type. Above the
backlog there is a banner: <strong>not sound yet</strong>. The Design, Implement and Deploy
buttons are visible and disabled. Nothing downstream will run until the domain is sound, and
the platform tells you so before you have written a line.</p>

<h2>The words are fixed before anything else</h2>

<figure class="story-figure">
  <img src="{{ '/images/turing/02-requirements.png' | relative_url }}" alt="A Turing requirement with its ubiquitous language and a use case with guard and refusal." width="1912" height="919" loading="lazy">
</figure>

<p>A requirement in Turing opens with its ubiquitous language: <em>these are the words the
system is described in, and no others.</em> USER is a persona. CREATE TASK is a command with
two typed fields. TITLE NOT BLANK is a specification over Task. TASKCREATIONFAILED is an event —
how the command is refused. Each term says which analysis declared it.</p>

<p>Then the use case, and this is where most tools stop and Turing doesn't. UC-01 has an actor,
a trigger, an intent, an outcome — and a <strong>guard</strong> and a <strong>refusal</strong>.
What happens when the title is blank is not an edge case to remember later; it is a first-class
part of the requirement, with its own alternative course: TaskCreationFailed is raised, no task
exists. The language models gathered this from a paragraph of prose. The grammar admitted it.</p>

<h2>The diagram is computed, not drawn</h2>

<figure class="story-figure">
  <img src="{{ '/images/turing/03-use-cases.png' | relative_url }}" alt="A use-case diagram Turing derived from the requirements alone." width="1909" height="912" loading="lazy">
</figure>

<p>One actor, two use cases, an «extend» for the refusal. The caption under the tab says it:
<em>from the requirements alone.</em> If the picture and the words ever disagreed, one of them
would be wrong. Here they can't, because one is a function of the other.</p>

<h2>The model refuses to guess</h2>

<figure class="story-figure">
  <img src="{{ '/images/turing/04-model.png' | relative_url }}" alt="The Guimel domain model, with comments stating where a shape was not given." width="1894" height="910" loading="lazy">
</figure>

<p>The requirements are composed into Guimel — the domain language. Personas. A context. An
entity with its fields. Events. Commands. Specifications as predicates. A repository. An
aggregate whose handler <em>allows</em> a persona, <em>requires</em> a specification, and
<em>emits</em> an event when the requirement is unsatisfied.</p>

<p>Now read the comments. <em>SHAPE NOT STATED: nothing says what TaskCreationFailed carries,
so it carries only the identity of what it is about. Name its fields in the requirement.</em>
The model could have invented a plausible payload. Every code generator you have used would
have. Turing does the opposite: it derives the minimum the requirement entails, and points at
the gap. A missing requirement is an unfulfilled obligation. The system's job is to name it,
not to fill it.</p>

<h2>Screens with evidence, source with none to spare</h2>

<figure class="story-figure">
  <img src="{{ '/images/turing/05-screens.png' | relative_url }}" alt="The Pencil screen editor with measured suggestions." width="1914" height="908" loading="lazy">
</figure>

<p>Pencil composes the interface from canonical layouts, and its suggestions come with their
evidence attached: <em>Pagination accompanies Table in 95% of this repository's own wireframes
(source: measured).</em> An observation that would change nothing says so and takes no action.
A suggestion you cannot audit is a guess with good manners; these are not guesses.</p>

<figure class="story-figure">
  <img src="{{ '/images/turing/06-source.png' | relative_url }}" alt="The generated TaskActor source on MLambda.Actors." width="1919" height="903" loading="lazy">
</figure>

<p>And finally, code — a <code>TaskActor</code> on the MLambda runtime, sharded by id, with a
<code>Receive</code> that switches on exactly the commands the model declared and handlers that
return exactly the events it declared, the <code>.samek</code> specifications and the Kubernetes
deployment generated beside it. One comment in the handler is the whole philosophy:
<em>convention-synthesized — the body carries no computation the specification did not already
imply.</em></p>

<h2>Why refusing is the feature</h2>

<p>Count the refusals in this walk-through. The banner refused to let design run. The
requirement refused to leave the blank title unspecified. The model refused to invent a
payload. The screen editor refused to act on an observation that changed nothing. None of these
are errors. They are the platform doing the one thing a code generator cannot: declining to
proceed on something it cannot justify.</p>

<p>That is what "verified before it is built" means in practice. Not a test suite at the end.
A sequence of gates, each of which can say no, in front of every line of code. The system you
get was true before it existed — or it didn't get built.</p>

<hr>

<p class="muted"><a href="{{ '/products/turing/' | relative_url }}">MLambda Turing</a> is in
active development; demonstrations by arrangement.
<a href="mailto:{{ site.data.company.email }}?subject=Turing%20demonstration">Request one on a
domain you describe.</a></p>
