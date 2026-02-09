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
3. Set **Branch** to `main`, folder to **/docs**, then save.
4. **Custom domain:** Under **Custom domain**, enter `salab.caltech.edu`, then **Save**. Optionally enable **Enforce HTTPS** after DNS has propagated.

The site will be available at **https://salab.caltech.edu** once DNS is configured.

### DNS (at Caltech)

Add a **CNAME** record so the custom domain points to GitHub Pages:

| Type  | Name  | Value                 |
|-------|-------|------------------------|
| CNAME | salab | ovrocaltech.github.io  |

(If `salab` is the full hostname in your DNS UI, use `salab.caltech.edu` as Name, or whatever your DNS provider expects for the subdomain.)

After saving DNS, wait for propagation (minutes to hours). GitHub will then serve the site at https://salab.caltech.edu and you can turn on **Enforce HTTPS** in Settings → Pages.

## Archive

The previous Squarespace-oriented pipeline (status table generator and workflow) is preserved in [archive/squarespace-status/](archive/squarespace-status/).
