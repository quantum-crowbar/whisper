# Devlog

Running log of development — hardware bring-up photos, bench-test results, firmware
notes, dead ends, decisions. Newest entries at the top.

Photos live in [assets/](assets/); reference them with relative paths so they render on
GitHub.

## How to add an entry

Copy the template, fill it in, drop any photos in `assets/` named
`YYYY-MM-DD-short-name.jpg`, and add newest-first under the log.

```markdown
## YYYY-MM-DD — <short title>

**Phase:** <0–5 / which>  ·  **Status:** <what changed>

<A few sentences: what you did, what worked, what didn't, next step.>

![caption](assets/YYYY-MM-DD-name.jpg)
```

Keep entries short. This is a log, not a report — a couple of sentences and a photo is plenty.

---

## Log

## 2026-08-08 — Repo bootstrapped

**Phase:** 0–1 · **Status:** docs/scaffolding only, no hardware work logged yet

Set up the repo from the spec: firmware/android/hardware/docs scaffold, pinout, BOM,
roadmap, and agent docs. quantum-basics attached as a submodule. No soldering or
bench-testing done yet — puck parts are in hand except the microSD card and LiPo
(pending purchase). First hardware entry will land once headers are soldered and the
mic/OLED/button bench-test runs.

<!-- Add new entries above this line, newest first. -->
