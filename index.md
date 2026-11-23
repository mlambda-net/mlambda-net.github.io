---
layout: home
title: MLambda
description: MLambda builds one family of software from the compiler up — the Aleph language and compiler, Hilbert and Shin for mathematics and logic, a tensor engine on the GPU, actors and an actor-native database, BDI agents with a neural engine, Turing for rational software, and the apps a company runs.
---

<section class="hero hero--split">
  <div>
    <span class="eyebrow">Software engineering, done as engineering</span>
    <h1>Software that is verified before it is built.</h1>
    <p class="hero__lede">A specification is a theorem. An implementation is its proof. MLambda builds
    the whole stack that makes that literal, from the compiler up: <strong>Aleph</strong>, a pure language
    and its native compiler; <strong>Hilbert</strong> and <strong>Shin</strong>, where every rule and every
    formula lives; <strong>Turing</strong>, rational software that reasons about architecture before code;
    and the runtime, the agents, the tools and the applications, all built the same way.</p>
    <div class="hero__actions">
      <a class="btn btn--primary" href="mailto:{{ site.data.company.email }}?subject=Turing%20demonstration">Request a demonstration</a>
      <a class="btn" href="{{ '/products/genesis.html' | relative_url }}">What we are building</a>
    </div>
  </div>
  {% include carousel.html slides=site.data.showcase title="MLambda products" class="carousel--hero" %}
</section>

<section class="section">
  <h2>Why it matters</h2>
  <p class="section__lede">Most software is built first, tested afterwards, and trusted on faith. Generating it faster does not change that.</p>
  <ul class="thesis">
    <li>
      <h3>The problem</h3>
      <p>Defects are found where they are most expensive — in production — because nothing in the
      process could rule them out earlier. AI code generation raises the volume of code without
      raising the guarantee on any line of it.</p>
    </li>
    <li>
      <h3>The wedge</h3>
      <p>Verification before construction. Requirements become a formal model; the model is
      checked for safety, liveness and consistency; the implementation is derived from it and its
      tests are obligations the model already implies. Agents do the work. Proofs decide.</p>
    </li>
    <li>
      <h3>Why now</h3>
      <p>Language models can finally produce the content — requirements, models, code — at the
      pace a business needs. What they cannot produce is the guarantee. MLambda supplies the part
      that is missing: the mathematics that admits or refuses what the model proposes.</p>
    </li>
  </ul>
</section>

<section class="section">
  <h2>A verifiable model</h2>
  <p class="section__lede">Every MLambda system is checked along four axes before it exists, and built in a language that keeps it that way.</p>
  <ul class="pillars">
    <li class="pillar">
      <span class="pillar__label">Consistency</span>
      <h3>Proved, not promised</h3>
      <p>Specifications in <strong>Z</strong>; models checked in <strong>TLA+</strong> for safety, liveness and temporal properties before a line of code. MLambda.Data's consistency model is a checked specification. Aggregates are derived from invariants, so the boundaries that must hold are the boundaries that exist.</p>
    </li>
    <li class="pillar">
      <span class="pillar__label">Security</span>
      <h3>Refusal is part of the model</h3>
      <p>Who may act, on what, under which guard, and what is emitted when the guard fails — <strong>declared in the domain</strong>, not patched in later. Actors isolate state by construction; cluster nodes speak over <strong>mTLS</strong>; the data gateway authenticates with JWT and routes by role.</p>
    </li>
    <li class="pillar">
      <span class="pillar__label">Performance</span>
      <h3>Measured against the target</h3>
      <p>An actor runtime with reactive messaging; a <strong>log-structured storage engine</strong> with Bloom-filtered reads; Aleph compiled to <strong>native code via LLVM</strong> with a direct FFI and SIMD. Every generated system carries benchmarks — throughput, latency, allocation — and design estimates are compared with what verification measures.</p>
    </li>
    <li class="pillar">
      <span class="pillar__label">Memory and mutation</span>
      <h3>Defects with nowhere to occur</h3>
      <p>Aleph is <strong>pure and immutable by default</strong>: no shared mutable state to race on, no null, no unchecked failure — errors are typed values, cases are matched exhaustively, effects are explicit. Coordination is software-transactional memory and channels, not locks. The bugs mutable languages spend their lifetimes chasing are not expressible.</p>
    </li>
  </ul>
