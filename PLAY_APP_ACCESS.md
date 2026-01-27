# Play App Access & Google Sign-in

This document explains how to wire Google Sign-in in the Flutter app and how the backend verifies the ID token.

## 1. Google Cloud / OAuth setup 🔧

- Create an OAuth client in Google Cloud Console (APIs & Services → Credentials → Create credentials → OAuth client ID).
- For Android, add the Android package name and SHA‑1 (debug/release as needed). For iOS, add the bundle identifier.
- Copy the client ID for use in the app configuration (when required).

## 2. Flutter client changes 🧩

- Add the `google_sign_in` package to `pubspec.yaml` (already added in the repo).
- Use the helper `signInWithGoogleAndLogin(API_BASE)` from `lib/google_sign_in_helper.dart` to perform sign in and exchange the Google ID token with the backend. Example wiring in a button handler:

```dart
// pseudo-code
final token = await signInWithGoogleAndLogin(API_BASE);
if (token != null) {
  // persist token and update UI
}
```

- Place a `Sign in with Google` button in your Flutter UI and call the helper from the onPressed handler.

## 3. Backend endpoint ✅

- The server exposes `POST /api/oauth/google` which accepts a JSON body like `{ "id_token": "<google-id-token>" }`.
- The server verifies the ID token with Google, creates or links a user, and returns the app token/credentials for the client.

## 4. Testing & Play Console notes 🧪

- Test sign-in flow on device/emulator with a Google account included on the device.
- For Play Console: ensure the OAuth consent screen is configured and the app access items (account deletion URL, privacy policy) point to the correct URLs (e.g., static account deletion page added for AtlasForteFinanceiro).
- Quick local smoke test (repo): a small smoke test is available at `tests/smoke_oauth_google.py` which POSTs an invalid id_token to `POST /api/oauth/google` and expects the server to reject it. Run it locally with `API_BASE=http://localhost:5000 python tests/smoke_oauth_google.py`.

## 5. Troubleshooting 💡

- If the server returns an invalid token error, verify the client ID used and that the ID token was issued for your OAuth client.
- Verify Android SHA‑1 matches the fingerprint used when creating the OAuth client.

---

If you want, I can add a concrete UI snippet for your app's `main.dart` and open a PR with the changes. ✅
