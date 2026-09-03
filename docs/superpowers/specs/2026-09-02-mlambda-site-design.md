# MLambda site redesign — www.mlambda.net

**Date:** 2026-09-02
**Status:** approved design, ready for implementation planning
**Repo:** `mlambda-net/mlambda-net.github.io`, default branch `main`, GitHub Pages with the
custom domain `www.mlambda.net` configured in Pages settings (build type: workflow).
**Sibling:** the personal site spec at
`yordivad.github.io/docs/superpowers/specs/2026-09-02-personal-site-design.md` — same stack,
same harness, deliberately different identity.

---

## 1. Goal

Replace a 2023 template site — generic Bootstrap theme, marketing copy for four products
that no longer represent the work, an About page calling MLambda "an open-source DSL
generator company" — with a vendor site that a technical reader can verify claim by claim
and an investor can read in five minutes.

**Identity (user's decision):** MLambda is a **software company**. Positioning line:

> **Software that is verified before it is built.**

**Commercial facts confirmed true on 2026-09-02** — and the only ones the site may state:

| Fact | On the site as |
|---|---|
| A legal entity exists | Footer and `/about/` carry the legal name and country **once the user supplies them**. Until then: "MLambda", "founded 2019", "Heredia, Costa Rica". No legal suffix is invented. |
| Consulting / services on offer | `/services/` — "Consulting" |
| Commercial licensing / support on offer | `/services/` — "Commercial licence and support"; product tier label "Commercial · early access" |
| Early-access programme exists | `/services/` — "Early access"; the "How to get it" block on Commercial-tier products |

Not true today and therefore absent: customers, logos, testimonials, pricing, revenue,
user or download counts, a team page, a funding ask.

## 2. Current state

| Aspect | Today |
|---|---|
| Source root | `docs/` — a Bootstrap/Liquid theme with `_sass/bootstrap/*`, `assets/js/scripts.js`, mermaid from a CDN, `jekyll-pug` |
| Products | `_products/{identity,net,store,web_core}.md` — Identity microservice, gRPC "Net Library", Store microservice, React "MLambda-Core" |
| About | Mission/Vision boilerplate about a DSL generator |
| Leftovers | `compose.yaml`, `skaffold.yaml`, `makefile`, `script/`, `docker/`, `netlify.toml`, `profile/README.md` (GitHub's untouched placeholder, and in the wrong repo to take effect) |
| Workflow | `actions/upload-pages-artifact@v1` (auto-fails on deprecated `upload-artifact@v3`), Ruby 3.1, `working-directory: ./docs` |
| Serves | `https://www.mlambda.net/` (also `mlambda.net`, `mlambda-net.github.io`) |

## 3. Source of truth

Claims come from the repositories on this machine and from live artifacts, verified
2026-09-02:

| Product | Licence | Public artifacts |
|---|---|---|
| MLambda.Actors | MIT (`MLambda.Actor/LICENSE`) | `actors.mlambda.net`; NuGet `MLambda.Actors` 2.2.x |
| Genesis | MIT (`MLambda.Genesis/LICENSE`) | `genesis.mlambda.net`; NuGet `MLambda.Genesis.*` (11 packages, e.g. `MLambda.Genesis.Parser` 0.12.x, `MLambda.Genesis.Algebra`) |
| Aleph | no LICENSE file | `genesis.mlambda.net/#/languages/aleph` (syntax reference) |
| MLambda.Data | no LICENSE file | `data.mlambda.net` (architecture, consistency model, TLA+ specs, whitepaper) |
| MLambda.UI | no LICENSE file | `mvvm.mlambda.net` |
| MLambda.OS | no LICENSE file | `mlambda-net.github.io/MLambda.OS` |
| Hilbert / ISLT | no LICENSE file | none — research |
| Factory (Turing · Gears · Thinker · Bet · Actor.Agent) | Genesis MIT for the workbench; the factory modules and Actor.Agent are private | `genesis.mlambda.net` (architecture, method book) |

**Tier rule:** a product is labelled **Open · MIT** only if a `LICENSE` file exists in its
repository (today: Actors, Genesis). Every other product is **Commercial · early access**.
Hilbert is **Research** (a third label, used once).

**Agentic LLM work (user asked for this to be introduced):** Genesis's Turing module is an
agent society — `IAgent`/`AgentMessage`/`AgentResult`, an `AgentRoster`, code agents (Better,
FrontEnd) — coordinated by **Gears**, the build engine, with `build.wf`/`advise.wf` flows.
Thinker is the reasoning layer: pluggable LLM providers and RAG acquire knowledge, a
deterministic grammar formalises it, the Shin engine proves over it, a proof kernel re-checks,
a symbolic reinforcement learner improves beliefs — **the LLM never answers; only proofs do.**
MLambda.Actor.Agent is a Claude Code plugin of 17 specialised agents (beam-researcher,
beam-conceptualizer, beam-formator, beam-planner, sequence-modeler, failure-analyst,
verification, code-generator, bdd-tester, benchmark-runner, code-cleanup, cluster-deployer,
integration-demo, application-architect, topology-deployer, diagnostic-agent, release-agent)
that runs the BEAM pipeline from a business description to a deployed actor system.

## 4. Architecture

### 4.1 Stack

Jekyll at the **repository root** (no longer `docs/`), hand-written Sass via `@use`, zero
JavaScript, plugins `jekyll-seo-tag` + `jekyll-sitemap`. `script/check` is the same
Docker copy-in harness as the personal site (no bind mount — Docker Desktop cannot mount
`D:` on the dev machine), extended with this site's assertions. `script/serve` builds via
check and serves `_site` with Python's `http.server`.

**Deleted:** everything under `docs/` except `docs/superpowers/`; `compose.yaml`,
`skaffold.yaml`, `makefile`, `script/*` (replaced), `docker/`, `netlify.toml`, `profile/`.

**Kept:** `images/logo/logo.svg` and `logo-mobile.svg` (moved to `/images/logo/`),
`images/favicon-32x32.svg`, `images/social/github.svg`. Everything else under `docs/images/`
(illustrations, feature icons, product screenshots) is deleted.

### 4.2 CI

`.github/workflows/site.yml` — the same four-step build as the personal site
(`checkout@v4` → `ruby/setup-ruby@v1` with Ruby 3.3 and `bundler-cache` →
`configure-pages@v5` → `jekyll build` → `upload-pages-artifact@v3`), then `deploy-pages@v4`.
The old `jekyll-gh-pages.yml` is deleted. The custom domain is not touched: it is a Pages
setting, not a file, and workflow deploys keep it.

### 4.3 Content model

```
_products/<nn>-<slug>.md   one file per product; front matter: title, slug, tagline,
                           tier (open|commercial|research), status, docs (url|null),
                           packages[] ({name, url}), tech[], weight;
                           body = three H2 sections in fixed order:
                           "What it is" · "What is built" · "How to get it"
_data/services.yml         three engagements: {name, summary, includes[], start}
_data/company.yml          name, legal_name (empty until supplied), founded: 2019,
                           location: "Heredia, Costa Rica", email, founder {name, url},
                           github: https://github.com/mlambda-net
_layouts/                  default.html, page.html, home.html, product.html
_includes/                 head.html, nav.html, footer.html, product-card.html,
                           tier.html, stack-diagram.svg, pipeline-diagram.svg
_sass/                     _tokens.scss, _base.scss, _typography.scss, _layout.scss,
                           _components.scss
assets/css/main.scss
index.md · products.md · method.md · services.md · about.md · 404.html
```

Products collection has `output: true` with `permalink: /products/:slug/`. Ordering in
Liquid via `sort: "weight"`.

## 5. Information architecture — 13 routes

### `/` — Home

1. Positioning line and a three-sentence intro (what MLambda builds; the two tiers; the
   factory).
2. **The stack** — inline SVG (`_includes/stack-diagram.svg`), five layers top to bottom:
   *Method* (BEAM · Turing agents · Actor.Agent) → *Languages* (Genesis · Aleph) →
   *Runtime* (Actors · Data · UI) → *Systems* (OS) → *Intelligence* (Hilbert · Thinker).
   Strokes and text use `currentColor`; fills use CSS custom properties; legible in both
   themes; `<title>`/`<desc>` for accessibility.
3. **Products** — eight cards from `_products` (`product-card.html`): title, tagline, tier
   badge, status, link to the product page.
4. **Method** teaser — two sentences and a link to `/method/`.
5. **Work with MLambda** — the three engagements as one line each, link to `/services/`.

### `/products/` — index

All eight cards, grouped by tier: Open · MIT first, then Commercial · early access, then
Research.

### `/products/<slug>/` × 8 — product pages (`product.html` layout)

Header: title, tagline, tier badge, status in mono. Rail: *Where to verify* (docs URL,
package links) and *Technology* tags. Body: the three H2 sections from the document.

| slug | title | tier | status | "How to get it" |
|---|---|---|---|---|
| `factory` | MLambda Factory | commercial | in active development; demonstrations by arrangement | request early access |
| `genesis` | Genesis | open | published on NuGet | `dotnet add package MLambda.Genesis.Parser` |
| `aleph` | Aleph | commercial | v1.2.0 | request early access |
| `actors` | MLambda.Actors | open | v2.2 on NuGet | `dotnet add package MLambda.Actors` |
| `data` | MLambda.Data | commercial | in development | request early access |
| `ui` | MLambda.UI | commercial | in development | request early access |
| `os` | MLambda.OS | commercial | research microkernel | request early access |
| `hilbert` | Hilbert | research | research, not yet released | not available |


### `/method/` — How MLambda builds software

BEAM end to end, with the second SVG (`pipeline-diagram.svg`): Research → Conceptualisation
→ Formation (Z) → Verification (TLA+) → Production plan → Generate → Test (BDD) → Benchmark
→ Deploy → Verify again. Then the agentic layer: Turing's society and Gears; Actor.Agent's 17
agents; Thinker's rule. The four claims of the method (missing requirement = unfulfilled
obligation; a waiver is a belief; aggregation is derivable; design estimates, verification
measures). Link to the method book on `genesis.mlambda.net`.

### `/services/` — Work with MLambda

Three engagements from `_data/services.yml`, each: name, one-paragraph summary, what it
includes (3–4 bullets), how to start (email). No pricing, no SLAs stated as numbers.

1. **Consulting** — architecture and delivery with the MLambda stack: actor systems,
   distributed data, formal specification and model checking, language tooling.
2. **Commercial licence and support** — for Data, Aleph, UI and OS, and for supported use
   of the open frameworks: licence, updates, support channel.
3. **Early access** — access to private builds and repositories for teams evaluating the
   commercial-tier products.

### `/about/` — About MLambda

What MLambda is; founded 2019; Heredia, Costa Rica; founder Roy Gonzalez with a link to
`https://yordivad.github.io/`; the legal name line rendered only when
`site.data.company.legal_name` is non-empty; contact email; GitHub org link.

### `/404.html`

## 6. Visual design

Dark-first, technical, and deliberately unlike the personal site.

**Type.** Space Grotesk (display), IBM Plex Sans (body), JetBrains Mono (tiers, versions,
commands, diagram labels). Google Fonts with real fallback stacks.

**Palette (dark, default).** ground `#0b0e12`, surface `#141920`, ink `#e6e8eb`, muted
`#9aa3ad`, rule `#242b34`, accent `#5cc8d6` (links, Open tier), warm `#e0a458` (Commercial
tier), research `#b48ead`.
**Light override** under `prefers-color-scheme: light`: ground `#f6f7f8`, surface `#ffffff`,
ink `#151a1f`, muted `#5c6670`, rule `#d9dee4`, accent `#0f7f8c`, warm `#9a5f12`, research
`#6b4d7a`. Tokens as CSS custom properties on `:root`; only the changed ones restated.

**Layout.** 72rem shell; card grid `repeat(auto-fit, minmax(18rem, 1fr))`; product page is a
two-column grid (rail 14rem + content) collapsing below 768px. Diagrams scale to the
container (`width: 100%; height: auto`), max 56rem.

**Logo.** The existing `logo.svg` in the masthead at 32px height, `logo-mobile.svg` below
640px. Both are reused, not redrawn.

## 7. Content integrity rules (binding)

1. Every product page links at least one live artifact (documentation site or NuGet page);
   Hilbert states "no public release" instead.
2. No customers, logos, testimonials, pricing, SLAs with numbers, revenue, user or download
   counts, "trusted by", "leading", "cutting-edge", "revolutionize".
3. **MIT** appears only on products whose repository has a `LICENSE` file (Actors, Genesis).
4. No links into private repositories (`github.com/mlambda-net/MLambda*`); the org link
   `github.com/mlambda-net` is allowed. No Aleph installer commands.
5. Status labels are the ones in §5's table, verbatim.
6. The legal name is rendered only from `_data/company.yml`; if empty, nothing legal is
   implied.
7. Agentic claims are limited to what §3 records: the Turing society, Gears, the 17
   Actor.Agent agents, Thinker's rule.

## 8. Verification

- `./script/check`: clean build; 13 routes exist; every `/products/<slug>/` page contains a
  tier badge and — except Hilbert — at least one `mlambda.net` or `nuget.org` href; `MIT`
  appears only on `actors` and `genesis` pages; forbidden strings absent everywhere
  (`github.com/mlambda-net/MLambda`, `install.sh`, `trusted by`, `customers`, `pricing`,
  `revolutioniz`, `cutting-edge`, a `$` followed by a digit); the two SVGs are inlined (`<svg` present on `/` and
  `/method/`); `sitemap.xml` lists the 13 routes.
- `./script/check --links`: every external URL 200 (LinkedIn 999 tolerated).
- Both themes checked structurally (tokens present); the by-eye pass at 375/768/1440 is the
  user's.
- Workflow green; `https://www.mlambda.net/` serves the new home page; the custom domain is
  still attached (`gh api repos/mlambda-net/mlambda-net.github.io/pages` → `cname`).

## 9. Out of scope

- The GitHub org profile README — requires a `mlambda-net/.github` repository.
- The per-product documentation sites on `*.mlambda.net`.
- NuGet package licence metadata (`PackageLicenseExpression`) — packages currently declare
  none.
- An Aleph documentation site (the README's installer URLs 404).
- The personal site.