</section>

<section class="section">
  <h2>Software as mathematics</h2>
  <div class="prose">
  <p>Aleph has a pure functional core — Hindley–Milner inference, algebraic data types, traits —
  and it is used as one: MLambda's rendering of <em>Category Theory for Programmers</em> is written
  in Aleph, each chapter a runnable program whose laws are verified by property tests. The same
  discipline runs through the stack. A system's invariants are stated as a theorem; the
  model checker is the referee; the implementation is admitted only as a proof. That is what
  MLambda means by treating software as engineering: not a metaphor, a method.</p>
  </div>
  <ul class="proof">
    <li><span class="proof__num">~70</span><span class="proof__label">repositories in one family</span></li>
    <li><span class="proof__num">9</span><span class="proof__label">targets the Aleph compiler emits</span></li>
    <li><span class="proof__num">0 · A · A</span><span class="proof__label">warnings, security, reliability: Ayin's bar</span></li>
    <li><span class="proof__num">95 %</span><span class="proof__label">coverage of derived scenes, at least</span></li>
    <li><span class="proof__num">2019</span><span class="proof__label">building since</span></li>
  </ul>
</section>

<section class="section mission">
  <span class="eyebrow">The mission</span>
  <h2>A system that understands architecture — and builds from it</h2>
  <div class="mission__body">
    <div class="prose">
      <p>The idea is older than the company. Years before MLambda existed, its founder was an
      enterprise architect applying <strong>TOGAF</strong> by hand — business, application, data,
      technology — and watching the same thing happen on every project: the architecture was
      right, and the software still drifted from it, because nothing connected the two except
      people and time.</p>
      <p>The mission became a single sentence: <strong>build a system that understands
      architecture the way TOGAF describes it, expresses each domain as a domain-specific
      language, and runs it on an actor framework built for reactive domain-driven design</strong> —
      so that the model is not documentation about the software, but the thing the software is
      generated and verified from.</p>
      <p>That is what Turing is. A set of <em>rational tools</em>: domain-specific languages that call
      on language models to gather and validate requirements, then hand them to <strong>symbolic
      artificial intelligence</strong> — an inference engine, a proof kernel, a model checker — to
      derive the logic, the views, the tests and the verification. The LLM gathers; the symbolic
      layer decides. Genesis is the workbench the languages are built in; MLambda.Actors is the
      runtime the domains run on; Aleph is the language chosen so the generated system stays
      correct after it exists.</p>
      <p class="mission__sign">This is the application I dreamed of building for many years. I am building it now.
      <br><a href="{{ site.data.company.founder.url }}">— {{ site.data.company.founder.name }}, founder</a></p>
    </div>
    <ul class="mission__map">
      <li><strong>TOGAF</strong><span>the architecture cycle Genesis runs — vision, business, data, application, technology, governance</span></li>
      <li><strong>Domain-specific languages</strong><span>Guimel for the domain, Samek for the specification, Aleph for the program</span></li>
      <li><strong>Actor framework</strong><span>MLambda.Actors — the runtime for reactive domain-driven design</span></li>
      <li><strong>LLM</strong><span>gathers and validates requirements in controlled language</span></li>
      <li><strong>Symbolic AI</strong><span>Shin inference, a proof kernel and TLA+ derive logic, views, tests and verification</span></li>
    </ul>
  </div>
</section>

