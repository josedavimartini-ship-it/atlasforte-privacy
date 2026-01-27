# Play Data Safety — AtlasForteFinanceiro

This file contains suggested Play Console "Data safety" answers and copy you can paste into the Play Console.

---

App: AtlasForteFinanceiro (mobile app / planilha financeira)

Data collection summary (high-level):

- We collect **Personal information** (email, display name), **Financial data** (budgets, transactions, user-entered bank connection metadata), **Device & usage data** (diagnostics and analytics), and **Advertising identifiers** for showing AdMob ads to free users.
- Purpose: app functionality (account, budgets, transactions), analytics & diagnostics, and advertising.
- Data is transmitted over TLS and stored securely on our backend. Users may request deletion; an account deletion page is public and deletion/anonymization is performed via the server endpoint and documented in the privacy policy.

---

Suggested Play Console answers (copy/paste)

## 1) Does your app collect or share any of the following user data? Select all that apply

- Personal info (Email, name)
- Financial info (Bank account metadata, budgets, transactions)
- Device or other identifiers (device identifiers, advertising ID)
- App info and performance (analytics, crash reports)
- Advertising ID and ad-related data

## 2) Purposes for data collection (for each selected category)

- Personal info: Account creation, authentication and user profile. Data source: User. Shared with third parties: No (except when user signs in with Google and limited profile info is provided by Google as part of sign-in).
- Financial info: Core app functionality (budgets, transactions, bank connection metadata). Data source: User and integrated services. Shared with third parties: No.
- Device or other identifiers: App performance, analytics, and ad personalization. Data source: Device. Shared with third parties: Yes (Google services for analytics/ads when using Google SDKs).
- App info & performance: Crash reports and analytics for product improvement. Data source: Device. Shared with third parties: Yes (Google Analytics / crash reporting SDKs if enabled).
- Advertising ID & ad-related data: Used by AdMob to serve and personalize ads for free-tier users. Data source: Device/Ad SDK. Shared with third parties: Yes (Google / AdMob).

## 3) Is any of the data shared with third parties? If yes, provide details

- Yes. We use Google services (AdMob and analytics) which may receive device identifiers, ad-related signals, and aggregated usage data. We do not sell personal data.

## 4) Data retention policy & deletion

