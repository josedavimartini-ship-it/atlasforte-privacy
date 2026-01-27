# Play Release checklist — AtlasForteFinanceiro

Use this checklist to prepare the Play Console listing and ensure compliance.

- [ ] Privacy policy published and URL available in Play Console
- [ ] Data Safety form completed (copy in `PLAY_DATA_SAFETY.md`)
- [ ] Account deletion URL published and reachable (`/apps/atlasfortefinanceiro/account/delete`)
- [ ] Google OAuth consent screen configured (verified email, scopes, test users if necessary)
- [ ] App access items filled (OAuth items, account deletion URL, support email)
- [ ] Ads settings reviewed (AdMob account linked, ad personalization settings clarified)
- [ ] Play Store listing assets (screenshots, contact email, privacy policy URL) ready
- [ ] E2E smoke tests run on deployed environment (run `smoke-oauth.yml` workflow or manual test)

Notes:

- If Google Sign-in is enabled, ensure the OAuth Client ID and SHA-1 fingerprints match the built app.

- Keep `PLAY_DATA_SAFETY.md` and `PLAY_APP_ACCESS.md` updated as you add or remove data collection or third-party SDKs.

