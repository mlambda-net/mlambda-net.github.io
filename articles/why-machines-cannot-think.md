---
layout: page
eyebrow: Essay · Philosophy of AI
title: Why machines cannot think
subtitle: A projection can take many dimensions down to three. Nothing can take three back up to many. A machine that computes inside three-dimensional space, on data that is itself a shadow, can lose information but never recover it — and the mind is in what was lost.
description: A philosophical essay by Roy Gonzalez. If the world we experience is a three-dimensional projection of a reality with more dimensions, and consciousness belongs to what the projection discards, then a machine built and trained entirely inside the projection cannot think or become conscious. The mathematics of why: a projection has no inverse, no smooth or one-to-one map from three dimensions fills a larger space (Sard, Brouwer), and no processing creates information the data did not carry (the data-processing inequality). Text is a shadow of a shadow. Turing's imitation game tests the shadow.
permalink: /articles/why-machines-cannot-think/
image: /images/articles/ns-19-why-machines-cannot-think.png
---

<figure class="story-figure">
  <img src="{{ '/images/articles/ns-19-why-machines-cannot-think.png' | relative_url }}" alt="Why machines cannot think — many dimensions project down to three; three cannot be projected back up to many." width="1200" height="627">
</figure>

<p>This is the third essay in a short series. In <a href="{{ '/articles/the-mind-is-not-in-the-shadow/' | relative_url }}">The
mind is not in the shadow</a> I argued that the world we experience is a three-dimensional projection
of a reality with more dimensions, and that consciousness belongs to the part the projection leaves
out. In <a href="{{ '/articles/malkhut-and-the-world-of-ideas/' | relative_url }}">Malkhut and the world
of ideas</a> I followed the idea into the oldest map of it I know. Here I draw the conclusion that
matters most for the industry I work in: why a machine cannot think, and why artificial intelligence,
built the way we build it, will not become conscious.</p>

<p>The argument has one sentence at its centre, and the rest of the essay is an explanation of it.
<strong>You can project many dimensions down to three. You cannot project three back up to
many.</strong></p>

<h2>A shadow cannot be turned back into a hand</h2>

<p>Hold your hand in front of a lamp. Its shadow on the wall is a faithful record of something: the
outline of the hand from one direction. Now try to go the other way. Give someone only the shadow and
ask them to reconstruct the hand. They cannot, and not because they are not clever enough. A fist and a
flat palm turned edge-on can cast the same line. A hand and a paper cut-out of it cast the same shape.
Every hand that could have cast that shadow is equally consistent with it, and there are infinitely
many.</p>

<p>Mathematics says this exactly. A projection from a space of many dimensions onto a space of three
keeps three directions and sends all the others to zero. Different states that differ only in the
discarded directions land on the same point. So a projection has no inverse: there is no rule that takes
the shadow and returns the object, because the shadow does not contain the information that
distinguished the object from all the others that cast it. For every point of the shadow, there is an
entire family of states it could have come from, as large as the dimensions that were thrown away.</p>

<p>And you cannot cheat by mapping the three dimensions back up. Any smooth map from a three-dimensional
space into a larger one covers only a vanishingly thin slice of it: Arthur Sard proved in 1942 that the
image has measure zero, a surface in a room. A continuous map that keeps distinct points distinct can do
no better: by the theory of dimension that Brouwer founded in 1911, its image has no interior. There are
exotic curves, first found by Peano in 1890, that pass through every point of a whole square, but they
do it by folding the line back over itself, passing through the same points more than once, which is
the opposite of recovering anything.
Going down is easy. Going back up, with the information restored, is impossible.</p>

<h2>Processing cannot create what the data never carried</h2>

<p>There is a second theorem, from information theory, that says the same thing about computation. It
is called the data-processing inequality. If the world produces some data, and a machine processes that
data to produce an answer, then the answer cannot contain more information about the world than the
data did. Processing can reorganise information, compress it, surface it, lose it. It cannot create it.
No algorithm, however clever, and no network, however large, gets out of this. It is as basic as the
fact that you cannot pour more water out of a jug than was poured in.</p>

<p>Put the two results together and you have the shape of the whole argument. The world is a state
with more dimensions than we see. Our experience is its projection into three. Everything a machine
receives is a record made inside the projection. Everything it computes, it computes inside the
projection. It can lose information at every step. It cannot, at any step, recover what the projection
threw away.</p>

<h2>Text is a shadow of a shadow</h2>

<p>Now look at what a language model is actually given. It is given text. And text is not even the
three-dimensional world; it is a projection of a projection. A person has a thought. The thought, on the
view of these essays, belongs partly to the dimensions we do not see; what shows of it in the world is
its intention. The person then writes the thought down, which is a second, much harsher projection:
from the full experience of thinking to a line of symbols. The model is trained on those lines. It
learns, superbly, the shape of the shadow: which symbols follow which, across the whole of what people
have written.</p>

<p>That is why a model's output looks like thought. It is cast from the shadows of thought, and a
shadow faithfully records its object's outline. It is also why the output is not thought. The model has
the outline and nothing else. It works in the space of the shadow, and by the two theorems above, it
cannot get back from there to what cast it. The thinking was in the people who wrote. What reaches the
model is what the writing kept.</p>

<h2>Why the machine cannot become conscious</h2>