<section class="section">
  <h2>What we are building</h2>
  <p class="section__lede">One family of software in MLambda.Genesis, every layer written here. <a href="{{ '/products/genesis.html' | relative_url }}">How the parts fit →</a></p>
  <ul class="stack">
    <li><strong>Applications</strong><span><a href="{{ '/products/crm.html' | relative_url }}">CRM</a> · <a href="{{ '/products/erp.html' | relative_url }}">ERP</a> · <a href="{{ '/products/desk.html' | relative_url }}">Desk</a> · <a href="{{ '/products/make.html' | relative_url }}">Make</a> · <a href="{{ '/products/muse.html' | relative_url }}">Muse</a> · Factory · Transport · SCM · WMS · Last Mile · Shop · Box</span></li>
    <li><strong>Services</strong><span><a href="{{ '/products/oauth.html' | relative_url }}">OAuth</a> · <a href="{{ '/products/mail.html' | relative_url }}">Mail</a> · <a href="{{ '/products/store.html' | relative_url }}">Store</a> · Iris · Aura · <a href="{{ '/products/helios.html' | relative_url }}">Helios</a> · EBank</span></li>
    <li><strong>Intelligence</strong><span><a href="{{ '/products/turing.html' | relative_url }}">Turing</a>, rational software · <a href="{{ '/products/max.html' | relative_url }}">Max</a>, BDI agents · <a href="{{ '/products/neuron.html' | relative_url }}">Neuron</a>, the neural engine</span></li>
    <li><strong>Delivery</strong><span><a href="{{ '/products/quality.html' | relative_url }}">Tsadi · Ayin · Litush · Katharsis · Arkhos</a> · <a href="{{ '/products/design.html' | relative_url }}">Playground</a></span></li>
    <li><strong>Runtime</strong><span><a href="{{ '/products/actors/' | relative_url }}">MLambda.Actors</a> · <a href="{{ '/products/data/' | relative_url }}">MLambda.Data</a> · <a href="{{ '/products/os.html' | relative_url }}">MLambda.OS</a></span></li>
    <li><strong>Languages</strong><span><a href="{{ '/products/aleph.html' | relative_url }}">Aleph</a> · <a href="{{ '/products/hilbert.html' | relative_url }}">Hilbert</a> · <a href="{{ '/products/shin.html' | relative_url }}">Shin</a> · <a href="{{ '/products/tensor.html' | relative_url }}">Tensor</a> · <a href="{{ '/products/samek.html' | relative_url }}">Samek</a> · <a href="{{ '/products/aphrodite.html' | relative_url }}">Aphrodite</a> · <a href="{{ '/products/dream.html' | relative_url }}">Dream</a></span></li>
    <li><strong>Machine</strong><span>LLVM · native code on x86-64, ARM64, RISC-V and WebAssembly · the GPU through each system's own driver</span></li>
  </ul>

  <h3 style="margin-top:2.4rem">Four languages, four kinds of work</h3>
  <ul class="split">
    <li><strong>Aleph</strong><em>general logic</em><span>Plumbing, records, readers and wiring, as traits (interfaces) and instances (classes).</span></li>
    <li><strong>Hilbert</strong><em>logic and mathematics</em><span>Every inference a Shin rule, every formula a law, every number on the tensor engine.</span></li>
    <li><strong>Aphrodite</strong><em>what is seen</em><span>Theme, styles, widgets and screens, each view reading a store.</span></li>
    <li><strong>Dream</strong><em>every test</em><span>Pages, states, acts and scenes, many of them derived from the model.</span></li>
  </ul>
</section>

<section class="section">
  <h2>Quality and security first</h2>
  <p class="section__lede">A change moves only when it is proved. Each tool has one job, and decides by logic. <a href="{{ '/products/quality.html' | relative_url }}">The path of a change →</a></p>
  <ul class="split">
    <li><strong>Tsadi</strong><em>creates the tests</em><span>Derives the test obligations from a system's laws, routes and states.</span></li>
    <li><strong>Ayin</strong><em>judges the code</em><span>Green only with 0 warnings, security A, reliability A and coverage of at least 95 %.</span></li>
    <li><strong>Litush</strong><em>polishes the code</em><span>Six agents refactor until Ayin is satisfied, at pre-commit or on a whole repository.</span></li>
    <li><strong>Katharsis</strong><em>drives the release</em><span>Branch, dev, main, tag: green locally before GitHub, never stopping short of the tag.</span></li>
    <li><strong>Arkhos</strong><em>deploys the microservices</em><span>Writes each client's infrastructure from the code's own facts, with a network policy for every route.</span></li>
    <li><strong>Helios</strong><em>watches them</em><span>Traces, logs, metrics, watchers and objectives from every service. Apps integrate only by events, through Make.</span></li>
  </ul>