- Users can request deletion via the public account deletion page: [Account deletion page](https://planilha-financeira-fam-lia-davi-martini.onrender.com/apps/atlasfortefinanceiro/account/delete) (static page). When an authenticated user requests deletion via `POST /api/account/delete`, personal and financial data are deleted or anonymized as documented in the privacy policy. Backups may be retained briefly and purged according to retention policy; no personal data is kept longer than necessary for operations or legal obligations.

## 5) Security & encryption

- All network communication uses TLS. Sensitive data stored in the backend is treated per best-practices. For Play Console, indicate that TLS is used for data in transit.

## 6) Contact & privacy policy

- Provide your privacy policy URL in the Play Console. We also document account deletion and data practices in the repo (`atlasforte-privacy/README.md`) and the static account deletion page linked above.

---

Notes & next steps:

- Verify the exact host URL you will use in Play Console (the sample above is the Render deployment). Replace it with your production domain if different.

- If you use additional third-party SDKs (analytics providers, crash reporters), include them and list the exact categories of data they receive in the Play Console questionnaire.

If you'd like, I can also open a small PR that updates the static privacy page with explicit Data Safety copy and a short checklist of Play Console answers ready to paste. ✅

---

Quick copy/paste block for Play Console (short snippets):

Personal info:
Collected: email, display name. Purpose: account and authentication. Shared: only with Google when using Google Sign-in; not sold.

Financial info:
Collected: budgets, transactions, bank connection metadata. Purpose: core app functionality. Shared: no.

Payment info:
Collected/transmitted during Stripe Checkout. Card details are handled by Stripe and are not stored by our servers.

Device & identifiers:
Collected: device identifiers and Advertising ID. Purpose: analytics and ad personalization. Shared: Google (AdMob, Analytics).

App telemetry:
Collected: crash reports and analytics for product improvement. Shared: Google (Analytics/Crash) if enabled.

Photos:
Collected: user-captured photos (e.g., receipts) used for OCR and bookkeeping. Purpose: extract transaction data (OCR) and attach receipts to the user account. Shared: Yes — images may be processed by a third-party OCR provider (e.g., Google Cloud Vision) for automatic reading and extraction; images are not sold. Processed ephemerally: No — images are persisted in the user account unless deleted by the user.

User uploads:
Collected: receipts and documents (camera or file uploads). Purpose: bookkeeping and OCR. Shared: Yes — see Photos/OCR above for details.

Retention:
Personal & financial data deleted within 30 days after verified request. Backups may be retained up to 90 days; logs/anonymized records up to 180 days.

Full details & editable copy snippets are available at:
[Data Safety details](https://planilha-financeira-fam-lia-davi-martini.onrender.com/static/play_data_safety_details.html)

Support contact: [davimartini@gmail.com](mailto:davimartini@gmail.com)

(Replace support email placeholders with your real support email before submitting.)

---

Per-field snippets (copy/paste)

Name:
Collected: Yes. Shared: No. Processed ephemerally: No. Required: Optional (users can choose whether to provide a display name).
Why collected: App functionality, Account management, Personalisation (optional).
Why shared: Not shared except when provided via Google OAuth (shared with Google only when user signs in via Google).

Email address:
Collected: Yes. Shared: Yes (with Google for OAuth, with transactional email provider, and with Stripe/analytics providers as needed).
Processed ephemerally: No (persisted in user profiles).
Required: Required (needed for account creation and authentication).
Why collected: App functionality (account/authentication), Developer communications (receipts/notifications), Fraud prevention/security, Account management, Analytics/Advertising (aggregated measurement).
Why shared: App functionality (Google OAuth), Developer communications (email provider), Fraud prevention/security (Stripe), Analytics/Advertising (aggregated reporting).

---

One-paste block for Google Play Console (copy and paste the sections below in order):

## 1) Data collection and security

- All network traffic is encrypted with TLS. Personal and financial data are stored securely on the backend.

## 2) Data types selected (copy the categories you selected in the form)

- Personal info: Email, Name
- Financial info: Budgets, Transactions, Bank connection metadata
- Payment info: Purchases (Stripe Checkout)
- Device identifiers & Advertising ID
- App info & performance: Crash reports, analytics
- User uploads: Photos (receipts), Files & Documents

## 3) Per-type short descriptions (paste into the per-type detail fields)

Personal info: Collected: email, display name. Purpose: account/authentication. Shared: only with Google when using Google Sign-in; not sold.
Email: Collected: yes. Shared: yes (Google when using Google Sign-in, transactional email provider, Stripe/analytics as needed). Used for account creation, receipts, fraud prevention, and account management.
Name: Collected: yes. Shared: no (except Google OAuth when used). Purpose: profile display and account management.
Financial info: Collected: budgets, transactions, bank connection metadata. Purpose: core app functionality. Shared: no.
Payment info: Collected/transmitted during Stripe Checkout. Card details are handled by Stripe and are not stored by our servers.
Device & identifiers: Collected: device identifiers and Advertising ID. Purpose: analytics and ad personalization. Shared: Google (AdMob, Analytics).
App telemetry: Collected: crash reports and analytics. Shared: Google (Analytics/Crash) if enabled.
User uploads: Collected: receipts and documents (camera or file uploads). Purpose: bookkeeping and OCR. Shared: no.

## 4) Retention & deletion (paste where the Play Console asks)

- Active personal & financial data are deleted within 30 days after verified request. Backups may be retained up to 90 days; logs/anonymized records up to 180 days where required by law or security.

## 5) URLs & contacts (paste into Delete account/data fields)

- Account deletion URL: [Account deletion](https://planilha-financeira-fam-lia-davi-martini.onrender.com/account/delete)
- Optional data deletion page: [Data deletion page](https://planilha-financeira-fam-lia-davi-martini.onrender.com/apps/atlasfortefinanceiro/account/delete)
- Privacy policy: [Privacy policy](https://planilha-financeira-fam-lia-davi-martini.onrender.com/privacy)
- Support contact: [davimartini@gmail.com](mailto:davimartini@gmail.com)

## 6) Reviewer note (paste into reviewer notes)

- Payments use Stripe Checkout (PCI-compliant). Card numbers are not stored by our servers. Delete URLs are public and include step-by-step verification instructions. Contact [davimartini@gmail.com](mailto:davimartini@gmail.com) for verification or access.

---

(Use these exact short lines to fill the Play Console fields quickly. Tell me if you want me to paste these directly into any docs or create a small PR.)
