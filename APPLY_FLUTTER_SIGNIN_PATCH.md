# APPLY: Flutter Google Sign-in patch

Use these commands in your Flutter project repository to apply the `flutter_signin_patch.md` patch (or copy the files manually). The patch adds `lib/widgets/google_sign_in_button.dart` and wires it in your login screen.

Steps (on your Flutter repo):

1. Create a branch:

  git checkout -b feature/google-signin

1. Add dependency in `pubspec.yaml` (if not already):

  dependencies:
    google_sign_in: ^6.0.0

1. Create file `lib/widgets/google_sign_in_button.dart` with the contents from `flutter_signin_patch.md`.

1. Update your login screen to import and insert the widget:

  import 'widgets/google_sign_in_button.dart';

  // inside your build:
  GoogleSignInButton(apiBase: const String.fromEnvironment('API_BASE', defaultValue: 'YOUR_API_BASE_URL')),

1. Run `flutter pub get`, build and test on emulator/device.

1. Commit & push:

  git add pubspec.yaml lib/widgets/google_sign_in_button.dart path/to/modified-login-files
  git commit -m "feat(auth): add Google Sign-in button and helper wiring"
  git push -u origin feature/google-signin

1. Open a Pull Request to your main branch and request review/testing for OAuth flow.

Notes:

- Ensure the OAuth client ID and SHA-1 fingerprints used to sign the app are registered in the Google Cloud Console and Play Console.
- Test with a real device and a Google account that is allowed on your OAuth consent screen (add as a test user if the consent screen is in testing mode).
- I can open the PR for you if you provide the Flutter repo remote or grant me permission to commit.
