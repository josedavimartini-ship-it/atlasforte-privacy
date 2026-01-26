# Release tracker — AtlasForteFinanceiro

This file tracks the remaining tasks to finish Play Console submission and launch the app. Use it to mark items done and add notes.

## High priority

- [ ] Paste the one-paste block from `PLAY_DATA_SAFETY.md` into the Play Console Data Safety form and run the console checks. (Assigned: @davimartini)
- [ ] Set Play Console Delete URLs to:

  - Account deletion: [Account delete](https://planilha-financeira-fam-lia-davi-martini.onrender.com/account/delete)
  - Data deletion: [Data delete](https://planilha-financeira-fam-lia-davi-martini.onrender.com/apps/atlasfortefinanceiro/account/delete)
  - Support: `davimartini@gmail.com`
- [ ] Upload signed app bundle (AAB) to an Internal Test track and verify OAuth flows (Google Sign‑in) with test users.

## Medium priority

- [ ] Apply the Flutter Google Sign-in patch to the Flutter app repo and open a PR (branch: `feature/google-signin`).
- [ ] Verify sign-in flows on device for both email/password and Google Sign-in; confirm `/api/oauth/google` exchanges ID token for app token.

## Low priority

- [ ] Remove or further restrict the `/__routes` diagnostic endpoint when no longer required.
- [ ] Add additional E2E tests that exercise the full purchase + webhook flow (advertiser checkout) as CI tests.

## Notes & context

- The repo contains `PLAY_DATA_SAFETY.md` and `static/play_data_safety_details.html` with exact copy snippets for the Play Console.
- A daily `smoke-oauth` workflow runs to verify the server rejects invalid Google ID tokens.

If you'd like, I can open a GitHub Issue for each high-priority task and assign it to you, or directly open the Flutter PR if you give me the repo/branch to target.
