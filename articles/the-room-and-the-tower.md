---
layout: page
eyebrow: Essay · Philosophy of AI
title: The room and the tower
subtitle: A language model is Searle's Chinese Room with a better calculator. Believing that scale will turn it into a mind is building the Tower of Babel again — and the mind, like God, may be the one object that cannot be studied from outside.
description: A philosophical essay by Roy Gonzalez on why current generative AI operates exactly as Searle's Chinese Room — a Transformer rolling across a landscape of smoothed mountains cast from human text, borrowing cognition it cannot produce — why scaling cannot turn syntax into semantics any more than a taller tower reaches heaven, why a brain can be simulated but a mind cannot be made an object of study from inside itself (Wittgenstein's eye, Nagel, McGinn, Gödel, Kant on God), and the tell that gives the whole story away — no CEO is building the AI that replaces the CEO.
permalink: /articles/the-room-and-the-tower/
image: /images/articles/ns-16-the-room-and-the-tower.png
---

<figure class="story-figure">
  <img src="{{ '/images/articles/ns-16-the-room-and-the-tower.png' | relative_url }}" alt="The room and the tower — Searle's Chinese Room with a landscape of smoothed hills inside it, and a tower built to reach cognition by scale." width="1200" height="627">
</figure>

<p>Two old stories explain the present moment in artificial intelligence better than any benchmark.
One is a thought experiment from 1980 about a man in a room who does not speak Chinese. The other
is a few verses of Genesis about a tower. I want to tell both, adapt the first to the machines we
actually have, and then go one step further than either: to say why the thing the industry is
promising — a mind, produced by making the machine larger — is not merely far away but is the wrong
kind of thing to be reached by that road at all.</p>

<p>I have argued elsewhere that language models are a <a href="{{ '/articles/system-two/' | relative_url }}">System 1
without a System 2</a>, and that scaling a guesser does not produce a checker. This essay is the
philosophical ground under that engineering claim. It is written for people who are not
specialists in AI or in philosophy, so I will take the time to explain the machinery before I say
anything about it.</p>

<h2>What the machine actually is</h2>

<p>Every generative language model on the market today, including the ones sold as "reasoning
models", is a single kind of neural network: the <strong>Transformer</strong>, published by Vaswani
and colleagues in 2017. Its whole job is to predict the next fragment of text — the next
<em>token</em> — given the text so far. It does this once, appends the fragment, and does it again.
A paragraph, a proof, a poem: each is produced one token at a time by the same act of prediction,
repeated.</p>

<p>The "reasoning" models are not a new architecture. DeepSeek's R1 paper, published in
<em>Nature</em> in 2025, is candid about this: the network is the same Transformer, and what changed
is the <em>training</em>. The model is rewarded, by reinforcement learning, when it produces a long
scratchpad of intermediate text before its final answer and that answer turns out to be right. Over
millions of trials it learns that emitting "thinking tokens" first raises its reward. That is the
entire mechanism. The machine that thinks aloud is the machine that guesses, given an extra rule:
<em>write several pages of plausible working before you write the answer</em>. I will come back to
what that rule does and does not buy.</p>

<h2>The landscape of smoothed mountains</h2>

<p>To see why this matters, you need one picture, and it is not a picture of neurons. It is a
picture of terrain.</p>

<p>Imagine that every possible fragment of text is a point on an enormous map — far more dimensions
than three, but a map. Training the model is like pouring the whole of human writing onto that map
and letting it settle. Where human beings have written the same kind of thing many times — the way a
sentence continues, the way a proof step follows another, the way an apology is worded — the ground
rises into a hill. Where nobody has written anything, the ground stays low. The billions of
"weights" inside the model are nothing more than the recorded shape of that terrain: the height of
every hill and the direction of every slope.</p>

