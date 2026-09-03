# MLambda Site Rebuild Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the 2023 Bootstrap template at `www.mlambda.net` with a plain-Jekyll vendor site — eight product pages with honest tier labels, a method page for the BEAM/agentic pipeline, a services page, an about page — every claim linked to a live artifact.

**Architecture:** Same stack and harness as the personal site (`D:\Workspace\yordivad.github.io`): Jekyll at the repo root, Sass via `@use`, zero JavaScript, `script/check` building in Docker by copying the source into a container and asserting on `_site/`. Content lives in a `_products` collection (output: true) plus `_data/services.yml` and `_data/company.yml`. Two inline SVG diagrams are first-class content.

**Tech Stack:** Jekyll 4.3, Dart Sass (`@use` only), Liquid, `jekyll-seo-tag`, `jekyll-sitemap`, Docker `ruby:3.3-slim`, GitHub Actions Pages workflow, custom domain `www.mlambda.net` (Pages setting).

**Spec:** [docs/superpowers/specs/2026-09-02-mlambda-site-design.md](../specs/2026-09-02-mlambda-site-design.md)

## Global Constraints

Copied from the spec; every task inherits them.

- Work in `D:\Workspace\mlambda-net.github.io`. Commit directly on `main`; no branches; no `Co-Authored-By` trailer. Do not push until Task 8.
- **No JavaScript.** No bundler. No CDN scripts (the old theme loaded mermaid from a CDN — gone).
- **Sass uses `@use`, never `@import`.** The build must be warning-free.
- **Docker, not Ruby:** builds run via `script/check`, which copies the source into a `ruby:3.3-slim` container (no bind mount — Docker Desktop cannot mount `D:`). Gems cache in the named volume `jekyll-gems`.
- **Tier rule:** `MIT` may appear only on the `actors` and `genesis` product pages. Every other product is "Commercial · early access"; Hilbert is "Research".
- **Status labels, verbatim:** factory "in active development; demonstrations by arrangement" · genesis "published on NuGet" · aleph "v1.2.0" · actors "v2.2 on NuGet" · data "in development" · ui "in development" · os "research microkernel" · hilbert "research, not yet released".
- **Forbidden anywhere in `_site`:** `github.com/mlambda-net/MLambda`, `install.sh`, `trusted by`, `customers`, `pricing`, `revolutioniz`, `cutting-edge`, and a `$` followed by a digit. The harness asserts all of them.
- **Allowed outbound hosts:** `*.mlambda.net`, `mlambda-net.github.io/MLambda.OS`, `www.nuget.org`, `github.com/mlambda-net` (org root only), `github.com/mlambda-net/go-reactive`, `yordivad.github.io`, `linkedin.com`.
- **Company facts:** name "MLambda", founded 2019, "Heredia, Costa Rica", email `roy.gonzalez@mlambda.net`, founder Roy Gonzalez → `https://yordivad.github.io/`. **No legal name** (the `legal_name` field stays empty and nothing legal is printed).
- **Nothing about customers, testimonials, logos, pricing, SLAs with numbers, revenue, users, downloads, funding.**
- **Palette (dark default):** ground `#0b0e12`, surface `#141920`, ink `#e6e8eb`, muted `#9aa3ad`, rule `#242b34`, accent `#5cc8d6`, warm `#e0a458`, research `#b48ead`. **Light override:** ground `#f6f7f8`, surface `#ffffff`, ink `#151a1f`, muted `#5c6670`, rule `#d9dee4`, accent `#0f7f8c`, warm `#9a5f12`, research `#6b4d7a`.
- **Type:** Space Grotesk (display), IBM Plex Sans (body), JetBrains Mono (mono).
- Collections are ordered in Liquid with `sort: "weight"`, never a `sort_by` config key.

---

## File Structure

**Deleted:** everything under `docs/` except `docs/superpowers/`; `compose.yaml`, `skaffold.yaml`, `makefile`, `script/`, `docker/`, `netlify.toml`, `profile/`, `.github/workflows/jekyll-gh-pages.yml`.

**Moved:** `docs/images/logo/logo.svg`, `docs/images/logo/logo-mobile.svg` → `images/logo/`; `docs/images/favicon-32x32.svg` → `images/`; `docs/images/social/github.svg` → `images/social/`.

**Created:**

| Path | Responsibility |
|---|---|
| `Gemfile`, `_config.yml` | Jekyll 4.3, two plugins, products collection, site data |
| `script/check`, `script/serve` | Harness (copied from the personal site, assertions replaced) |
| `.github/workflows/site.yml` | 4-step Pages workflow |
| `_layouts/default.html`, `page.html`, `home.html`, `product.html` | Shell, prose page, home, product page with rail |
| `_includes/head.html`, `nav.html`, `footer.html`, `tier.html`, `product-card.html`, `story-figure.html`, `stack-diagram.svg`, `pipeline-diagram.svg` | Fragments |
| `docs/genesis-images.md` | Image brief for the four Factory story illustrations (not published) |
| `_sass/_tokens.scss`, `_base.scss`, `_typography.scss`, `_layout.scss`, `_components.scss` | Design system |
| `assets/css/main.scss` | Entry point |
| `_products/{factory,genesis,aleph,actors,data,ui,os,hilbert}.md` | Eight products |
| `_data/company.yml`, `_data/services.yml` | Facts and engagements |
| `index.md`, `products.md`, `method.md`, `services.md`, `about.md`, `404.html` | Pages |

---

## Task 1: Strip the theme, scaffold Jekyll at the root, harness and workflow

**Files:**
- Create: `Gemfile`, `_config.yml`, `script/check`, `script/serve`, `_layouts/default.html`, `_includes/head.html`, `index.md`, `404.html`, `.github/workflows/site.yml`, `_data/company.yml`
- Move: the four image files listed in File Structure
- Delete: as listed in File Structure

**Interfaces:**
- Produces: `script/check` with `build`, `ok`, `bad`, `assert_file`, `assert_contains`, `assert_absent`, `assert_absent_everywhere`, `assert_absent_regex_everywhere`, `check_links`; an `# --- assertions ---` block later tasks append to. `_config.yml` exposes `site.title`, `site.tagline`, `site.description`, `site.url`, and `site.data.company.*` (`name`, `legal_name`, `founded`, `location`, `email`, `founder.name`, `founder.url`, `github`). Layout `default` renders `{{ content }}` inside `<main>`.

- [ ] **Step 1: Copy the harness from the personal site and replace its assertion block**

```bash
cd /d/Workspace/mlambda-net.github.io
mkdir -p script
cp /d/Workspace/yordivad.github.io/script/check script/check
cp /d/Workspace/yordivad.github.io/script/serve script/serve
chmod +x script/check script/serve
git update-index --add --chmod=+x script/check script/serve 2>/dev/null || true
```

Open `script/check`. Add this helper directly after `assert_absent_everywhere()`:

```bash
assert_absent_regex_everywhere() {
  if grep -rqE --binary-files=without-match -- "$1" _site 2>/dev/null; then
    bad "_site must NOT match /$1/ anywhere"
  else
    ok "_site free of /$1/"
  fi
}
```

Then replace everything between `# --- assertions ---` and the `if [ "${1:-}" = "--links" ]` line with:

```bash
# --- assertions ---
assert_file "index.html"
assert_contains "index.html" "MLambda"
assert_contains "index.html" "verified before it is built"
assert_absent_everywhere "Lorem"
assert_absent_everywhere "Welcome to MLambda!"
assert_absent_everywhere "github.com/mlambda-net/MLambda"
assert_absent_everywhere "install.sh"
assert_absent_everywhere "trusted by"
assert_absent_everywhere "customers"
assert_absent_everywhere "pricing"
assert_absent_everywhere "revolutioniz"
assert_absent_everywhere "cutting-edge"
assert_absent_regex_everywhere '\$[0-9]'
assert_absent_everywhere "<script src="
```

- [ ] **Step 2: Run the check to verify it fails**

```bash
./script/check
```

Expected: the build fails — there is no `Gemfile` at the root and `_config.yml` lives in `docs/` — so `bad "build exited …"` and the file assertions fail.

- [ ] **Step 3: Delete the theme and leftovers, move the kept images**

```bash
mkdir -p images/logo images/social
git mv docs/images/logo/logo.svg images/logo/logo.svg
git mv docs/images/logo/logo-mobile.svg images/logo/logo-mobile.svg
git mv docs/images/favicon-32x32.svg images/favicon-32x32.svg
git mv docs/images/social/github.svg images/social/github.svg
git rm -r -q docs/_config.yml docs/_data docs/_includes docs/_layouts docs/_products docs/_sass \
  docs/about.md docs/assets docs/Gemfile docs/Gemfile.lock docs/images docs/index.md \
  docs/netlify.toml docs/products.md docs/.gitignore
git rm -r -q compose.yaml skaffold.yaml makefile docker profile .github/workflows/jekyll-gh-pages.yml
rm -rf docs/_site
ls docs      # expected: only "superpowers"
```