</section>

<section class="section">
  <h2>Designed, then proved side by side</h2>
  <p class="section__lede">Every screen starts as a clickable prototype. Playground drives the built window into the same states and lays the two on each other, with a slider, until they match. <a href="{{ '/products/design.html' | relative_url }}">How →</a></p>
  <div class="pair">
    <figure><img src="{{ '/products/images/compare/muse-products-canvas.png' | relative_url }}" alt="Muse's products, the prototype canvas" loading="lazy"><figcaption>the prototype</figcaption></figure>
    <figure><img src="{{ '/products/images/compare/muse-products-window.png' | relative_url }}" alt="Muse's products, the built window" loading="lazy"><figcaption>the window, built in Aphrodite</figcaption></figure>
  </div>
</section>

<section class="section">
  <h2>Products</h2>
  <p class="section__lede">A few to start with. <a href="{{ '/products/' | relative_url }}">The whole catalog →</a></p>
  {%- assign picks = "aleph,hilbert,tensor,max,neuron,turing,muse,crm,science" | split: "," %}
  <ul class="grid-cards">
  {%- for slug in picks %}{% assign rp = "_products/" | append: slug | append: ".md" %}{% assign product = site.products | where: "relative_path", rp | first %}{% if product %}{% include product-card.html product=product %}{% endif %}{% endfor %}
  </ul>
</section>

<section class="section">
  <h2>Built for</h2>
  <p class="section__lede">Teams for whom a defect is not an inconvenience.</p>
  <ul class="verticals">
    <li><strong>Financial services and trading</strong><span>Order flow, positions and settlement, where latency and fault tolerance are architectural constraints — the founder's background is a mission-critical US trading platform.</span></li>
    <li><strong>Logistics and supply chain</strong><span>Integration-heavy systems with many parties and no tolerance for lost messages; the founder's years on DHL's logistics core.</span></li>
    <li><strong>Regulated and safety-critical software</strong><span>Anywhere an auditor asks for evidence. A checked specification and derived tests are the evidence.</span></li>
    <li><strong>Teams adopting AI code generation</strong><span>Keep the speed; add the guarantee. Turing puts a model checker between the language model and your codebase.</span></li>
  </ul>
</section>

<section class="section">
  <h2>What's next</h2>
  <p class="section__lede">Direction, not dates.</p>
  <ul class="roadmap">
    <li><strong>Applications</strong><span>Release 1 of ERP, Desk, Make, Factory, Transport, SCM, WMS, Last Mile, Shop and Box, each deployed per client and proved against its prototype.</span></li>
    <li><strong>Turing</strong><span>From the accepted design to the services, screens and tests the other languages build.</span></li>
    <li><strong>Muse</strong><span>Marketing around the product: its assets, its page and its campaigns, with Neuron's models.</span></li>
    <li><strong>MLambda.OS</strong><span>Machines that join into one operating system on actors, updated live.</span></li>
  </ul>
</section>

<section class="section">
  <h2>Method</h2>
  <p class="lede">Every system here is specified in Z, model-checked in TLA+, and only then
  implemented — by people or by agents — with the tests derived from the model rather than
  invented afterwards. <a href="{{ '/method/' | relative_url }}">How MLambda builds software →</a></p>
</section>

<section class="section">
  <h2>Work with MLambda</h2>
  <ul>
    <li><strong>Demonstration</strong> — see Turing run on a domain you describe.</li>
    <li><strong>Consulting</strong> — architecture and delivery with the MLambda stack.</li>
    <li><strong>Commercial licence and support</strong> — for the commercial-tier products and supported use of the open ones.</li>
    <li><strong>Early access</strong> — private builds and repositories for teams evaluating the commercial tier.</li>
  </ul>
  <div class="hero__actions">
    <a class="btn btn--primary" href="mailto:{{ site.data.company.email }}?subject=Turing%20demonstration">Request a demonstration</a>
    <a class="btn" href="{{ '/services/' | relative_url }}">Services</a>
  </div>
</section>
