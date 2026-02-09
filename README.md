# salwww

Static website for **OVRO SAL** (Software & Algorithms Lab), hosted on GitHub Pages. The site highlights three telescopes: OVRO-LWA, DSA-110, and the Deep Synoptic Array (DSA).

## Site content

- **Landing:** [docs/index.html](docs/index.html) — intro, software topics, and telescope cards.
- **Telescope pages:** [docs/telescopes/](docs/telescopes/) — `ovro-lwa.html`, `dsa-110.html`, `dsa.html`.
- **Assets:** [docs/assets/](docs/assets/) — `site.css`, [docs/assets/images/](docs/assets/images/) for telescope images.
- **404:** [docs/404.html](docs/404.html) — custom not-found page (when GitHub Pages supports it).

All content is plain HTML and CSS; no build step.

## Preview locally

Open the site from the repo root:

```bash
# From repo root: open docs/index.html in your browser
open docs/index.html
```

Or serve the `docs/` folder with any static server, e.g.:

```bash
python3 -m http.server 8000 --directory docs
# Then visit http://localhost:8000
```

## Updating the site

- **Text:** Edit the HTML files in `docs/` and `docs/telescopes/`.
- **Styles:** Edit [docs/assets/site.css](docs/assets/site.css).
- **Images:** Replace or add files in `docs/assets/images/` and update the corresponding `src` and `alt` in the HTML.

## GitHub Pages setup

1. In the repo: **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
3. Set **Branch** to `main`, folder to **/ (root)**, then choose **/docs**.
4. Save. The site will be published at `https://<owner>.github.io/salwww/`.

(If the repo is in an organization, replace `<owner>` with the org name.)

## Archive

The previous Squarespace-oriented pipeline (status table generator and workflow) is preserved in [archive/squarespace-status/](archive/squarespace-status/).
