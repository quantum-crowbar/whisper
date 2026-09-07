# docs

Design docs and notes. The master specification is [../specs.md](../specs.md).

- [roadmap.md](roadmap.md) — phases, dependencies, critical path, blockers, milestones
- [index.html](index.html) — the devlog site (entries live here)
- [devlog/](devlog/) — how to add an entry, plus the photo assets

## Devlog site

Plain static HTML — one page, one stylesheet, no build step and no toolchain. Open
`docs/index.html` in a browser to preview it exactly as it will be served.

Published by GitHub Pages at <https://quantum-crowbar.github.io/whisper/>, built by
[`.github/workflows/pages.yml`](../.github/workflows/pages.yml) on every push that touches
`docs/`. Set **Settings → Pages → Source: GitHub Actions**.

Not "Deploy from a branch" — that flow always checks out submodules, and `quantum-basics`
is private, so the Pages builder can't clone it and the checkout fails before the site is
ever built. The workflow passes `submodules: false`, which the devlog doesn't need anyway.

The empty `.nojekyll` file stops the files being run through Jekyll.

## Open questions
- CAD tool preference for the enclosure
- Whether the mic needs a felt/mesh dust cover behind its acoustic port
- Exact SD reader module footprint vs. final case dimensions
