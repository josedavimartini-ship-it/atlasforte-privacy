AtlasForte Privacy Page

This repository contains the public privacy policy page for AtlasForteFinanceiro (AFF).

How to publish (quick):

1) (Recommended) Create repository on GitHub (public):
   - Name: `atlasforte-privacy` (or similar)
   - Public visibility

2) Locally push these files to the new repo:
   - git init
   - git add privacy.html README.md
   - git commit -m "Add public privacy page for AtlasForte"
   - git branch -M main
   - git remote add origin git@github.com:<your-username>/atlasforte-privacy.git
   - git push -u origin main

3) Enable GitHub Pages:
   - Repo → Settings → Pages → Source: **main** / **root** (or /docs if you prefer)
   - Save and wait for the URL to appear (enable "Enforce HTTPS" when available).

4) Use the resulting URL for Play Console → App content → Privacy policy.

If you prefer I can create the repo and enable Pages for you if you provide a GitHub Personal Access Token (scopes: repo, pages).