- [ ] **Step 4: Write `Gemfile` and `_config.yml`**

`Gemfile`:

```ruby
source "https://rubygems.org"

gem "jekyll", "~> 4.3"

group :jekyll_plugins do
  gem "jekyll-seo-tag"
  gem "jekyll-sitemap"
end
```

`_config.yml`:

```yaml
title: MLambda
tagline: Software that is verified before it is built.
description: >-
  MLambda builds the stack for correct-by-construction software: the Genesis compiler
  workbench, the Aleph language, the MLambda.Actors runtime, an actor-native database,
  a reactive UI framework, a research microkernel, neuro-symbolic AI — and an agentic
  factory that turns a description into a model-checked, tested, deployable system.
url: "https://www.mlambda.net"
baseurl: ""
lang: en

permalink: pretty

collections:
  products:
    output: true
    permalink: /products/:name/

defaults:
  - scope:
      path: ""
      type: products
    values:
      layout: product

sass:
  sass_dir: _sass
  style: compressed

plugins:
  - jekyll-seo-tag
  - jekyll-sitemap

exclude:
  - Gemfile
  - Gemfile.lock
  - README.md
  - LICENSE
  - script
  - docs
  - vendor
```

`_data/company.yml`:

```yaml
name: MLambda
legal_name: ""
founded: 2019
location: Heredia, Costa Rica
email: roy.gonzalez@mlambda.net
founder:
  name: Roy Gonzalez
  url: https://yordivad.github.io/
github: https://github.com/mlambda-net
```

- [ ] **Step 5: Write the minimal layout, head, stub index, 404**

`_includes/head.html`:

```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" type="image/svg+xml" href="{{ '/images/favicon-32x32.svg' | relative_url }}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600&family=IBM+Plex+Sans:ital,wght@0,400;0,500;1,400&family=JetBrains+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="{{ '/assets/css/main.css' | relative_url }}">
{%- seo -%}
```

`_layouts/default.html`:

```html
<!DOCTYPE html>
<html lang="{{ site.lang | default: 'en' }}">
<head>
  {%- include head.html -%}
</head>
<body>
  <main id="content">
    {{ content }}
  </main>
</body>
</html>
```

`index.md`:

```markdown
---
layout: default
title: MLambda
---

# MLambda

Software that is verified before it is built.
```

`404.html`:

```html
---
permalink: /404.html
layout: default
---

<h1>Not here</h1>
<p>That page does not exist.</p>
```

- [ ] **Step 6: Write the workflow**

`.github/workflows/site.yml`:

```yaml
name: Build and deploy site

on:
  push:
    branches: ["main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.3'
          bundler-cache: true

      - name: Setup Pages
        id: pages
        uses: actions/configure-pages@v5

      - name: Build with Jekyll
        run: bundle exec jekyll build --baseurl "${{ steps.pages.outputs.base_path }}"
        env:
          JEKYLL_ENV: production

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: _site/

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

Also append to `.gitignore`: `_site`, `.jekyll-cache`, `.jekyll-metadata`, `.superpowers/`.

- [ ] **Step 7: Run the check to verify it passes**

```bash
./script/check
```

Expected: `PASS  build clean`, all assertions pass, `0 failed`. The build regenerates `Gemfile.lock`; commit it.

- [ ] **Step 8: Commit**

```bash
git add -A
git commit -m "build: replace the Bootstrap theme with plain Jekyll at the repo root

Deletes the docs/ theme (Bootstrap, jekyll-pug, CDN mermaid, a JS
bundle), the four 2023 product pages, and the compose/skaffold/netlify
leftovers. Adds the Docker copy-in check harness from the personal site
with this site's integrity assertions, a 4-step Pages workflow off the
deprecated upload-pages-artifact@v1, and the company facts data file."
```

---

## Task 2: Design system

**Files:**
- Create: `_sass/_tokens.scss`, `_sass/_base.scss`, `_sass/_typography.scss`, `_sass/_layout.scss`, `_sass/_components.scss`, `assets/css/main.scss`
- Modify: `script/check`

**Interfaces:**
- Produces: custom properties `--ground --surface --ink --muted --rule --accent --warm --research --display --body --mono --shell --measure`; classes `.shell .prose .masthead .masthead__inner .masthead__logo .site-nav .site-footer .hero .hero__lede .grid-cards .card .card__title .card__tagline .card__meta .tier .tier--open .tier--commercial .tier--research .product .product__rail .product__body .rail-block .rail-block__label .tags .tag .btn .diagram .services .service .service__name .muted .mono`.

- [ ] **Step 1: Add the failing style assertions**

Append to the assertions block:

```bash
assert_file "assets/css/main.css"
assert_contains "assets/css/main.css" "--ground: #0b0e12"
assert_contains "assets/css/main.css" "--accent: #5cc8d6"
assert_contains "assets/css/main.css" "prefers-color-scheme: light"
assert_contains "assets/css/main.css" "JetBrains Mono"
```

- [ ] **Step 2: Run the check to verify it fails** — `./script/check` → 5 FAIL lines (no CSS yet).

- [ ] **Step 3: Write `_sass/_tokens.scss`**

```scss
// Dark-first. Only the tokens that change are restated for light.
:root {
  --ground: #0b0e12;
  --surface: #141920;
  --ink: #e6e8eb;
  --muted: #9aa3ad;
  --rule: #242b34;
  --accent: #5cc8d6;
  --warm: #e0a458;
  --research: #b48ead;

  --display: "Space Grotesk", "Helvetica Neue", Arial, sans-serif;
  --body: "IBM Plex Sans", "Segoe UI", Roboto, sans-serif;
  --mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;

  --shell: 72rem;
  --measure: 44rem;

  color-scheme: dark light;
}

@media (prefers-color-scheme: light) {
  :root {
    --ground: #f6f7f8;
    --surface: #ffffff;
    --ink: #151a1f;
    --muted: #5c6670;
    --rule: #d9dee4;
    --accent: #0f7f8c;
    --warm: #9a5f12;
    --research: #6b4d7a;
  }
}
```

- [ ] **Step 4: Write `_sass/_base.scss`**

```scss
*,
*::before,
*::after { box-sizing: border-box; }

html { font-size: 106.25%; }

body {
  margin: 0;
  background: var(--ground);
  color: var(--ink);
  font-family: var(--body);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

img, svg { max-width: 100%; height: auto; }

a {
  color: var(--accent);
  text-decoration-thickness: 1px;
  text-underline-offset: 0.16em;
}

a:hover { text-decoration-thickness: 2px; }

hr { border: 0; border-top: 1px solid var(--rule); margin: 3rem 0; }

::selection { background: var(--accent); color: var(--ground); }

:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }

code, pre {
  font-family: var(--mono);
  font-size: 0.86em;
}

pre {
  background: var(--surface);
  border: 1px solid var(--rule);
  padding: 0.9rem 1rem;
  overflow-x: auto;
}

code { background: var(--surface); padding: 0.1em 0.35em; border-radius: 3px; }
pre code { background: none; padding: 0; }
```

- [ ] **Step 5: Write `_sass/_typography.scss`**

```scss
h1, h2, h3 {
  font-family: var(--display);
  font-weight: 600;
  line-height: 1.15;
  letter-spacing: -0.01em;
  margin: 0 0 0.6em;
}

h1 { font-size: 2.4rem; }
h2 { font-size: 1.5rem; margin-top: 2.4em; }
h3 { font-size: 1.1rem; margin-top: 1.6em; }

p { margin: 0 0 1.2em; }

.lede { font-size: 1.15rem; color: var(--muted); max-width: var(--measure); }
.muted { color: var(--muted); }

.mono,
.card__meta,
.tier,
.tag,
.rail-block__label,
.site-nav a,
.site-footer {
  font-family: var(--mono);
  font-size: 0.78rem;
  letter-spacing: 0.02em;
}

blockquote {
  margin: 1.6rem 0;
  padding: 0.2rem 0 0.2rem 1.1rem;
  border-left: 2px solid var(--accent);
  color: var(--ink);
}

@media (max-width: 768px) {
  h1 { font-size: 1.9rem; }
}
```

- [ ] **Step 6: Write `_sass/_layout.scss`**

```scss
.shell { max-width: var(--shell); margin: 0 auto; padding: 0 1.5rem; }
.prose { max-width: var(--measure); }

// Masthead ------------------------------------------------------------------

.masthead { border-bottom: 1px solid var(--rule); padding: 1.1rem 0; margin-bottom: 3rem; }

.masthead__inner {
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 1rem;
}

.masthead__logo { display: inline-flex; align-items: center; }
.masthead__logo img { height: 32px; width: auto; }
.masthead__logo .logo-mobile { display: none; }

@media (max-width: 640px) {
  .masthead__logo .logo-desktop { display: none; }
  .masthead__logo .logo-mobile { display: inline; height: 28px; }
}

