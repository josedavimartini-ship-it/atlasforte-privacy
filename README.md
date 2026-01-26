# AtlasForte Privacy & Support Utilities

This repository contains the public privacy policy page for AtlasForteFinanceiro (AFF) and a set of supporting scripts/docs used to help with Play Console submission, CI smoke tests, and utility tasks.

Privacy page (quick):

- This repo can host a privacy page using GitHub Pages. Publish by setting the repository Pages source to `main` / root (Settings → Pages) and enabling HTTPS.

- To set up locally:

  ```bash
  git init
  git add privacy.html README.md
  git commit -m "Add public privacy page for AtlasForte"
  git branch -M main
  git remote add origin git@github.com:your-username/atlasforte-privacy.git
  git push -u origin main
  ```

- Use the resulting Pages URL for Play Console → App content → Privacy policy.

If you prefer I can create the repo and enable Pages for you if you provide a GitHub Personal Access Token (scopes: repo, pages).

Support utilities in this repository:

- `PLAY_DATA_SAFETY.md` — suggested copy for Play Console "Data safety" form.
- `PLAY_APP_ACCESS.md` — instructions for Google Sign-in and a quick smoke test note.
- `flutter_google_signin_snippet.md` — a minimal UI snippet to add a Google Sign-in button to `main.dart`.
- `tests/smoke_oauth_google.py` — a smoke test that posts an invalid id_token to the server to verify the server rejects invalid tokens.
- `.github/workflows/smoke-oauth.yml` — GitHub Actions workflow to run the smoke test on push or on manual dispatch.

How to run the smoke test locally:

```bash
API_BASE=http://localhost:5000 python tests/smoke_oauth_google.py
```

If you'd like, I can also open a PR in the Flutter client repository (or in this repo if it contains the Flutter app) that inserts the sign-in button into the login screen and wires the helper directly. Let me know which repo/path to target.

