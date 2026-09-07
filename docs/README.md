# docs

Design docs and notes. The master specification is [../specs.md](../specs.md).

- [roadmap.md](roadmap.md) — phases, dependencies, critical path, blockers, milestones
- [index.html](index.html) — the devlog site (entries live here)
- [devlog/](devlog/) — how to add an entry, plus the photo assets

## Devlog site

Plain static HTML — one page, one stylesheet, no build step and no toolchain. Open
`docs/index.html` in a browser to preview it exactly as it will be served.

Published by GitHub Pages at <https://quantum-crowbar.github.io/whisper/>. Enable it under
**Settings → Pages → Source: Deploy from a branch → `main` → `/docs`**. The empty
`.nojekyll` file stops Pages running the files through Jekyll.

## Open questions
- CAD tool preference for the enclosure
- Whether the mic needs a felt/mesh dust cover behind its acoustic port
- Exact SD reader module footprint vs. final case dimensions