.site-nav ul { display: flex; flex-wrap: wrap; gap: 1.4rem; list-style: none; margin: 0; padding: 0; }
.site-nav a { color: var(--muted); text-decoration: none; padding-bottom: 2px; }
.site-nav a:hover { color: var(--ink); }
.site-nav a[aria-current="page"] { color: var(--ink); border-bottom: 1px solid var(--accent); }

// Footer --------------------------------------------------------------------

.site-footer {
  border-top: 1px solid var(--rule); margin-top: 6rem; padding: 2.5rem 0 4rem; color: var(--muted);
}
.site-footer ul { display: flex; flex-wrap: wrap; gap: 1.4rem; list-style: none; margin: 0 0 1rem; padding: 0; }

// Product page: rail + body -------------------------------------------------

.product { display: grid; grid-template-columns: 14rem 1fr; gap: 0 3rem; align-items: start; }
.product__body { max-width: var(--measure); }
.product__body h2 { margin-top: 2em; }

@media (max-width: 768px) {
  .product { grid-template-columns: 1fr; }
  .masthead { margin-bottom: 2rem; }
}
```

- [ ] **Step 7: Write `_sass/_components.scss`**

```scss
// Hero ----------------------------------------------------------------------

.hero { padding: 1rem 0 2rem; }
.hero h1 { font-size: 2.8rem; max-width: 36rem; }
.hero__lede { font-size: 1.15rem; max-width: var(--measure); }

@media (max-width: 768px) { .hero h1 { font-size: 2rem; } }

// Cards ---------------------------------------------------------------------

.grid-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(18rem, 1fr));
  gap: 1.2rem;
  list-style: none;
  margin: 1.5rem 0 0;
  padding: 0;
}

.card {
  display: block;
  background: var(--surface);
  border: 1px solid var(--rule);
  padding: 1.3rem 1.4rem 1.4rem;
  color: var(--ink);
  text-decoration: none;
}

.card:hover { border-color: var(--accent); text-decoration: none; }
.card__title { font-family: var(--display); font-size: 1.15rem; font-weight: 600; margin: 0.5rem 0 0.3rem; }
.card__tagline { margin: 0 0 0.8rem; color: var(--muted); }
.card__meta { color: var(--muted); display: block; }

// Tier badges ---------------------------------------------------------------

.tier {
  display: inline-block;
  padding: 0.15rem 0.55rem;
  border: 1px solid currentColor;
  border-radius: 2px;
}
.tier--open { color: var(--accent); }
.tier--commercial { color: var(--warm); }
.tier--research { color: var(--research); }

// Product rail --------------------------------------------------------------

.rail-block { margin-bottom: 1.6rem; }
.rail-block__label { display: block; color: var(--muted); margin-bottom: 0.4rem; text-transform: uppercase; }
.rail-block ul { list-style: none; margin: 0; padding: 0; }
.rail-block li { margin-bottom: 0.35rem; }

.tags { display: flex; flex-wrap: wrap; gap: 0.4rem; list-style: none; margin: 0; padding: 0; }
.tag { border: 1px solid var(--rule); color: var(--muted); padding: 0.15rem 0.5rem; border-radius: 2px; }

// Buttons -------------------------------------------------------------------

.btn {
  display: inline-block;
  font-family: var(--mono);
  font-size: 0.8rem;
  border: 1px solid var(--accent);
  color: var(--accent);
  padding: 0.55rem 1rem;
  text-decoration: none;
}
.btn:hover { background: var(--accent); color: var(--ground); }

// Diagrams ------------------------------------------------------------------

.diagram { max-width: 56rem; margin: 2rem 0; }
.diagram svg { width: 100%; height: auto; display: block; }
.diagram .box { fill: var(--surface); stroke: var(--rule); }
.diagram .box--accent { stroke: var(--accent); }
.diagram .label { font-family: var(--display); font-size: 15px; font-weight: 600; fill: var(--ink); }
.diagram .sub { font-family: var(--mono); font-size: 11px; fill: var(--muted); }
.diagram .arrow { stroke: var(--muted); fill: none; }
.diagram .arrowhead { fill: var(--muted); }

// Services ------------------------------------------------------------------

.services { display: grid; grid-template-columns: repeat(auto-fit, minmax(18rem, 1fr)); gap: 1.2rem; list-style: none; padding: 0; margin: 1.5rem 0 0; }
.service { background: var(--surface); border: 1px solid var(--rule); padding: 1.4rem; }
.service__name { font-family: var(--display); font-size: 1.15rem; margin: 0 0 0.5rem; }
.service ul { padding-left: 1.1rem; margin: 0.6rem 0 1rem; }
```

- [ ] **Step 8: Write `assets/css/main.scss`**

```scss
---
---

@use "tokens";
@use "base";
@use "typography";
@use "layout";
@use "components";
```

- [ ] **Step 9: Run the check to verify it passes** — `./script/check` → `0 failed`, no `DEPRECATION` line.

- [ ] **Step 10: Commit**

```bash
git add -A
git commit -m "style: dark-first technical design system

Tokens as custom properties with a light override, Space Grotesk / IBM
Plex Sans / JetBrains Mono, card grid, tier badges (open, commercial,
research), product rail layout, and diagram styling that keys SVG fills
and strokes to the theme."
```

---

## Task 3: Layouts, navigation, footer, about page

**Files:**
- Create: `_includes/nav.html`, `_includes/footer.html`, `_layouts/page.html`, `_layouts/home.html`, `about.md`
- Modify: `_layouts/default.html`, `index.md`, `404.html`, `script/check`

**Interfaces:**
- Consumes: Task 2 classes; `site.data.company.*`.
- Produces: layout `page` (front matter `title`, `subtitle`, `description`; content in `.shell > .prose`), layout `home` (`.shell` only). Nav: Products · Method · Services · About.

- [ ] **Step 1: Add the failing assertions**

```bash
assert_contains "index.html" "site-nav"
assert_contains "index.html" "/products/"
assert_contains "index.html" "/method/"
assert_contains "index.html" "/services/"
assert_contains "index.html" "/about/"
assert_contains "index.html" "roy.gonzalez@mlambda.net"
assert_contains "index.html" "images/logo/logo.svg"
assert_file "about/index.html"
assert_contains "about/index.html" "Heredia, Costa Rica"
assert_contains "about/index.html" "2019"
assert_contains "about/index.html" "yordivad.github.io"
assert_absent "about/index.html" "S.A."
```

- [ ] **Step 2: Run the check to verify it fails** — `./script/check` → 12 FAIL lines (`assert_absent` fails on a missing file, so the `S.A.` line fails too until the page exists).

- [ ] **Step 3: Write `_includes/nav.html` and `_includes/footer.html`**

`_includes/nav.html`:

```html
<nav class="site-nav" aria-label="Main">
  <ul>
    <li><a href="{{ '/products/' | relative_url }}"{% if page.url contains '/products/' %} aria-current="page"{% endif %}>Products</a></li>
    <li><a href="{{ '/method/' | relative_url }}"{% if page.url == '/method/' %} aria-current="page"{% endif %}>Method</a></li>
    <li><a href="{{ '/services/' | relative_url }}"{% if page.url == '/services/' %} aria-current="page"{% endif %}>Services</a></li>
    <li><a href="{{ '/about/' | relative_url }}"{% if page.url == '/about/' %} aria-current="page"{% endif %}>About</a></li>
  </ul>
</nav>
```

`_includes/footer.html`:

```html
<footer class="site-footer">
  <div class="shell">
    <ul>
      <li><a href="mailto:{{ site.data.company.email }}">{{ site.data.company.email }}</a></li>
      <li><a href="{{ site.data.company.github }}">GitHub</a></li>
      <li><a href="{{ site.data.company.founder.url }}">{{ site.data.company.founder.name }}</a></li>
    </ul>
    <p>{% if site.data.company.legal_name != "" %}{{ site.data.company.legal_name }} · {% endif %}{{ site.data.company.name }} · {{ site.data.company.location }} · since {{ site.data.company.founded }}</p>
  </div>
</footer>
```

- [ ] **Step 4: Rewrite `_layouts/default.html`; write `page.html` and `home.html`**

`_layouts/default.html`:

```html
<!DOCTYPE html>
<html lang="{{ site.lang | default: 'en' }}">
<head>
  {%- include head.html -%}
</head>
<body>
  <header class="masthead">
    <div class="shell masthead__inner">
      <a class="masthead__logo" href="{{ '/' | relative_url }}" aria-label="MLambda home">
        <img class="logo-desktop" src="{{ '/images/logo/logo.svg' | relative_url }}" alt="MLambda">
        <img class="logo-mobile" src="{{ '/images/logo/logo-mobile.svg' | relative_url }}" alt="MLambda">
      </a>
      {%- include nav.html -%}
    </div>
  </header>

  <main id="content">
    {{ content }}
  </main>

  {%- include footer.html -%}
