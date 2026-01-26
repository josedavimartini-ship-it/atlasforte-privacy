# TODO Issues (create GitHub issues from these)

Create the following issues in your repository to track remaining work for Play launch:

1. Paste Play Data Safety and verify

- Title: "Play Data Safety: paste short snippets & verify"
- Description: "Paste the one-paste block from `PLAY_DATA_SAFETY.md` into Play Console Data Safety form, run validations, and attach screenshots of any flags. Contact: [davimartini@gmail.com](mailto:davimartini@gmail.com)"
- Labels: play, release, data-safety

1. Apply Flutter Google Sign-in patch

- Title: "Add Google Sign-in button (feature/google-signin)"
- Description: "Apply `patches/google_signin_patch.diff` in Flutter repo, add dependency `google_sign_in`, insert the widget, test on device, and open PR. Test that `/api/oauth/google` exchanges ID token and returns app token. Assign to: @davimartini"
- Labels: feature, auth, mobile

1. Internal Test: Upload AAB and verify OAuth flows

- Title: "Upload AAB to Internal Test and verify OAuth"
- Description: "Upload signed AAB to Play Internal Track, add test users to OAuth consent, verify Google Sign-in and Deletion flow works for test accounts. Report any issues."
- Labels: release, test

1. CI/E2E: Add E2E test for OAuth + Account Deletion

- Title: "Add E2E test: Google OAuth -> Account Deletion"
- Description: "Add test that signs in (Google or email), triggers account deletion API, verifies deletion effect in DB or via API, and uploads logs as artifact. This can be implemented in GitHub Actions or a separate E2E runner."
- Labels: test, ci

1. Monitor & Rotate Render Token (ongoing)

- Title: "Render Token rotation procedure and monitoring"
- Description: "Document token rotation steps and run periodic checks. Include issue template for rotation and verify RENDER_TOKEN is set in GitHub Secrets."

- Labels: infra, security