<p>In the first essay of this series I argued that consciousness belongs to the dimensions the
projection discards: that the brain is the circle a sphere draws as it crosses a plane, and the mind is
the sphere. If that is right, the conclusion about machines follows directly. A machine is a pattern
built in the plane, out of the plane's materials, trained on the plane's shadows. Making the pattern
larger makes a larger pattern in the plane. No amount of circle adds up to a sphere.</p>

<p>This is the precise sense in which the "scaling" promise of the industry is a category mistake. The
bet is that consciousness is a pattern in three-dimensional computation, and that a large enough
pattern will have it. The projection view says that consciousness is not a pattern in the projection at
all. Adding computation adds more of the thing it is not. The tower of the earlier essay is being built,
brick by brick, on the wall of the cave.</p>

<h2>What Turing's test measures</h2>

<p>In 1950 Alan Turing replaced the question "Can machines think?" with a game: if a machine can
converse so that we cannot tell it from a person, we should say it thinks. He anticipated the objection
from consciousness and answered it with a fair point: we never observe anyone's consciousness directly;
we accept other people's minds on the evidence of their behaviour, so we should accept a machine's on
the same evidence.</p>

<p>The projection view agrees with Turing's premise and rejects his conclusion. It is true that we
only ever observe other minds through their behaviour, as intention. That is exactly what the view
predicts: intention is the part of consciousness that shows in three dimensions. But it follows that
the imitation game tests the shadow. A machine trained on the shadows of human intention can reproduce
those shadows, and so it can pass a test that looks only at shadows. Passing it tells us that the
machine has learned the outline. It cannot tell us that anything casts it.</p>

<h2>Two honesties</h2>

<p>First: the mathematics here is exact, but what it is applied to is a thesis. A projection has no
inverse, smooth maps from three dimensions cover nothing of a larger space, and processing cannot create
information. Those are theorems. That consciousness lives in the dimensions the projection discards is
the philosophical thesis of the series, supported by the shape of the evidence rather than proved by it.
If it is false, the argument about consciousness falls with it. The argument that a model trained on text
has only what the text kept does not.</p>

<p>Second: human beings are in three-dimensional space too, so why can we think? On this view, because
a person is not a pattern built inside the projection. A person is the projection of a mind: the circle
is there because the sphere crosses the plane. A machine is a circle drawn on the plane by someone else.
I cannot prove that nothing could ever come to be projected into an artefact. What I can say is that
nothing we do inside the projection, including making the pattern larger, is a way of causing it.</p>

<h2>Sources</h2>

<ul>
  <li>Arthur Sard, "The measure of the critical values of differentiable maps", <em>Bulletin of the American Mathematical Society</em> 48, 1942.</li>
  <li>L. E. J. Brouwer, "Beweis der Invarianz der Dimensionenzahl", <em>Mathematische Annalen</em> 70, 1911 — invariance of dimension.</li>
  <li>Giuseppe Peano, "Sur une courbe, qui remplit toute une aire plane", <em>Mathematische Annalen</em> 36, 1890.</li>
  <li>Claude E. Shannon, "A Mathematical Theory of Communication", <em>Bell System Technical Journal</em> 27, 1948; Thomas M. Cover and Joy A. Thomas, <em>Elements of Information Theory</em>, 2nd edn, Wiley, 2006, §2.8 — the data-processing inequality.</li>
  <li>Alan M. Turing, "Computing Machinery and Intelligence", <em>Mind</em> 59(236), 1950; Graham Oppy and David Dowe, <a href="https://plato.stanford.edu/entries/turing-test/">The Turing Test</a>, <em>Stanford Encyclopedia of Philosophy</em>.</li>
  <li>John R. Searle, <a href="https://artscimedia.case.edu/wp-content/uploads/2013/07/14182625/Searle-Minds-Brains-and-Programs.pdf">Minds, Brains, and Programs</a>, <em>Behavioral and Brain Sciences</em> 3(3), 1980.</li>
  <li>Stevan Harnad, <a href="https://www.cs.ox.ac.uk/activities/ieg/e-library/sources/harnad90_sgproblem.pdf">The Symbol Grounding Problem</a>, <em>Physica D</em> 42, 1990.</li>
  <li>Emily M. Bender, Alexander Koller, <a href="https://aclanthology.org/2020.acl-main.463/">Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data</a>, ACL 2020.</li>
  <li>Ashish Vaswani et al., <a href="https://arxiv.org/abs/1706.03762">Attention Is All You Need</a> (2017); Jared Kaplan et al., <a href="https://arxiv.org/abs/2001.08361">Scaling Laws for Neural Language Models</a> (2020).</li>
  <li>David Chalmers, <a href="https://consc.net/papers/facing.pdf">Facing Up to the Problem of Consciousness</a>, <em>Journal of Consciousness Studies</em> 2(3), 1995.</li>
  <li>Edwin A. Abbott, <a href="https://www.gutenberg.org/ebooks/201"><em>Flatland</em></a> (1884).</li>
</ul>

<hr>

<p class="muted">Related: <a href="{{ '/articles/the-mind-is-not-in-the-shadow/' | relative_url }}">The mind is not in the shadow</a> ·
<a href="{{ '/articles/malkhut-and-the-world-of-ideas/' | relative_url }}">Malkhut and the world of ideas</a> ·
<a href="{{ '/articles/the-room-and-the-tower/' | relative_url }}">The room and the tower</a>.
Where the machine is useful — gathering, while proofs decide: <a href="{{ '/products/turing/' | relative_url }}">Turing</a>.</p>