</body>
</html>
```

`_layouts/page.html`:

```html
---
layout: default
---
<div class="shell">
  <div class="{% if page.wide %}wide{% else %}prose{% endif %}">
    <h1>{{ page.title }}</h1>
    {%- if page.subtitle %}<p class="lede">{{ page.subtitle }}</p>{% endif -%}
    {{ content }}
  </div>
</div>
```

Add to `_sass/_layout.scss` after `.prose`: `.wide { max-width: var(--shell); }`.

`_layouts/home.html`:

```html
---
layout: default
---
<div class="shell">
  {{ content }}
</div>
```

- [ ] **Step 5: Write `about.md`; update `index.md` and `404.html` to the new layouts**

`about.md`:

```markdown
---
layout: page
title: About MLambda
subtitle: A software company building the stack for software that is verified before it is built.
description: MLambda is a software company in Heredia, Costa Rica, founded in 2019 by Roy Gonzalez. Compiler tooling, an actor runtime, a distributed database, and an agentic factory.
permalink: /about/
---

<p>MLambda was founded in {{ site.data.company.founded }} in {{ site.data.company.location }},
by <a href="{{ site.data.company.founder.url }}">{{ site.data.company.founder.name }}</a> — a
software architect with eighteen years in distributed systems and a second degree in the
philosophy of formal science. The company exists because of one conviction: most software is
tested after the fact and trusted on faith, and it does not have to be.</p>

<h2>What we build</h2>

<p>A stack whose parts share a premise. <a href="{{ '/products/genesis/' | relative_url }}">Genesis</a>
is a compiler workbench that model-checks a specification before anything is built from it.
<a href="{{ '/products/aleph/' | relative_url }}">Aleph</a> is a language with a native
foreign-function interface. <a href="{{ '/products/actors/' | relative_url }}">MLambda.Actors</a>
is an actor runtime for .NET and <a href="{{ '/products/data/' | relative_url }}">MLambda.Data</a>
a database built entirely out of actors, its consistency model specified in TLA+. On top of them
sits the <a href="{{ '/products/factory/' | relative_url }}">Factory</a>: a society of agents that
turns a plain-language description into a formal specification, verifies it, and generates the
tested, containerised system that follows from it.</p>

<h2>How we work</h2>

<p>Two tiers, stated on every product page. <strong>Open</strong> products are MIT-licensed and
published on NuGet with public documentation. <strong>Commercial</strong> products have public
documentation and are available under licence or through early access. The
<a href="{{ '/method/' | relative_url }}">method</a> page describes how systems get built here;
the <a href="{{ '/services/' | relative_url }}">services</a> page describes how to work with us.</p>

{% if site.data.company.legal_name != "" %}
<p class="muted">{{ site.data.company.legal_name }}.</p>
{% endif %}

<h2>Contact</h2>

<ul>
  <li><a href="mailto:{{ site.data.company.email }}">{{ site.data.company.email }}</a></li>
  <li><a href="{{ site.data.company.github }}">github.com/mlambda-net</a></li>
</ul>
```

`index.md` → `layout: home` (keep the stub heading and line for now). `404.html` → `layout: page`, `title: Not here`, body: `<p>That page does not exist. Try <a href="{{ '/products/' | relative_url }}">Products</a> or <a href="{{ '/method/' | relative_url }}">Method</a>.</p>`.

- [ ] **Step 6: Run the check to verify it passes** — `./script/check` → `0 failed`.

- [ ] **Step 7: Commit**

```bash
git add -A
git commit -m "feat: masthead, navigation, footer and the about page

Reuses the existing MLambda logo. Company facts come from
_data/company.yml; the legal-name line renders only when one is set."
```

---

## Task 4: Products collection, product layout, products index

**Files:**
- Create: `_products/factory.md`, `genesis.md`, `aleph.md`, `actors.md`, `data.md`, `ui.md`, `os.md`, `hilbert.md`, `_includes/tier.html`, `_includes/product-card.html`, `_includes/story-figure.html`, `_layouts/product.html`, `products.md`, `docs/genesis-images.md`
- Modify: `script/check`

**Interfaces:**
- Consumes: Task 2 classes, layout `default`.
- Produces: `site.products` with front matter `title`, `tagline`, `tier` (`open|commercial|research`), `status`, `docs` (url or `null`), `packages` (list of `{name, url}` or empty), `tech` (list), `weight`. `_includes/tier.html` expects `tier`; `_includes/product-card.html` expects `product`. Task 5 renders the cards on the home page.

- [ ] **Step 1: Add the failing assertions**

```bash
for s in factory genesis aleph actors data ui os hilbert; do assert_file "products/$s/index.html"; done
assert_file "products/index.html"
assert_contains "products/genesis/index.html" "MIT"
assert_contains "products/actors/index.html" "MIT"
for s in factory aleph data ui os hilbert; do assert_absent "products/$s/index.html" "MIT"; done
assert_contains "products/factory/index.html" "in active development; demonstrations by arrangement"
assert_contains "products/genesis/index.html" "published on NuGet"
assert_contains "products/aleph/index.html" "v1.2.0"
assert_contains "products/actors/index.html" "v2.2 on NuGet"
assert_contains "products/data/index.html" "in development"
assert_contains "products/ui/index.html" "in development"
assert_contains "products/os/index.html" "research microkernel"
assert_contains "products/hilbert/index.html" "research, not yet released"
assert_contains "products/genesis/index.html" "genesis.mlambda.net"
assert_contains "products/genesis/index.html" "nuget.org/packages/MLambda.Genesis.Parser"
assert_contains "products/actors/index.html" "actors.mlambda.net"
assert_contains "products/actors/index.html" "nuget.org/packages/MLambda.Actors"
assert_contains "products/aleph/index.html" "genesis.mlambda.net/#/languages/aleph"
assert_contains "products/data/index.html" "data.mlambda.net"
assert_contains "products/ui/index.html" "mvvm.mlambda.net"
assert_contains "products/os/index.html" "mlambda-net.github.io/MLambda.OS"
assert_contains "products/factory/index.html" "genesis.mlambda.net"
assert_contains "products/hilbert/index.html" "no public release"
assert_contains "products/factory/index.html" "17 specialised agents"
assert_contains "products/index.html" "tier--open"
assert_contains "products/index.html" "tier--commercial"
assert_contains "products/index.html" "tier--research"
```

- [ ] **Step 2: Run the check to verify it fails** — `./script/check` → every new line fails (no products yet; `assert_absent` fails on missing files).

- [ ] **Step 3: Write the includes and the product layout**

`_includes/tier.html`:

```html
{%- case include.tier -%}
{%- when "open" -%}<span class="tier tier--open">Open · MIT</span>
{%- when "commercial" -%}<span class="tier tier--commercial">Commercial · early access</span>
{%- else -%}<span class="tier tier--research">Research</span>
{%- endcase -%}
```

`_includes/product-card.html`:

```html
{%- assign p = include.product -%}
<li>
  <a class="card" href="{{ p.url | relative_url }}">
    {% include tier.html tier=p.tier %}
    <h3 class="card__title">{{ p.title }}</h3>
    <p class="card__tagline">{{ p.tagline }}</p>
    <span class="card__meta">{{ p.status }}</span>
  </a>
</li>
```

`_layouts/product.html`:

```html
---
layout: default
---
<div class="shell">
  <div class="hero">
    {% include tier.html tier=page.tier %}
    <h1>{{ page.title }}</h1>
    <p class="hero__lede">{{ page.tagline }}</p>
    <p class="mono muted">Status: {{ page.status }}</p>
  </div>

  <div class="product">
    <aside class="product__rail">
      <div class="rail-block">
        <span class="rail-block__label">Where to verify</span>
        <ul>
          {%- if page.docs %}<li><a href="{{ page.docs }}">Documentation →</a></li>{% endif -%}
          {%- for p in page.packages %}<li><a href="{{ p.url }}">{{ p.name }} on NuGet →</a></li>{% endfor -%}
          {%- if page.docs == nil and page.packages.size == 0 %}<li class="muted">No public release.</li>{% endif -%}
        </ul>
      </div>
      <div class="rail-block">
        <span class="rail-block__label">Technology</span>
        <ul class="tags">{% for t in page.tech %}<li class="tag">{{ t }}</li>{% endfor %}</ul>
      </div>
      <div class="rail-block">
        <a class="btn" href="{{ '/products/' | relative_url }}">All products</a>
      </div>
    </aside>
    <div class="product__body">
      {{ content }}
    </div>
  </div>