<p>Now the crucial detail. The terrain is <em>smoothed</em>. The model does not memorise each
sentence as a separate spike; training rounds the spikes off into rolling hills, so that between
two things it has seen there is a gentle ridge of things it has not seen but which lie "between"
them. This smoothing is the whole trick. It is why a model can complete a sentence nobody has ever
written: it is standing on a ridge between hills that were cast from real text, and it reads the
slope. Mathematicians call this shape a <em>manifold</em>, and the observation that natural data
tends to lie on such a lower-dimensional surface is called the manifold hypothesis; Fefferman,
Mitter and Narayanan gave it a rigorous test in 2016, and Chris Olah's 2014 essay is the clearest
picture of how a network bends the terrain layer by layer.</p>

<p>Generation, then, is walking. You put the model down at the point your prompt names, and it
takes one step downhill — or, when it is told to be "creative", a step that is mostly downhill with
a little noise — to the most probable next token. Then another step. The path it traces is the
answer. A "reasoning" model is one that has been trained to take a long walk through the region of
the map where step-by-step working lives before it arrives at the region where answers live. It
is a longer walk on the same terrain.</p>

<p>Hold on to this: <strong>the hills were not made by the machine.</strong> They were cast, like a
footprint in wet sand, by the humans who wrote the text. The shape of human reasoning is pressed
into the landscape because human reasoning produced the text that poured onto it. When the model
walks a valley of good logic, it is walking a valley that logicians dug. A footprint can be
astonishingly detailed. It is not a foot.</p>

<h2>The Chinese Room, as Searle told it</h2>

<p>In 1980 John Searle asked readers of <em>Behavioral and Brain Sciences</em> to imagine the
following. A man who speaks no Chinese is locked in a room. Through a slot he receives sheets of
paper covered in Chinese characters. He has an enormous rulebook, written in English, that tells
him: when you see these shapes, look up those, copy out these others, and pass them back through
the slot. The rulebook is so good that the sheets he passes out are perfect Chinese answers to the
questions that came in. Outside the room, a Chinese speaker is convinced there is someone inside
who understands Chinese.</p>

<p>Searle's point is short. The man understands nothing. He manipulates symbols by their shape —
<em>syntax</em> — and never at any point comes into contact with what they mean —
<em>semantics</em>. And since a computer program is by definition nothing but the manipulation of
symbols by their shape, running the right program is not sufficient for understanding, no matter how
convincing the output. The Stanford Encyclopedia's entry on the argument lists nearly half a century of
replies; the best known is the "systems reply" — the man does not understand, but the man plus the
rulebook plus the room, taken as a whole, does. Searle's answer was to have the man memorise the
rulebook and work in his head: now the man is the whole system, and he still does not understand
Chinese.</p>

<h2>The Chinese Room, adapted to the machines we have</h2>

<p>Here is the same room, nearly half a century on. The rulebook is gone. In its place the man has a
calculator of extraordinary power and a landscape — the smoothed mountains of the last section —
engraved into it. Chinese characters come through the slot. The man types them in; the calculator
finds the point on the terrain those characters name, reads the slope, and prints the character
that lies one step downhill. The man copies it, appends it, and types again. Sheets of flawless
Chinese go back out through the slot.</p>

<p>Ask the three questions that matter. Does the man understand Chinese? No; he has never learned a
character. Does the calculator understand Chinese? It computes a gradient; it does not know that the
symbols are symbols. Does the landscape understand Chinese? This is the interesting one, and the
answer is that the landscape <em>contains the shape</em> of understanding, because it was cast from
the writing of millions of people who understood — and containing the shape of a thing is not being
the thing. The valley is the shape of the river that cut it. The valley does not flow.</p>

