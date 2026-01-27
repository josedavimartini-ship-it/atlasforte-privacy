# Play Console Submission Checklist — AtlasForteFinanceiro

Use this checklist to finish Play Console fields quickly. Each section includes exact copy you can paste into the Play Console form.

1. App details & assets

- App name, short/long description, screenshots (phone/tablet), contact email: **[davimartini@gmail.com](mailto:davimartini@gmail.com)**, privacy policy: [privacy policy](https://planilha-financeira-fam-lia-davi-martini.onrender.com/privacy)

1. Data Safety form — copy/paste

- Data collection & security: "All network traffic is encrypted with TLS. Personal and financial data are stored securely on our backend."
- Data types: Paste from `PLAY_DATA_SAFETY.md` (Personal info, Financial info, Payment info, Device identifiers, App telemetry, User uploads).
- Per-type short descriptions: Paste the per-type snippets from `PLAY_DATA_SAFETY.md`.
- Retention: "Active personal & financial data deleted within 30 days after verified request. Backups up to 90 days; logs/anonymized records up to 180 days."
- Delete URLs: Use account delete: [Account delete](https://planilha-financeira-fam-lia-davi-martini.onrender.com/account/delete) and data delete: [Data delete](https://planilha-financeira-fam-lia-davi-martini.onrender.com/apps/atlasfortefinanceiro/account/delete)
- Support: `davimartini@gmail.com`
- Reviewer note: "Payments use Stripe Checkout (PCI-compliant). Card numbers are not stored by our servers. Contact [davimartini@gmail.com](mailto:davimartini@gmail.com) for verification."

1. App access / OAuth

- OAuth client: ensure OAuth consent screen configured (verified email) and that Google Sign-in client ID SHA-1(s) match the built app.
- Test accounts: add test users to the OAuth consent screen if the app is restricted.

1. Ads & Monetization

- Ensure AdMob integration is configured and ad personalization settings are set as you prefer.
- If advertising ID used, mark it in Data Safety and include Google/AdMob as recipients.

1. Final checks

- Confirm deletion page is reachable and content matches the Delete URL. (Already deployed and reachable.)
- Run the `smoke-oauth` workflow manually (Actions → Smoke test — OAuth endpoint → Run workflow) to validate the OAuth endpoint is reachable and rejects invalid tokens.

1. Release

- Build signed release AAB/AAB bundle and upload to Play Console Release (internal test track first). Use Play Console's internal testing to validate flows before publishing to production.

If you'd like, I can perform any of these steps for you (start scheduled smoke run, prepare Flutter PR, or produce release artifacts).

