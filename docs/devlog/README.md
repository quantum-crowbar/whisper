# Devlog

Running log of development — hardware bring-up photos, bench-test results, firmware
notes, dead ends, decisions.

**The entries live in [`../index.html`](../index.html)** and are published at
<https://quantum-crowbar.github.io/whisper/>. They used to be appended to this file; they
were moved so the site and the repo don't hold two copies that drift apart.

Photos stay in [assets/](assets/), named `YYYY-MM-DD-short-name.jpg`.

## Prepping a photo

Phone photos come off the camera at 4000×3000 and ~4 MB, with an EXIF orientation flag
instead of actual rotation. Neither is usable as-is: the page column is ~700 px wide, and a
browser honours the EXIF flag, so a "4000×3000" file actually renders 3000×4000 and any
`width`/`height` you copy off the file is inverted.

Each photo goes in at **two sizes**:

| | long edge | where | why |
|---|---|---|---|
| inline | 1600 px | `assets/` | what the page loads — 2× the ~550 px column |
| full | 2400 px | `assets/full/` | click-through, only fetched on demand |

Same filename in both directories. Run both:

```sh
N=YYYY-MM-DD-short-name
convert IN.jpg -auto-orient -resize '1600x1600>' -strip \
        -interlace Plane -sampling-factor 4:2:0 -quality 82 "assets/$N.jpg"
convert IN.jpg -auto-orient -resize '2400x2400>' -strip \
        -interlace Plane -quality 82 "assets/full/$N.jpg"
```

`-auto-orient` bakes the rotation into the pixels, `-strip` then drops the EXIF (including
the GPS tags, which otherwise geolocate the bench on a public site).

The two tiers exist because 1600 px is right for the page but too small to read silkscreen —
component labels and pin markings turn to mush. 2400 px recovers them, and is close enough
to a 4000 px original that the original adds nothing for handheld shots. Inline is ~300 KB,
full is ~600–800 KB.

## How to add an entry

Prep the photos into `assets/` as above, then paste one `<article>` block into
`../index.html` directly under the `newest entry goes directly below this line` comment.
Newest first.

```html
<article id="YYYY-MM-DD">
  <h2><a href="#YYYY-MM-DD">Short title</a></h2>
  <p class="meta"><span class="d">YYYY-MM-DD</span> · <span class="k">phase</span> 0 · <span class="k">status</span> what changed</p>

  <p>A few sentences: what you did, what worked, what didn't, next step.</p>

  <a class="shot" href="devlog/assets/full/YYYY-MM-DD-name.jpg">
    <img src="devlog/assets/YYYY-MM-DD-name.jpg" width="1200" height="1600" loading="lazy" decoding="async"
         alt="caption">
  </a>
</article>
```

Note the paths are relative to `index.html`, so they start with `devlog/`, not `assets/`.
The `a.shot` wrapper is what makes the photo click through to the larger copy; without the
class it picks up the global link styling and gets underlined in purple.
The `width`/`height` are the prepped photo's real pixel dimensions — they stop the page
jumping around while images load, so they have to match. Read them off the prepped file,
never the original: `identify -format '%wx%h' assets/whatever.jpg`.

Keep entries short. This is a log, not a report — a couple of sentences and a photo is plenty.

## Previewing

Open `docs/index.html` in a browser. There is no build step.