<p>This is the point I want to make as precisely as I can. The only cognition anywhere in that room
is <em>borrowed</em>. It entered with the data, it was pressed into the terrain, and it is read back
out by a machine that could not have produced a single hill of it on its own. Give the calculator an
empty landscape and it produces nothing; give it a landscape cast from nonsense and it produces
fluent nonsense with exactly the same confidence. The machine does not create cognition from the
combination of symbols. It abstracts the cognition that was already in the symbols, and that
abstraction, however dense, is Searle's syntax with better tooling. Stevan Harnad named the
underlying problem in 1990 — the <em>symbol grounding problem</em>: how can the meaning of a symbol
be intrinsic to the system rather than parasitic on the meanings in our heads? — and his image was
trying to learn Chinese from a Chinese-to-Chinese dictionary. A language model is that dictionary,
vast and smoothed. Emily Bender and Alexander Koller made the same argument for modern models in
2020: a system trained only on <em>form</em> has no route to <em>meaning</em>, and they proposed a
test — an octopus that has listened to every telegraph conversation between two islanders and can
imitate either flawlessly, right up to the moment one of them asks for help building a catapult.
The octopus has all the words and none of the world.</p>

<p>And the reasoning models? In the adapted room, the reinforcement learning that produced them
amounts to one more instruction pinned above the calculator: <em>before you pass the answer through
the slot, first print three pages of intermediate characters, because when you do, the answer that
follows is more often marked correct</em>. The man follows it. The pages he prints look, to the
Chinese speaker outside, exactly like someone thinking. They are a longer walk on the same terrain,
and Apple's 2025 study of these models found what the picture predicts: past a complexity threshold
the accuracy collapses, and it collapses even when the correct algorithm is written into the prompt.
The room cannot use an algorithm. It can only walk the slope where algorithms have been written
about.</p>

<h2>The tower</h2>

<p>Every objection to this argument that I hear from industry reduces to one word: <em>scale</em>.
Yes, the model is a calculator on a landscape today, but with ten times the data and a hundred times
the parameters the landscape becomes so fine that the distinction stops mattering, and somewhere on
that curve syntax becomes semantics, the footprint stands up and walks.</p>

<p>Genesis 11 tells of a people who, having one language, resolved to build a city and a tower
"with its top in the heavens", so as to make a name for themselves. The tower is not condemned for
being too small. It is condemned for being a tower: a structure of the wrong kind for the purpose,
built in the belief that heaven is simply very high up, so that enough bricks will reach it. The
story ends with the language of the builders confounded and the work abandoned.</p>

<p>Scaling is the tower. The scaling laws — Kaplan and colleagues, 2020 — are real and I do not
dispute them. But read what they measure: the model's <em>loss</em>, its error at predicting the
next token, falling as a smooth power law with data, parameters and compute. That is fluency. It is
the terrain getting finer and the walk getting surer. Nowhere in the curve is there a quantity called
meaning, because meaning was never in the terrain to begin with; it was in the people who wrote the
text. Making a map more detailed does not make it experience the wind. Adding bricks to a tower does
not change what a tower is. Syntax and semantics are not two ends of one scale, such that enough of
the first becomes the second; they are different categories, and a category is not crossed by
quantity. Even the builders have begun to say so in their own vocabulary: Ilya Sutskever told
NeurIPS in December 2024 that "pre-training as we know it will end", because there is one internet
and the fossil fuel of AI is being used up. The terrain has a finite source, which is us. When it is
all poured in, the hills will be as high as they will ever be, and they will still be hills.</p>

<h2>The eye that cannot see itself</h2>

<p>So far I have argued that this machine does not think. I want now to make a stronger and stranger
claim: that "build a mind" may not be the kind of project that can be carried out from where we
stand, by anyone, with any architecture — and that this is a fact about the mind, not about
engineering.</p>

<p>Consider the difference between simulating a brain and simulating a mind. Simulating a brain is
hard but ordinary science. Henry Markram's Blue Brain Project spent two decades building
biologically faithful models of cortical tissue, neuron by neuron; the European Human Brain Project
concluded in 2023 with an external panel calling the results impressive. Nobody involved claimed to
have produced a mind, and nobody could have, because the brain is an <em>object</em>: we can open
other brains, measure them, compare them, and check the simulation against what we found. That is
how science works on eyes, too. We understand the eye because we can take an eye that is not ours,
dissect it, trace its optics, and confirm that what we found explains what we see. Vision became a
tangible object of study the moment it could be studied in an eye other than the observer's.</p>

