# Archive: Squarespace status pipeline

This folder preserves the previous setup that generated a service status table for embedding in Squarespace:

- **getstatus.py** — checked OVRO-LWA and DSA-110 services and wrote `status/*.md`
- **blank.yml** — GitHub Actions workflow that concatenated markdown and rendered `status/include.html`
- **status/** — generated markdown and HTML used by Squarespace

The live site has been migrated to a static GitHub Pages site in the repo root `docs/` folder.