</div>
```

- [ ] **Step 4: Write the eight product documents**

`_products/factory.md`:

```markdown
---
title: MLambda Factory
tagline: Describe a system in plain language. Get back one that was verified before it was built.
tier: commercial
status: in active development; demonstrations by arrangement
docs: https://genesis.mlambda.net
packages: []
tech: [C#, .NET 10, LLM agents, Z notation, TLA+, Reqnroll, Docker, Kubernetes]
weight: 1
---

## What it is

An application factory built on the Genesis workbench. A project name and a prose
description go in; a formal domain, a model-checked specification, and a generated, tested,
containerised system come out. It is not a prompt with a code generator behind it: the
language model acquires content, rules admit it, and what is missing is derived rather than
guessed.

## What is built

**Turing** is the front half — the human surface (a terminal REPL and a web flow: describe,
run, watch, download), a society of agents that negotiates the domain, and **Gears**, the
build engine that coordinates them through declared workflows. **Bet** is the back half: it
emits the actor system, the data layer and the UI from the specification, and **Tsadi**
derives the test obligations from the model instead of searching for them. **Thinker** is the
reasoning layer underneath both — pluggable LLM providers and retrieval acquire knowledge; a
deterministic grammar formalises it; a forward-chaining engine proves over it; a proof kernel
re-checks; a symbolic reinforcement learner improves what is believed over time. The LLM
never answers. Only proofs do.

Alongside it, **MLambda.Actor.Agent** packages the same method as a Claude Code plugin: 17
specialised agents — research, conceptualisation, formation into Z, production planning,
sequence modelling, failure analysis, TLA+ verification, code generation, BDD testing,
benchmarking, cleanup, cluster deployment, integration demo, application architecture,
topology deployment, diagnostics, release — that take a business description to a deployed
actor system on the MLambda runtime.

## The story

{% include story-figure.html src="/images/genesis/01-describe.png" alt="A person describing a business in plain language at a terminal; the words begin to arrange themselves into a graph." %}

**It begins with a description.** Someone who knows the business — not the architecture —
types what it does: who orders, who approves, what must never happen twice. Turing listens.
It does not start generating code; it starts asking what is missing. A missing requirement
is not an oversight to be discovered in production. It is an unfulfilled obligation, and the
system deduces it.

{% include story-figure.html src="/images/genesis/02-society.png" alt="A society of agents around a shared domain graph, each holding a different part of it, with Gears at the centre coordinating." %}

**Then a society argues about it.** Expert agents each own a view — process, data, human
boundary, failure. They propose, critique and refuse in controlled English. Gears, the build
engine, runs the workflow that decides whose turn it is and writes down what each one
concluded. Nothing any agent says is believed yet. It is content, waiting to be admitted.

{% include story-figure.html src="/images/genesis/03-proof.png" alt="A formal specification being checked: a lattice of states with one path marked as a refusal." %}

**Then it is proved, or refused.** A deterministic grammar formalises what the agents
agreed into a Z specification. Thinker's engine proves over it; a proof kernel re-checks
every proof; the TLA+ model checker walks every reachable state looking for the one that
violates an invariant. When it finds one, that is not a failure of the pipeline — it is the
pipeline working. The refusal goes back to the specification, never forward to code. The
language model acquires. Rules admit. Proofs decide.

{% include story-figure.html src="/images/genesis/04-system.png" alt="The verified specification unfolding into a running system: actors, a data layer, a user interface, and the tests derived alongside them." %}

**Only then is it built.** Bet emits the actor system, the data layer and the interface
from the specification. Tsadi derives the tests — obligations the model already implied,
not cases someone remembered to write. It is containerised, deployed, and measured, and
the measurements return to the first step as evidence. The system you get was true before
it existed.

## How to get it

The Factory is not yet a public download. Teams evaluating it can
[request early access](/services/#early-access); the architecture and the method book are
public on the Genesis documentation site.
```

`_includes/story-figure.html` — renders a figure only when the image file exists, so the
page ships without images and picks them up when they are added:

```html
{%- assign found = site.static_files | where: "path", include.src | first -%}
{%- if found -%}
<figure class="story-figure">
  <img src="{{ include.src | relative_url }}" alt="{{ include.alt }}" loading="lazy" width="1600" height="900">
</figure>
{%- endif -%}
```

Add to `_sass/_components.scss`:

```scss
.story-figure { margin: 2rem 0 1.2rem; }
.story-figure img { display: block; border: 1px solid var(--rule); background: var(--surface); }
```

Add to the Task 4 assertions: `assert_contains "products/factory/index.html" "The story"` and
`assert_absent "products/factory/index.html" "story-figure"` (no images exist yet, so no figure
may render — this proves the guard works; remove the second line once images are added).

- [ ] **Step 4b: Write the image brief for the user**

`docs/genesis-images.md` (under `docs/`, which Jekyll excludes — it is a brief for the user
who will generate the images, not site content):

```markdown
# Genesis / Factory story — image brief

Four images, one per beat of "The story" on /products/factory/. Drop each file at the path
given; the page renders it automatically. Then delete the `assert_absent … "story-figure"`
line from `script/check`.

Format: PNG, 1600 × 900 (16:9), no text or lettering in the image, dark ground close to
#0b0e12, one accent close to #5cc8d6 (teal) and one warm close to #e0a458. Style: precise,
diagrammatic, quiet — an engineering illustration, not a poster.

1. `images/genesis/01-describe.png` — *The description.*
   Prompt: A single person at a plain terminal in a dark room, typing. Their words leave the
   screen as thin teal lines and begin arranging themselves in the air into the first nodes
   of a graph — processes, roles, events — still loose and unconnected. No text visible.

2. `images/genesis/02-society.png` — *The society.*
   Prompt: Seven abstract figures around a floating domain graph, each holding or lighting
   one region of it in a slightly different hue; at the centre a small precise mechanism
   (gears, but restrained) turns and threads connect it to each figure in turn. Dark ground,
   teal and warm accents. No text.

3. `images/genesis/03-proof.png` — *The proof.*
   Prompt: A lattice of states rendered as a clean geometric structure of nodes and edges;
   one path through it is highlighted in warm amber and terminates at a barred node — a
   refusal, shown as deliberate and correct, not as an error. Everything else is cool teal on
   near-black. No text.

4. `images/genesis/04-system.png` — *The system.*
   Prompt: The same lattice from image 3 unfolding downward into three layered planes — a
   mesh of small nodes (actors), a stacked store (data), and a rectilinear interface — with
   thin lines of tests drawn alongside each plane rather than after it; at the bottom edge,
   a faint return path curving back up to the top. Dark ground, teal accent, one warm
   highlight. No text.
```

`_products/genesis.md`:

```markdown
---
title: Genesis
tagline: A compiler workbench for building languages — and for verifying what they describe before it exists.
tier: open
status: published on NuGet
docs: https://genesis.mlambda.net
packages:
  - name: MLambda.Genesis.Parser
    url: https://www.nuget.org/packages/MLambda.Genesis.Parser
  - name: MLambda.Genesis.Algebra
    url: https://www.nuget.org/packages/MLambda.Genesis.Algebra
  - name: All Genesis packages
    url: https://www.nuget.org/packages?q=MLambda.Genesis
tech: [C#, .NET 10, Parser combinators, EBNF, ASDL, TLA+, Symbolic algebra]
weight: 2
---

## What it is

A .NET meta-language workbench. Grammars become executable parsers; schemas become typed
syntax trees; specifications become model-checked properties. It is the foundation the
Aleph compiler, the Factory and MLambda's own domain languages are built on.

## What is built

Eleven packages, MIT-licensed: a monadic parser-combinator library with full LINQ support;
an EBNF grammar compiler that emits executable combinators; an ASDL schema parser that
generates C# syntax-tree types; a generator tool (`mlambda-gen`) that turns EBNF plus ASDL
into a language front-end; Shin, a stratified forward-chaining rule language and runtime; a
TLA+ checker and prover with LTL evaluation; a mathematical expression language; a symbolic
algebra system that differentiates, integrates, expands and solves; a CAS rule DSL; and a
SQL front-end with analyser and code generator. Front-ends exist for C#, CSS, JavaScript,
HTML, Guimel, SQL, LLVM IR and Aleph.

## How to get it

```
dotnet add package MLambda.Genesis.Parser
dotnet add package MLambda.Genesis.Algebra
```

Documentation, architecture and the twelve-chapter method book are at genesis.mlambda.net.
```

`_products/aleph.md`:

```markdown
---
title: Aleph
tagline: A functional language that reaches the machine directly — C, assembly, LLVM and WebAssembly through a native FFI.
tier: commercial
status: v1.2.0
docs: https://genesis.mlambda.net/#/languages/aleph
packages: []
tech: [Compiler design, Type systems, FFI, LLVM, WebAssembly, POSIX]
weight: 3
---

## What it is

A programming language designed and implemented at MLambda: grammar, type checker, code
generation and a standard library. Programs compile to native code and can call C,
assembly, LLVM IR and WebAssembly through `import "c"`, `import "asm"`, `import "llvm"` and
`import "wasm"`, so a program can reach a POSIX system call with no runtime in the way.

## What is built

The compiler, and an SDK covering error and recovery policy, resource disposal with full
propagation, a JSON algebraic data type with per-type codecs, equality dictionaries, a
filesystem module that discriminates real error cases through `access(2)`, and a test
framework with TAP output and property testing. Sixty-one tests across eight suites. A
literate rendering of *Category Theory for Programmers* is being written in Aleph as its
first large program.

## How to get it

The syntax reference is public on the Genesis documentation site. The compiler and SDK are
available through [early access](/services/#early-access).
```

`_products/actors.md`:

```markdown
---
title: MLambda.Actors
tagline: A reactive actor runtime for .NET with supervision, clustering, gossip membership and mTLS.
tier: open
status: v2.2 on NuGet
docs: https://actors.mlambda.net
packages:
  - name: MLambda.Actors
    url: https://www.nuget.org/packages/MLambda.Actors
tech: [C#, .NET, System.Reactive, gRPC, Kubernetes, Helm, mTLS]
weight: 4
---

## What it is

An actor-model framework for .NET, MIT-licensed. Concurrency is made tractable by removing
shared state instead of guarding it: every actor owns its state, every interaction is a
message, and every response is an `IObservable<T>`.

## What is built

A root/system/user/temp guardian hierarchy with parent–child supervision; one-for-one and
all-for-one strategies; runtime behaviour switching with become and unbecome; message
stashing and replay; death-watch; lifecycle hooks; dependency-injection registration. Beyond
one process it clusters — gossip-based membership, mTLS between nodes, gRPC transport — and
the same actor code runs standalone, hybrid or clustered on configuration alone. Helm charts
are published for Kubernetes deployment.

## How to get it

```
dotnet add package MLambda.Actors
```

Documentation and the quick start are at actors.mlambda.net. Supported use is available under
[commercial licence and support](/services/#commercial-licence-and-support).
```

`_products/data.md`:

```markdown
---
title: MLambda.Data
tagline: A distributed database in which every component is an actor — and the consistency model is a checked TLA+ specification.
tier: commercial
status: in development
docs: https://data.mlambda.net
packages: []
tech: [C#, .NET 10, LSM storage, B-tree, Bloom filters, Consistent hashing, CRDT, TLA+]
weight: 5
---

## What it is

An actor-native distributed database on the MLambda.Actors runtime. Storage, indexes,
filesystem, query planning and authorisation are all actors; there is no shared mutable
state and there are no mutexes in the data path. Correctness comes from message ordering,
not from locks.

## What is built

A log-structured storage engine — write-ahead log with CRC32 integrity, sorted in-memory
memtable, immutable SSTables, throttled background compaction. Indexes for sorted range
queries, constant-time point lookups, probabilistic existence checks and full-text search.
A schema registry with versioning. A cluster layer that places data on a consistent hash
ring and replicates metadata through CRDT gossip. Three deployment topologies — standalone,
hybrid, cluster — selected by configuration. The consistency model is specified in TLA+ and
model-checked; a research whitepaper accompanies the documentation.

## How to get it

Architecture, consistency model, formal specification and whitepaper are public at
data.mlambda.net. Builds are available through [early access](/services/#early-access);
production use under [commercial licence](/services/#commercial-licence-and-support).
```

`_products/ui.md`:

```markdown
---
title: MLambda.UI
tagline: A reactive MVVM framework that never calls a render method — one view, painted by ImGui, Blazor or Avalonia.
tier: commercial
status: in development
docs: https://mvvm.mlambda.net
packages: []
tech: [C#, Rx.NET, ImGui, Blazor WebAssembly, Avalonia, Material 3]
weight: 6
---

## What it is

A backend-agnostic UI framework for C#. Components describe an atom tree; rendering engines
walk it and paint. The same view code runs on the desktop through ImGui, in the browser
through Blazor WebAssembly, and natively through Avalonia, unchanged.

## What is built

Reactive state on `Observable<T>` and `Computed<T>`; an enforced Control → ViewModel → View
→ Design separation; **Morphe**, an algebraic styling system — Geometry × Color × Font — so
styles compose like expressions rather than cascading; a component catalogue mapped to the
Material 3 specification; three rendering backends.

## How to get it

Concepts, the Morphe algebra and the component reference are public at mvvm.mlambda.net.
The framework is available through [early access](/services/#early-access).
```

`_products/os.md`:

```markdown
---
title: MLambda.OS
tagline: A Minix 3-inspired microkernel for x86-64, specified before it is implemented.
tier: commercial
status: research microkernel
docs: https://mlambda-net.github.io/MLambda.OS
packages: []
tech: [Rust, C, x86-64, Assembly, Microkernel]
weight: 7
---

## What it is

A research microkernel written to own the whole stack down to the hardware: the layer the
runtime, the database and the language ultimately stand on.

## What is built

Specifications and implementation, subsystem by subsystem: CPU feature detection, the GDT
and IDT, paging, protection rings and the syscall boundary; then processes, IPC, memory
management, a filesystem and I/O. Every subsystem is specified first, and the specification
is the authority the implementation is checked against.

## How to get it

The specifications are public. Source is available through
[early access](/services/#early-access).
```

`_products/hilbert.md`:

```markdown
---
title: Hilbert
tagline: A neuro-symbolic transformer that reasons across five systems of logic and learns from each input without retraining.
tier: research
status: research, not yet released
docs: null
packages: []
tech: [Python, PyTorch, Transformers, Graph attention, Fast weights, Meta-learning, Modal logic, Temporal logic]
weight: 8
---

## What it is

Research into neural architectures that carry logic inside them rather than bolting a
reasoner onto the side. The founding observation: a transformer's attention layer is
mathematically an adaptive filter with feedback — which means it can be made to learn from
each input as it arrives.

## What is built

Five levels, each with a different logic: first-order; relational with graph attention;
modal with a multi-world attention matrix; temporal with LTL and dual causal/bidirectional
attention; sortal with ontology-biased attention. Fast weights and episodic memory connect
them; a strange loop after Hofstadter feeds the top level's error signal back down to
refine the lower four at inference time; a genetic layer evolves populations of fast-weight
configurations against gradient descent. The same commitments drive Thinker, the reasoning
layer of the Factory.

## How to get it

There is no public release. Hilbert is active research; results will be published when
they are ready.
```

- [ ] **Step 5: Write `products.md`**

```markdown
---
layout: page
title: Products
subtitle: Two tiers, stated on every page. Open products are MIT-licensed on NuGet with public documentation; Commercial products have public documentation and are available under licence or through early access.
description: The MLambda product line — Genesis, Aleph, MLambda.Actors, MLambda.Data, MLambda.UI, MLambda.OS, the Factory and Hilbert — with tiers, status and where to verify each.
permalink: /products/
wide: true
---

{% assign all = site.products | sort: "weight" %}

<h2>Open · MIT</h2>
<ul class="grid-cards">
{% for product in all %}{% if product.tier == "open" %}{% include product-card.html product=product %}{% endif %}{% endfor %}
</ul>

<h2>Commercial · early access</h2>
<ul class="grid-cards">
{% for product in all %}{% if product.tier == "commercial" %}{% include product-card.html product=product %}{% endif %}{% endfor %}
</ul>

<h2>Research</h2>
<ul class="grid-cards">
{% for product in all %}{% if product.tier == "research" %}{% include product-card.html product=product %}{% endif %}{% endfor %}
</ul>
```

- [ ] **Step 6: Run the check to verify it passes** — `./script/check` → `0 failed`. Then `./script/check --links` → every URL 200.

- [ ] **Step 7: Commit**

```bash
git add -A
git commit -m "feat: products collection, product pages and index

Eight products with honest tier labels: MIT only where a LICENSE file
exists (Actors, Genesis); Commercial / early access for Data, Aleph, UI,
OS and the Factory; Research for Hilbert. Every page links a live
documentation site or NuGet page, or says there is no public release."
```

---

## Task 5: Home page with the stack diagram

**Files:**
- Create: `_includes/stack-diagram.svg`
- Modify: `index.md`, `script/check`

**Interfaces:**
- Consumes: `product-card.html`, `.hero`, `.diagram`, `.grid-cards`.

- [ ] **Step 1: Add the failing assertions**

```bash
assert_contains "index.html" "<svg"
assert_contains "index.html" "The stack"
assert_contains "index.html" "tier--open"
assert_contains "index.html" "MLambda Factory"
assert_contains "index.html" "Hilbert"
assert_contains "index.html" "/method/"
assert_contains "index.html" "Early access"
```

- [ ] **Step 2: Run the check to verify it fails** — `./script/check` → 6 FAIL lines (`/method/` is already in the nav and passes).

- [ ] **Step 3: Write `_includes/stack-diagram.svg`**

```html
<svg viewBox="0 0 800 400" role="img" aria-labelledby="stack-t stack-d" xmlns="http://www.w3.org/2000/svg">
  <title id="stack-t">The MLambda stack</title>
  <desc id="stack-d">Five layers: Method on top (BEAM, Turing agents, Actor.Agent), then Languages (Genesis, Aleph), Runtime (Actors, Data, UI), Systems (OS), and Intelligence at the base (Hilbert, Thinker).</desc>
  <g class="layer">
    <rect class="box box--accent" x="40" y="20" width="720" height="60" rx="3"/>
    <text class="label" x="60" y="45">Method</text>
    <text class="sub" x="60" y="66">BEAM · Turing agent society · Gears · Actor.Agent (17 agents)</text>
    <text class="sub" x="740" y="56" text-anchor="end">describe → specify → verify → build</text>
  </g>
  <g class="layer">
    <rect class="box" x="40" y="100" width="355" height="60" rx="3"/>
    <text class="label" x="60" y="125">Genesis</text>
    <text class="sub" x="60" y="146">compiler workbench · TLA+ · algebra</text>
    <rect class="box" x="405" y="100" width="355" height="60" rx="3"/>
    <text class="label" x="425" y="125">Aleph</text>
    <text class="sub" x="425" y="146">language · native FFI · v1.2.0</text>
  </g>
  <g class="layer">
    <rect class="box" x="40" y="180" width="230" height="60" rx="3"/>
    <text class="label" x="60" y="205">MLambda.Actors</text>
    <text class="sub" x="60" y="226">runtime · clustering · mTLS</text>
    <rect class="box" x="285" y="180" width="230" height="60" rx="3"/>
    <text class="label" x="305" y="205">MLambda.Data</text>
    <text class="sub" x="305" y="226">actor-native database · TLA+</text>
    <rect class="box" x="530" y="180" width="230" height="60" rx="3"/>
    <text class="label" x="550" y="205">MLambda.UI</text>
    <text class="sub" x="550" y="226">reactive MVVM · 3 backends</text>
  </g>
  <g class="layer">
    <rect class="box" x="40" y="260" width="720" height="50" rx="3"/>
    <text class="label" x="60" y="285">MLambda.OS</text>
    <text class="sub" x="60" y="302">x86-64 microkernel · specified first</text>
  </g>
  <g class="layer">
    <rect class="box" x="40" y="330" width="720" height="50" rx="3"/>
    <text class="label" x="60" y="355">Intelligence</text>
    <text class="sub" x="60" y="372">Hilbert neuro-symbolic transformer · Thinker: the LLM never answers, only proofs do</text>
  </g>
</svg>
```

- [ ] **Step 4: Write `index.md`**

```markdown
---
layout: home
title: MLambda
description: MLambda builds the stack for software that is verified before it is built — a compiler workbench, a language, an actor runtime, a distributed database, and an agentic factory.
---

<section class="hero">
  <h1>Software that is verified before it is built.</h1>
  <p class="hero__lede">MLambda builds the stack for correct-by-construction systems: a compiler
  workbench that model-checks a specification before anything is generated from it, a
  language that reaches the machine directly, an actor runtime and a database built out of
  actors, a UI framework, a research microkernel, and neuro-symbolic AI.</p>
  <p class="hero__lede">On top of them sits the Factory — a society of LLM agents that turns a
  plain-language description into a formal specification, verifies it, and generates the
  tested, deployable system that follows. The language model acquires; rules admit; proofs
  decide.</p>
  <p class="hero__lede">Two tiers, stated on every page: <span class="tier tier--open">Open · MIT</span>
  on NuGet with public documentation, and <span class="tier tier--commercial">Commercial · early access</span>
  with public documentation and source by arrangement.</p>
</section>

<h2>The stack</h2>
<div class="diagram">{% include stack-diagram.svg %}</div>

<h2>Products</h2>
{% assign all = site.products | sort: "weight" %}
<ul class="grid-cards">
{% for product in all %}{% include product-card.html product=product %}{% endfor %}
</ul>

<h2>Method</h2>
<p class="lede">Every system here is specified in Z, model-checked in TLA+, and only then
implemented — by people or by agents — with the tests derived from the model rather than
invented afterwards. <a href="{{ '/method/' | relative_url }}">How MLambda builds software →</a></p>

<h2>Work with MLambda</h2>
<ul>
  <li><strong>Consulting</strong> — architecture and delivery with the MLambda stack.</li>
  <li><strong>Commercial licence and support</strong> — for the commercial-tier products and supported use of the open ones.</li>
  <li><strong>Early access</strong> — private builds and repositories for teams evaluating the commercial tier.</li>
</ul>
<p><a class="btn" href="{{ '/services/' | relative_url }}">Services</a></p>
```

- [ ] **Step 5: Run the check to verify it passes** — `./script/check` → `0 failed`.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat: home page with the stack diagram

Inline SVG keyed to the theme tokens so it renders in both colour
schemes, the product grid, and the three engagement paths."
```

---

## Task 6: Method page with the pipeline diagram

**Files:**
- Create: `_includes/pipeline-diagram.svg`, `method.md`
- Modify: `script/check`

- [ ] **Step 1: Add the failing assertions**

```bash
assert_file "method/index.html"
assert_contains "method/index.html" "<svg"
assert_contains "method/index.html" "TLA+"
assert_contains "method/index.html" "17 specialised agents"
assert_contains "method/index.html" "only proofs do"
assert_contains "method/index.html" "genesis.mlambda.net"
```

- [ ] **Step 2: Run the check to verify it fails** — `./script/check` → 6 FAIL lines.

- [ ] **Step 3: Write `_includes/pipeline-diagram.svg`**

```html
<svg viewBox="0 0 800 300" role="img" aria-labelledby="pipe-t pipe-d" xmlns="http://www.w3.org/2000/svg">
  <title id="pipe-t">The BEAM pipeline</title>
  <desc id="pipe-d">Ten stages in two rows: research, conceptualise, formalise in Z, verify in TLA+, plan; then generate, test with BDD, benchmark, deploy, and verify again — with evidence returning to the start.</desc>
  <defs>
    <marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path class="arrowhead" d="M 0 0 L 10 5 L 0 10 z"/>
    </marker>
  </defs>
  <g>
    <rect class="box" x="20" y="40" width="130" height="56" rx="3"/><text class="label" x="85" y="64" text-anchor="middle">Research</text><text class="sub" x="85" y="84" text-anchor="middle">domain graph</text>
    <rect class="box" x="175" y="40" width="130" height="56" rx="3"/><text class="label" x="240" y="64" text-anchor="middle">Conceptualise</text><text class="sub" x="240" y="84" text-anchor="middle">actor topology</text>
    <rect class="box box--accent" x="330" y="40" width="130" height="56" rx="3"/><text class="label" x="395" y="64" text-anchor="middle">Formalise</text><text class="sub" x="395" y="84" text-anchor="middle">Z specification</text>
    <rect class="box box--accent" x="485" y="40" width="130" height="56" rx="3"/><text class="label" x="550" y="64" text-anchor="middle">Verify</text><text class="sub" x="550" y="84" text-anchor="middle">TLA+ · TLC</text>
    <rect class="box" x="640" y="40" width="140" height="56" rx="3"/><text class="label" x="710" y="64" text-anchor="middle">Plan</text><text class="sub" x="710" y="84" text-anchor="middle">five artifact plans</text>
    <path class="arrow" d="M150 68 H175" marker-end="url(#ah)"/>
    <path class="arrow" d="M305 68 H330" marker-end="url(#ah)"/>
    <path class="arrow" d="M460 68 H485" marker-end="url(#ah)"/>
    <path class="arrow" d="M615 68 H640" marker-end="url(#ah)"/>
  </g>
  <g>
    <rect class="box" x="20" y="180" width="130" height="56" rx="3"/><text class="label" x="85" y="204" text-anchor="middle">Generate</text><text class="sub" x="85" y="224" text-anchor="middle">actors · data · UI</text>
    <rect class="box" x="175" y="180" width="130" height="56" rx="3"/><text class="label" x="240" y="204" text-anchor="middle">Test</text><text class="sub" x="240" y="224" text-anchor="middle">BDD from the model</text>
    <rect class="box" x="330" y="180" width="130" height="56" rx="3"/><text class="label" x="395" y="204" text-anchor="middle">Benchmark</text><text class="sub" x="395" y="224" text-anchor="middle">throughput · latency</text>
    <rect class="box" x="485" y="180" width="130" height="56" rx="3"/><text class="label" x="550" y="204" text-anchor="middle">Deploy</text><text class="sub" x="550" y="224" text-anchor="middle">Helm · Kubernetes</text>
    <rect class="box box--accent" x="640" y="180" width="140" height="56" rx="3"/><text class="label" x="710" y="204" text-anchor="middle">Measure</text><text class="sub" x="710" y="224" text-anchor="middle">evidence → gap list</text>
    <path class="arrow" d="M150 208 H175" marker-end="url(#ah)"/>
    <path class="arrow" d="M305 208 H330" marker-end="url(#ah)"/>
    <path class="arrow" d="M460 208 H485" marker-end="url(#ah)"/>
    <path class="arrow" d="M615 208 H640" marker-end="url(#ah)"/>
  </g>
  <path class="arrow" d="M710 96 V140 H85 V180" marker-end="url(#ah)"/>
  <path class="arrow" d="M710 236 V270 H10 V68 H20" marker-end="url(#ah)"/>
  <text class="sub" x="400" y="266" text-anchor="middle">measurements return to research — the cycle repeats</text>
</svg>
```

- [ ] **Step 4: Write `method.md`**

```markdown
---
layout: page
title: How MLambda builds software
subtitle: Specified in Z, checked in TLA+, and only then built — by people or by agents — with the tests derived from the model.
description: The BEAM method and the agentic pipeline behind every MLambda system — formal specification, model checking, generation, derived tests, and measured deployment.
permalink: /method/
wide: true
---

<div class="prose">
<p>Most software is built first and tested afterwards, and the tests are whatever someone
thought to write. Everything at MLambda inverts that. A system exists first as a formal
specification; the specification is model-checked; the implementation follows from it; and
the tests are obligations derived from the model, not guesses about it.</p>
</div>

<h2>The pipeline</h2>
<div class="diagram">{% include pipeline-diagram.svg %}</div>

<div class="prose">
<p><strong>Research</strong> decomposes a business domain into a knowledge graph of processes,
events, data flows, decisions and human roles. <strong>Conceptualisation</strong> turns that
into an actor topology with an explicit supervision hierarchy, human boundaries and interface
surfaces. <strong>Formation</strong> refines colloquial requirements into a purified Z
specification. <strong>Verification</strong> generates an executable TLA+ specification from it
and runs the TLC model checker until every safety, liveness and temporal property holds —
correction loops go back to Formation, not forward to code. <strong>Planning</strong> derives
five artifact plans — mobile UI, web UI, API gateway, backend, infrastructure. Only then:
generation, BDD tests derived from the model, benchmarks, deployment, and measurement whose
evidence returns to the research gap list.</p>

<h2>Four claims the method rests on</h2>

<ul>
  <li><strong>A missing requirement is an unfulfilled obligation</strong> — deduced from the knowledge base, not guessed by a model.</li>
  <li><strong>A waiver is a belief, and closes nothing</strong> until a scope statement a person wrote grounds it.</li>
  <li><strong>The aggregation is derivable</strong>: an invariant spanning two entities forces them into one aggregate, so the connected components of the invariant graph <em>are</em> the aggregates.</li>
  <li><strong>Design estimates, verification measures</strong>, and the difference between them is what the method learns.</li>
</ul>

<h2>The agentic layer</h2>

<p>The pipeline is run by agents. In the Factory, <strong>Turing</strong> hosts a society of
agents — a roster, expert agents, code agents — coordinated by <strong>Gears</strong>, a build
engine that drives declared workflows and writes each agent's report. As a Claude Code
plugin, <strong>MLambda.Actor.Agent</strong> runs the same method with 17 specialised agents,
one per stage, from a business description to an actor system deployed on Kubernetes.</p>

<p>What keeps an LLM-driven pipeline honest is the reasoning layer, <strong>Thinker</strong>.
Language models acquire content — through pluggable providers and retrieval — and a
deterministic grammar formalises what they propose. A forward-chaining engine proves over
the formalised knowledge, a proof kernel re-checks every proof, and a symbolic reinforcement
learner improves what is believed over time. <strong>The LLM never answers; only proofs do.</strong>
The method borrows TOGAF for what exists, Gilb's Planguage for what must hold, and reactive
domain-driven design for what to build.</p>

<p>The full method is documented in the twelve-chapter method book on
<a href="https://genesis.mlambda.net">genesis.mlambda.net</a>.</p>
</div>
```

- [ ] **Step 5: Run the check to verify it passes** — `./script/check` → `0 failed`.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat: method page with the BEAM pipeline diagram

Formal specification and model checking before construction, the four
claims the method rests on, and the agentic layer: Turing's society,
Gears, the 17 Actor.Agent agents, and Thinker's rule."
```

---

## Task 7: Services page

**Files:**
- Create: `_data/services.yml`, `services.md`
- Modify: `script/check`

- [ ] **Step 1: Add the failing assertions**

```bash
assert_file "services/index.html"
assert_contains "services/index.html" 'id="consulting"'
assert_contains "services/index.html" 'id="commercial-licence-and-support"'
assert_contains "services/index.html" 'id="early-access"'
assert_contains "services/index.html" "roy.gonzalez@mlambda.net"
```

- [ ] **Step 2: Run the check to verify it fails** — `./script/check` → 5 FAIL lines.

- [ ] **Step 3: Write `_data/services.yml`**

```yaml
engagements:
  - id: consulting
    name: Consulting
    summary: >-
      Architecture and delivery with the MLambda stack, for teams that need a system to be
      correct rather than merely shipped.
    includes:
      - Actor-model and reactive system design on MLambda.Actors
      - Distributed data on MLambda.Data, or specification-first design of your own store
      - Formal specification in Z and model checking in TLA+ for the parts that must not fail
      - Language and compiler tooling on Genesis — domain languages, parsers, generators
    start: Write with a description of the system and its hardest invariant.

  - id: commercial-licence-and-support
    name: Commercial licence and support
    summary: >-
      For the commercial-tier products — Data, Aleph, UI, OS and the Factory — and for
      supported use of the open ones.
    includes:
      - A licence for the product and its updates
      - A support channel with a named engineer
      - Upgrade guidance across versions
      - Priority on defects that affect your deployment
    start: Write with the product, the deployment topology, and the timeline.

  - id: early-access
    name: Early access
    summary: >-
      Access to private builds and repositories for teams evaluating the commercial tier
      before committing to it.
    includes:
      - Builds and source for the product under evaluation
      - Direct contact with the engineer who built it
      - A defined evaluation window and exit criteria
      - The option to convert to a commercial licence
    start: Write with the product you want to evaluate and what you intend to build with it.
```

- [ ] **Step 4: Write `services.md`**

```markdown
---
layout: page
title: Work with MLambda
subtitle: Three ways to engage. Terms are agreed per engagement.
description: Consulting, commercial licence and support, and early access to the MLambda stack.
permalink: /services/
wide: true
---

<ul class="services">
{% for e in site.data.services.engagements %}
  <li class="service" id="{{ e.id }}">
    <h2 class="service__name">{{ e.name }}</h2>
    <p>{{ e.summary }}</p>
    <ul>{% for i in e.includes %}<li>{{ i }}</li>{% endfor %}</ul>
    <p class="muted">{{ e.start }}</p>
    <p><a class="btn" href="mailto:{{ site.data.company.email }}?subject={{ e.name | uri_escape }}">{{ site.data.company.email }}</a></p>
  </li>
{% endfor %}
</ul>
```

- [ ] **Step 5: Run the check to verify it passes** — `./script/check` → `0 failed`. Also `./script/check --links` → every URL 200.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat: services page

Consulting, commercial licence and support, early access — the three
engagements confirmed on offer. No figures; terms per engagement."
```

---

## Task 8: Sitemap and SEO assertions, push, deploy, verify the domain

**Files:**
- Modify: `script/check`

- [ ] **Step 1: Add the final assertions**

```bash
assert_file "sitemap.xml"
for r in products method services about products/factory products/genesis products/aleph products/actors products/data products/ui products/os products/hilbert; do assert_contains "sitemap.xml" "/$r/"; done
assert_contains "index.html" "og:title"
assert_contains "products/genesis/index.html" "og:description"
```

- [ ] **Step 2: Run the check** — `./script/check` → `0 failed` (these should pass already; if not, fix `_config.yml` rather than the assertion).

- [ ] **Step 3: Commit and push**

```bash
git add -A
git commit -m "test: assert the sitemap lists every route"
git push origin main
```

- [ ] **Step 4: Watch the deploy and verify the live site**

```bash
ID=$(gh run list --limit 1 --json databaseId --jq '.[0].databaseId'); gh run watch "$ID" --exit-status
for p in "" products/ products/genesis/ method/ services/ about/; do printf "%s  /%s\n" "$(curl -s -o /dev/null -w '%{http_code}' https://www.mlambda.net/$p)" "$p"; done
curl -s https://www.mlambda.net/ | grep -c "verified before it is built"
gh api repos/mlambda-net/mlambda-net.github.io/pages --jq .cname     # expected: www.mlambda.net
./script/check --links
```

Expected: run `success`; every route 200; the phrase count ≥ 1; cname unchanged; `--links` `0 failed`.

---

## Follow-up work, not in this plan

1. GitHub org profile README — create the `mlambda-net/.github` repository with `profile/README.md`.
2. `PackageLicenseExpression` metadata on the NuGet packages (they declare no licence today).
3. An Aleph documentation site; the README installer URLs 404.
4. The legal entity name in `_data/company.yml` when the user supplies it.