<p>The mind has no such other. To make the mind an object of analysis I must use the only
instrument I have, which is my mind, and the instrument cannot be taken out of the circuit to be
inspected. Wittgenstein put it in one line of the <em>Tractatus</em>: nothing in the visual field
allows you to infer that it is seen by an eye. The eye is the limit of the field, not an item in it.
Thomas Nagel, asking what it is like to be a bat, drew the same conclusion from the other side:
there are facts about experience that cannot be reached by any description given from outside the
point of view, and we cannot step out of ours. Colin McGinn, in 1989, gave the position a name —
<em>cognitive closure</em> — and a diagnosis: the link between mind and brain is real, but our
concept-forming faculties may simply be closed to it, the way a dog's are closed to arithmetic. He
did not say there is a miracle. He said there is a lock, and we are on the inside of it.</p>

<p>Gödel gives the lock a mathematical shape. In 1931 he proved that any consistent formal system
rich enough to do arithmetic contains truths it cannot prove, and cannot prove its own consistency
from inside. The lesson I take is not the strong one Lucas and Penrose drew — that minds must
therefore be more than machines; that argument has been fought over for sixty years and I will not
lean my weight on it. The lesson I take is the shape of the result: <em>a system that must use
itself to examine itself will meet truths about itself that it cannot settle</em>. The mind studying
the mind is a self-referential system by construction. It cannot be surprised to find that its own
foundation is the one thing it cannot see whole.</p>

<p>Kant had already found this wall in a different corridor. To prove that God exists, he argued,
reason would have to reach an object that lies beyond all possible experience; but the idea of God
answers to no object that could ever be given to us, so speculative reason can neither prove nor
disprove it, and every attempt smuggles in what it hopes to conclude. Put more bluntly, as it was
put to me: to take God as an object of my experience I would have to stand above God, and there is
nothing above God. The mind is in the same position with respect to itself. To see it as it is I
would have to stand outside it, and there is no outside; every vantage I can occupy is a vantage
<em>of</em> the mind. Whatever else the mind-body problem is, it is the last problem with the shape
of the problem of God, and I think that is why it has not moved in two and a half thousand years of
very good people trying.</p>

<p>Now set the industry's promise against that. The claim is that a model of artificial neurons,
a reduction far cruder than Blue Brain's, will, at sufficient scale, <em>awaken</em> — will produce
the one phenomenon that we cannot make an object even in ourselves, as a by-product of predicting
text. It is not that I think it will take longer than they say. It is that the project has the
structure of the tower: a brick answer to a question that is not about height. One can simulate how a
brain works, and one should. One cannot simulate how the mind operates, because "how the mind
operates" is not available to be copied, not to the engineer and not to the mind that would be doing
the copying.</p>

<h2>The tell</h2>

<p>If you doubt any of this, watch what the builders do rather than what they say. In 2025 and 2026
the chief executives of the largest AI and industrial companies have warned that AI could remove
half of white-collar jobs; the engineers, the analysts, the junior lawyers, the support staff. In an
edX survey of more than five hundred CEOs, 49% agreed that most or all of their <em>own</em> role
should be automated or replaced by AI. Not one has done it. No company has announced the model that
will replace its chief executive, and no board has installed one. The role that is universally
declared automatable in a survey is the one role that is never automated in practice, and that is
not hypocrisy so much as an honest report from the people closest to the machine: they know, in
the way one knows a tool one uses every day, that it does not <em>decide</em>. It walks the terrain.
The deciding — the responsibility, the judgement in a situation the terrain does not cover — they
keep for themselves, because it is the part that was never in the text.</p>

<h2>What follows</h2>

<p>None of this is an argument against the machine. It is an argument about what the machine is,
and a good engineer wants to know what a thing is before betting a company on it. A calculator on a
landscape of human thought is one of the most useful instruments ever built. Used as what it is — a
gatherer, a translator between the way people talk and the way systems must be specified, a proposer
of candidates — it is extraordinary. Used as a mind, it is the man in the room, and every failure
that has made the news, from invented case law to refund policies that never existed, is the slot
opening onto a question the terrain did not cover.</p>

