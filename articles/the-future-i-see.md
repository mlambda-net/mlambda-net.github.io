---
layout: page
eyebrow: Essay · Neuro-symbolic AI
title: The future I see
subtitle: Code is about to be cheap. Quality is not. Why I spent years on actors, logic and proofs while the industry bet on scale — and why I am still betting against it.
description: A personal essay by Roy Gonzalez, founder of MLambda — the ideas he fell in love with (Hewitt's actors, reactive data, domain-driven design, Prolog and Haskell, programs as proofs), the gap between architecture and practice that made the last years painful, why LLM-generated code repeats the COBOL mistake at machine speed, the evidence that scaling does not produce reasoning, and the neuro-symbolic bet behind Turing.
permalink: /articles/the-future-i-see/
image: /images/articles/ns-15-the-future-i-see.png
---

<figure class="story-figure">
  <img src="{{ '/images/articles/ns-15-the-future-i-see.png' | relative_url }}" alt="The future I see — a timeline from Turing's instruction tables to vibe coding, and the bet on mathematics over scale." width="1200" height="627">
</figure>

<p>This one is personal. It is about the ideas I fell in love with, the years in which almost nobody
around me wanted them, and why I still think they are the future of software — now more than ever,
precisely because a machine can produce code faster than any of us.</p>

<h2>What I fell in love with</h2>

<p>The first was the <strong>actor model</strong>. When I read Carl Hewitt's 1973 paper I understood that
here was a model of computation that did not descend from the von Neumann machine at all. It is
almost physical: nothing happens except in response to the reception of a message, and on receiving
one an actor may send messages, create other actors, and decide how it will behave towards the next
message. No shared memory, no global clock, no lock — concurrency as a law of nature rather than a
patch on a sequential machine. I loved it enough to build my own framework, which became
<a href="{{ '/products/actors/' | relative_url }}">MLambda.Actors</a>.</p>

<p>The second was Erik Meijer explaining that a database is a reactive system. His argument that
"your mouse is a database" — that a stream of events and a table of rows are two faces of one duality —
made me want a database that <em>was</em> actors: every row an actor, every query a message, consistency
a property proved rather than promised. That is what
<a href="{{ '/products/data/' | relative_url }}">MLambda.Data</a> is.</p>

<p>Then the discipline that gives structure to all of it: Eric Evans's domain-driven design, Alistair
Cockburn's hexagonal architecture — the ports and adapters that keep the domain free of its plumbing —
Robert Martin's clean architecture, and the testing tradition of the Agile Manifesto signatories: Kent
Beck's test-driven development and Ward Cunningham's Framework for Integrated Test, where the test is the
specification and the specification is executable. Every line I have written since has been written
test-first.</p>

<p>And underneath everything, two languages: <strong>Prolog</strong> and <strong>Haskell</strong>. Declarative
and functional, the languages in which one writes theorem provers rather than merely programs. Through
them I found the British school of programming languages — Strachey, Landin, Milner, Hoare — who insisted
that a program is a mathematical object with an axiomatic meaning, and the Curry–Howard correspondence
that makes the insistence exact: propositions are types, and a program is a proof of its type. All code
is the proof of a theorem. Most code, unfortunately, is the proof of nothing in particular.</p>

<p>That was my love: the mathematical precision of the British school, the physical computational model
of the actor, and the idea of software built the way an engineer builds a bridge — from a model that is
checked before anything is poured.</p>

<h2>The gap</h2>

<p>When I began working as an architect I discovered that understanding domain-driven design, actors,
TOGAF and reactive programming was not the problem. The problem was that almost nobody else did, and
that training teams to implement them well was harder than the implementing. Good architectures were
approved and then quietly not built. I ended up writing most of the cores myself, because concepts as
elementary as decoupling and binding did not survive contact with the schedule. I worked in companies
whose stated objective was to deliver software without architecture, and they meant it.</p>

<p>The last years were painful for a simple reason: I watched ugly architectures go to production with
the instruction "if it works, don't touch it", and I watched quality treated as a preference rather than
a property. I was unhappy, and often frustrated, because none of this was necessary. The mathematics
that prevents it has existed for fifty years.</p>

<h2>Turing's warning, and COBOL</h2>

<p>Alan Turing saw this coming before there was a computer to see it on. In his 1945 design report for
the ACE he wrote that the instruction tables — the programs — would have to be made up by mathematicians
with computing experience and a certain puzzle-solving ability. Two years later, lecturing to the London
Mathematical Society, he said that the language of instruction tables "forms a sort of symbolic logic",
and that a human mathematician's training "may be regarded as not unlike putting instruction tables into
a machine". Programming, for the man who invented it, was applied logic and would need logicians.</p>

<p>The industry decided otherwise. In 1959 COBOL was designed so that business programs could be written
in something resembling English, by people who would never need the mathematics — and it was a colossal
commercial success, which proves the demand was real. Business software was born there, and it was born
with the belief that rigour is optional. Dijkstra's verdict, in 1975, was that the use of COBOL "cripples
the mind". I would put it more gently: the sin was never the English syntax. It was the separation of
"business software" from "engineering software", as if the code that moves money could afford to be
less precise than the code that computes a trajectory. Scientific computing kept its error bounds and its
proofs. Business computing kept "if it works, don't touch it".</p>

<h2>The boom repeats the mistake at machine speed</h2>

<p>This is what the language-model boom is, seen from where I stand: business software, produced the
COBOL way, by a machine. "Vibe coding" — describe what you want in colloquial language, accept what
comes back if it runs — is the old habit with the human removed from the loop where the human was the
only remaining check. There is no mathematical knowledge behind the output; there are statements in
natural language that produce something acceptable. And acceptable, as every architect knows, is where
the cost begins: in the bug that takes a week to find, in the change that cannot be made safely, in the
system nobody dares touch.</p>

<p>The measurements are in, and they say what the theory says. Veracode's 2025 study found that
about <strong>45% of AI-generated code samples contained security flaws</strong> from the OWASP top ten. Perry
and colleagues found that developers with an AI assistant wrote <em>less</em> secure code and were
<em>more</em> confident it was secure. METR's 2025 randomised trial found experienced open-source developers
were <strong>19% slower</strong> with AI tools while believing they were faster. GitClear's analysis of
hundreds of millions of changed lines shows duplicated code rising and refactoring falling since the
assistants arrived. None of this is a reason to abandon the tools. It is a reason to stop pretending
that fluency is correctness.</p>

<p>There is a deeper worry, and it is the industry's own. Shumailov and colleagues showed in
<em>Nature</em> that models trained on the output of previous models degrade — "model collapse" — as
the tails of the real distribution disappear. Garbage over garbage is not a metaphor; it is a
measurable feedback loop. It is telling that in August 2026 Anthropic announced it would watermark
the text its models produce, and that one of the uses openly discussed for such marks is keeping
generated material out of future training data. Read that as I read it: the people building these
systems know that their output must not become their own standard — and they are among the most
careful. If a model's habits become the industry's habits, the bad architectures get standardised
and the things that are genuinely good, because they are rare, never enter the corpus at all.</p>

<h2>Companies are finding out</h2>

<p>The enterprise results are consistent with the code results. MIT's 2025 study of enterprise
generative-AI deployments reported that about <strong>95% of pilots produced no measurable impact</strong>
on profit and loss. Gartner predicts that more than <strong>40% of "agentic AI" projects will be cancelled
by the end of 2027</strong>, most of them because the value was never there. Klarna, which announced in
2024 that its assistant was handling two-thirds of customer conversations, said in 2025 that quality had
suffered and began hiring people back. A Canadian tribunal held Air Canada liable for a refund policy its
chatbot invented. Lawyers have been sanctioned for filing cases that a model made up.</p>

<p>None of these are accidents of deployment. They are the one structural fact showing through:
<strong>a language model has no faculty of verification</strong>. OpenAI's own 2025 paper on why models
hallucinate concludes that hallucination is not a bug of a particular model but a consequence of how
models are trained and scored — guessing is rewarded over abstaining. Kambhampati's ICML position paper
shows that autoregressive models cannot plan or self-verify. And Apple's 2025 study of the "reasoning"
models — the ones with the long visible monologue — found their accuracy collapses beyond a complexity
threshold even when the algorithm is handed to them in the prompt. A reasoning model is a System 1 with a
longer monologue. The monologue is not a proof.</p>

<h2>Scaling is not a road to AGI</h2>

<p>Every day someone announces the agentic future, and every announcement rests on the same bet: that
hallucination is a scaling problem, that enough data and enough infrastructure will make the guessing
reliable. I do not believe it, and the people closest to the models are saying so in their own words.
Ilya Sutskever told NeurIPS 2024 that "pre-training as we know it will end", because the data is finite —
the fossil fuel of AI. François Chollet has argued for years that intelligence is the efficiency of
acquiring new skills, not the recall of old ones, and his ARC benchmark remains the place where scale
buys the least. Gary Marcus has been right about this for longer than has been comfortable for him.</p>

<p>And when a frontier laboratory needed answers that had to be <em>right</em>, it did not scale. DeepMind's
AlphaGeometry, published in <em>Nature</em>, pairs a language model with a symbolic deduction engine;
AlphaProof pairs one with a formal proof assistant. The model proposes; a logic decides. Garcez and Lamb
call this the third wave of AI — neural and symbolic, learning and reasoning. That is the bet I am
making. It is simpler than a data centre and much harder than a prompt, and it is a bet — I will say so
plainly rather than sell it as a certainty. But I am sure of the negative half: scaling a System 1 does
not produce a System 2.</p>

<h2>My bet</h2>

<p>So I do not use a language model to write code. I use a language model to help write better
requirements. I built a powerful inference engine for the rest, and I put the model where it is genuinely
good: in front of the human, gathering and validating requirements in the domain's own language. From the requirements a calculator — not a guesser — derives the logic, and
the logic is emitted to the target language. This is more efficient than generation and, more
importantly, deterministic: the same requirements produce the same system, and a change in one is a
change in the other. The architecture is actors, by construction. The verification is mathematical and
symbolic, never neural: model checking for the invariants, analysis for the security gaps, the
performance bottlenecks and the consistency of the data, all of it on the model before a line exists.
That is <a href="{{ '/products/turing/' | relative_url }}">Turing</a>, and the engine inside it is described in
<a href="{{ '/articles/system-two/' | relative_url }}">System 2 for machines</a>.</p>

<p>The list of what it took — the actor model, domain-driven design, reactive programming,
immutability, Haskell, Prolog, temporal logic, TLA<sup>+</sup>, the patterns, model checking — reads to
most people as a wall of hard concepts. They were not hard for me, and not because I am cleverer than
the people who found them hard. It is because I followed Turing's instruction rather than COBOL's: I
used mathematics to make software, all the time, and thought as a mathematician rather than as a
business person. Everything I have shipped was written test-first and modelled before it was built. The
result is an actor framework, a database that is distributed by design because it is made of actors,
and a rational ecosystem for building software with an approach — neuro-symbolic — that is only now
becoming respectable.</p>

<h2>The future I see</h2>

<p>Code will get cheaper. It is already nearly free. Quality will not get cheaper, because quality was
never the cost of typing; it was the cost of knowing what is true about a system, and that cost has not
moved. So the companies that matter will move — are moving — from "business software" to engineering:
requirements that are formal enough to check, architectures that are derived rather than improvised,
verification that runs on the model before the code. The people who win will be the genuinely
exceptional ones, and they will not be the ones pasting whatever the model returned. Generic software,
produced generically, will be worth what it costs to produce, which is nothing.</p>

<p>The human part does not change. Trade, negotiation, collaboration, the conversation in which a
requirement is discovered — those remain human, and the robots and the models can make us faster and
the world better. But the best results will come, as they have always come in engineering, from
precision and mathematical rigour. And the good news — the reason I can write this with hope rather
than only frustration — is that the mathematics has become accessible. Symbolic AI, an expert system that
reasons in logic, can hold the rigour on behalf of a team that never learned it. That is the point of
Turing: not to replace the engineer, but to make engineering the default.</p>

<h2>Why it has hurt</h2>

<p>I have spent years building against the grain of the market, and it has cost me — in positions, in
patience, and lately in a job. It is hard to hold a bet while everyone around you is collecting on the
opposite one. I know the neuro-symbolic programme has open problems: how much of the symbolic layer can
be learned rather than written, how to keep formalisation from becoming the bottleneck, how far an
ontology generalises beyond the domain it was built for. MLambda's research line, Hilbert, exists because
those questions are not settled, and I would rather name them than hide them. But I have never been
able to make myself believe that a system which cannot verify anything will, at sufficient size, verify
everything. I would rather be wrong with a proof than right by accident. That is the dream, that is why
it hurts, and that is why I am not stopping.</p>

<h2>Sources</h2>

<ul>
  <li>Carl Hewitt, Peter Bishop, Richard Steiger, <a href="https://www.ijcai.org/Proceedings/73/Papers/027B.pdf">A Universal Modular ACTOR Formalism for Artificial Intelligence</a>, IJCAI 1973; Hewitt, <a href="https://arxiv.org/abs/1008.1459">Actor Model of Computation</a> (2010).</li>
  <li>Erik Meijer, "Your Mouse is a Database", <em>ACM Queue</em> 10(3), 2012; the duality is the basis of Reactive Extensions.</li>
  <li>Eric Evans, <a href="https://www.domainlanguage.com/ddd/"><em>Domain-Driven Design</em></a> (2003); Alistair Cockburn, <a href="https://alistair.cockburn.us/hexagonal-architecture/">Hexagonal Architecture</a> (2005); Ward Cunningham, <a href="http://fit.c2.com/">Framework for Integrated Test</a>.</li>
  <li>Alan Turing, <a href="https://www.vordenker.de/downloads/turing-vorlesung.pdf">Lecture to the London Mathematical Society, 20 February 1947</a>; <em>Proposed Electronic Calculator</em> (ACE report, 1945).</li>
  <li>Edsger Dijkstra, <a href="https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD498.html">How do we tell truths that might hurt?</a> (EWD498, 1975).</li>
  <li>Philip Wadler, <a href="https://homepages.inf.ed.ac.uk/wadler/papers/propositions-as-types/propositions-as-types.pdf">Propositions as Types</a>, CACM 2015 — the Curry–Howard correspondence.</li>
  <li>Veracode, <a href="https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/">2025 GenAI Code Security Report</a>.</li>
  <li>Neil Perry et al., <a href="https://arxiv.org/abs/2211.03622">Do Users Write More Insecure Code with AI Assistants?</a> (2023).</li>
  <li>METR, <a href="https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/">Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity</a> (2025).</li>
  <li>GitClear, <a href="https://www.gitclear.com/ai_assistant_code_quality_2025_research">AI Copilot Code Quality: 2025 Data</a>.</li>
  <li>Ilia Shumailov et al., <a href="https://www.nature.com/articles/s41586-024-07566-y">AI models collapse when trained on recursively generated data</a>, <em>Nature</em> 2024.</li>
  <li>TechCrunch, <a href="https://techcrunch.com/2026/08/11/anthropic-says-it-will-watermark-text-generated-by-its-ai-models/">Anthropic says it will watermark text generated by its AI models</a> (August 2026).</li>
  <li>Fortune, <a href="https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/">MIT report: 95% of generative AI pilots at companies are failing</a> (2025).</li>
  <li>Gartner, <em>Over 40% of Agentic AI Projects Will Be Canceled by End of 2027</em> (press release, June 2025).</li>
  <li>Klarna, <a href="https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/">AI assistant handles two-thirds of customer service chats</a> (2024); Fortune, <a href="https://fortune.com/2025/05/09/klarna-ai-humans-return-on-investment/">Klarna brings humans back</a> (2025).</li>
  <li>BBC, <a href="https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know">Air Canada chatbot misinformation</a> (2024); <a href="https://en.wikipedia.org/wiki/Mata_v._Avianca,_Inc."><em>Mata v. Avianca</em></a>, S.D.N.Y. 2023.</li>
  <li>Adam Tauman Kalai et al., <a href="https://arxiv.org/abs/2509.04664">Why Language Models Hallucinate</a>, OpenAI, 2025.</li>
  <li>Kambhampati et al., <a href="https://proceedings.mlr.press/v235/kambhampati24a.html">Position: LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks</a>, ICML 2024.</li>
  <li>Parshin Shojaee et al., <a href="https://arxiv.org/abs/2506.06941">The Illusion of Thinking</a>, Apple, 2025.</li>
  <li>The Verge, <a href="https://www.theverge.com/2024/12/13/24320811/what-ilya-sutskever-sees-openai-model-data-training">Ilya Sutskever at NeurIPS 2024: "pre-training as we know it will end"</a>.</li>
  <li>François Chollet, <a href="https://arxiv.org/abs/1911.01547">On the Measure of Intelligence</a> (2019); <a href="https://arcprize.org/">ARC Prize</a>.</li>
  <li>Gary Marcus, <a href="https://garymarcus.substack.com/p/alphaproof-alphageometry-chatgpt">Why the future of AI is neurosymbolic</a>.</li>
  <li>Trinh et al., <a href="https://www.nature.com/articles/s41586-023-06747-5">Solving olympiad geometry without human demonstrations</a>, <em>Nature</em> 2024; DeepMind, <a href="https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/">AI achieves silver-medal standard at the IMO</a>.</li>
  <li>Artur d'Avila Garcez, Luís Lamb, <a href="https://arxiv.org/abs/2012.05876">Neurosymbolic AI: the 3rd Wave</a>.</li>
</ul>

<hr>

<p class="muted">The systems in this essay: <a href="{{ '/products/actors/' | relative_url }}">Actors</a> ·
<a href="{{ '/products/data/' | relative_url }}">Data</a> · <a href="{{ '/products/genesis/' | relative_url }}">Genesis</a> ·
<a href="{{ '/products/turing/' | relative_url }}">Turing</a>.
Related: <a href="{{ '/articles/system-two/' | relative_url }}">System 2 for machines</a> ·
<a href="{{ '/articles/the-llm-never-answers/' | relative_url }}">The LLM never answers</a> ·
<a href="{{ '/articles/the-code-era-is-over/' | relative_url }}">The code era is over</a>.
<a href="mailto:{{ site.data.company.email }}?subject=Turing%20demonstration">Request a demonstration.</a></p>