<p>So the practical conclusion is the one I keep arriving at from every direction: put the meaning
where the meaning actually is. It is in the human who states the requirement, and it is in the
logic that can be checked — proofs, model checking, a symbolic engine that either derives a
conclusion from stated axioms or says that it cannot. That is the division of labour behind
<a href="{{ '/products/turing/' | relative_url }}">Turing</a>: the language model gathers, the proofs
decide, and nothing in the system is asked to understand anything, because understanding is the one
service we cannot buy. The room can be a superb clerk. It should never be the judge. And the tower,
however high it is built this year, will not end anywhere but where the first one did.</p>

<h2>Two honesties</h2>

<p>First: the systems reply is not stupid, and neither are its modern heirs. If someone builds a
system that is <em>grounded</em> — that has a body, acts in a world, is corrected by the world and
not only by text — then Harnad's problem changes shape and part of this essay would need to be
rewritten. I am not aware of any such system on the market, and none of the products sold as
"reasoning" today are of that kind. Second: I have used Gödel for the shape of a lesson, not as a
theorem about minds. The Lucas–Penrose argument that minds out-run machines is contested on solid
technical grounds, and a careful reader should not take my essay to have settled it. What I claim is
narrower and, I think, harder to escape: the mind cannot be made an object from outside itself, the
machine's cognition is borrowed from the text of people who had minds, and no quantity of the first
turns into the second.</p>

<h2>Sources</h2>

<ul>
  <li>John R. Searle, <a href="https://artscimedia.case.edu/wp-content/uploads/2013/07/14182625/Searle-Minds-Brains-and-Programs.pdf">Minds, Brains, and Programs</a>, <em>Behavioral and Brain Sciences</em> 3(3), 1980; David Cole, <a href="https://plato.stanford.edu/entries/chinese-room/">The Chinese Room Argument</a>, <em>Stanford Encyclopedia of Philosophy</em>.</li>
  <li>Ashish Vaswani et al., <a href="https://arxiv.org/abs/1706.03762">Attention Is All You Need</a> (2017) — the Transformer.</li>
  <li>Daya Guo et al., <a href="https://www.nature.com/articles/s41586-025-09422-z">DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning</a>, <em>Nature</em> 645, 2025; preprint <a href="https://arxiv.org/abs/2501.12948">arXiv:2501.12948</a>.</li>
  <li>Charles Fefferman, Sanjoy Mitter, Hariharan Narayanan, <a href="https://arxiv.org/abs/1310.0425">Testing the Manifold Hypothesis</a>, <em>Journal of the AMS</em> 29(4), 2016.</li>
  <li>Christopher Olah, <a href="https://colah.github.io/posts/2014-03-NN-Manifolds-Topology/">Neural Networks, Manifolds, and Topology</a> (2014).</li>
  <li>Stevan Harnad, <a href="https://www.cs.ox.ac.uk/activities/ieg/e-library/sources/harnad90_sgproblem.pdf">The Symbol Grounding Problem</a>, <em>Physica D</em> 42, 1990.</li>
  <li>Emily M. Bender, Alexander Koller, <a href="https://aclanthology.org/2020.acl-main.463/">Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data</a>, ACL 2020 — the octopus test.</li>
  <li>Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, Shmargaret Shmitchell, <a href="https://s10251.pcdn.co/pdf/2021-bender-parrots.pdf">On the Dangers of Stochastic Parrots</a>, FAccT 2021.</li>
  <li>Parshin Shojaee et al., <a href="https://arxiv.org/abs/2506.06941">The Illusion of Thinking</a>, Apple, 2025; Kambhampati et al., <a href="https://proceedings.mlr.press/v235/kambhampati24a.html">LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks</a>, ICML 2024.</li>
  <li>Jared Kaplan et al., <a href="https://arxiv.org/abs/2001.08361">Scaling Laws for Neural Language Models</a> (2020).</li>
  <li>The Verge, <a href="https://www.theverge.com/2024/12/13/24320811/what-ilya-sutskever-sees-openai-model-data-training">Ilya Sutskever at NeurIPS 2024: "pre-training as we know it will end"</a>.</li>
  <li><a href="https://www.biblegateway.com/passage/?search=Genesis%2011&version=NRSVUE">Genesis 11:1–9</a>, the Tower of Babel.</li>
  <li>Blue Brain Project: <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10767063/">The Blue Brain Project: pioneering the frontier of brain simulation</a> (2023); Human Brain Project, <a href="https://www.humanbrainproject.eu/en/follow-hbp/news/2023/11/28/impressive-research-results-external-review-panel-evaluates-final-results-of-human-brain-project/">final external review</a> (November 2023).</li>
  <li>Ludwig Wittgenstein, <a href="https://en.wikisource.org/wiki/Tractatus_Logico-Philosophicus"><em>Tractatus Logico-Philosophicus</em></a> (1922), propositions 5.632–5.6331 — the eye and the visual field.</li>
  <li>Thomas Nagel, <a href="https://cse.buffalo.edu/courses/cse725/peter/Nagel_1974.pdf">What Is It Like to Be a Bat?</a>, <em>Philosophical Review</em> 83(4), 1974.</li>
  <li>Colin McGinn, <a href="https://www.newdualism.org/papers/C.McGinn/McGinn_1989_Mind-body-problem_M.pdf">Can We Solve the Mind–Body Problem?</a>, <em>Mind</em> 98(391), 1989 — cognitive closure.</li>
  <li>David Chalmers, <a href="https://consc.net/papers/facing.pdf">Facing Up to the Problem of Consciousness</a>, <em>Journal of Consciousness Studies</em> 2(3), 1995.</li>
  <li>Panu Raatikainen, <a href="https://plato.stanford.edu/entries/goedel-incompleteness/">Gödel's Incompleteness Theorems</a>, <em>Stanford Encyclopedia of Philosophy</em>; J. R. Lucas, <a href="https://philomatica.org/wp-content/uploads/2021/12/lucas1961.pdf">Minds, Machines and Gödel</a>, <em>Philosophy</em> 36, 1961; <a href="https://iep.utm.edu/lp-argue/">The Lucas–Penrose Argument about Gödel's Theorem</a>, <em>Internet Encyclopedia of Philosophy</em>.</li>
  <li>Immanuel Kant, <em>Critique of Pure Reason</em>, "The Ideal of Pure Reason"; Michelle Grier, <a href="https://plato.stanford.edu/entries/kant-metaphysics/">Kant's Critique of Metaphysics</a>, <em>Stanford Encyclopedia of Philosophy</em>.</li>
  <li>Fortune, <a href="https://fortune.com/2026/05/20/tech-ceos-warn-job-losses-glean-chief-says-ai-never-replace-a-single-worker/">While other tech CEOs warn of mass job losses, Glean's chief says AI will never replace a single worker</a> (May 2026).</li>
  <li>edX and Workplace Intelligence, <a href="https://press.edx.org/edx-survey-finds-nearly-half-49-of-ceos-believe-most-or-all-of-their-role-should-be-automated-or-replaced-by-ai">Nearly half (49%) of CEOs believe most or all of their role should be automated or replaced by AI</a> (September 2023).</li>
</ul>

<hr>

<p class="muted">Related: <a href="{{ '/articles/system-two/' | relative_url }}">System 2 for machines</a> ·
<a href="{{ '/articles/the-future-i-see/' | relative_url }}">The future I see</a> ·
<a href="{{ '/articles/the-llm-never-answers/' | relative_url }}">The LLM never answers</a>.
The system built on this division of labour: <a href="{{ '/products/turing/' | relative_url }}">Turing</a>.
<a href="mailto:{{ site.data.company.email }}?subject=Turing%20demonstration">Request a demonstration.</a></p>
