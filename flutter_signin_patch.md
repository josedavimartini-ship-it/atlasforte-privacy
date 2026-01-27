# Patch: Add Google Sign-in button to Flutter app

This is a small patch and instructions you can apply inside your Flutter app (`android_app/flutter_app`). It adds the `GoogleSignInButton` widget to the login screen and wires it to the existing `google_sign_in_helper.dart` helper.

1. Ensure dependency in `pubspec.yaml` (should already be present):

  dependencies:
    google_sign_in: ^6.0.0

1. Add the widget file (create `lib/widgets/google_sign_in_button.dart`):

```dart
import 'package:flutter/material.dart';
import '../google_sign_in_helper.dart';

class GoogleSignInButton extends StatefulWidget {
  final String apiBase;
  const GoogleSignInButton({super.key, required this.apiBase});

  @override
  State<GoogleSignInButton> createState() => _GoogleSignInButtonState();
}

class _GoogleSignInButtonState extends State<GoogleSignInButton> {
  bool _loading = false;

  Future<void> _handleSignIn() async {
    setState(() => _loading = true);
    try {
      final token = await signInWithGoogleAndLogin(widget.apiBase);
      if (token != null) {
        // TODO: Replace with your token storage logic
        ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Signed in')));
      } else {
        ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Sign-in cancelled or failed')));
      }
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Error: $e')));
    } finally {
      setState(() => _loading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return TextButton.icon(
      onPressed: _loading ? null : _handleSignIn,
      icon: const Icon(Icons.login),
      label: Text(_loading ? 'Signing in...' : 'Sign in with Google'),
    );
  }
}
```

1. Insert into your login screen (example `lib/main.dart` or login widget):

```dart
// in your LoginScreen build method
Column(
  children: [
    // existing email/password form
    SizedBox(height: 12),
    GoogleSignInButton(apiBase: const String.fromEnvironment('API_BASE', defaultValue: 'https://planilha-financeira-fam-lia-davi-martini.onrender.com')),
  ],
)
```

1. Testing:

- Run the app on device/emulator and test the Google Sign-in flow. It should return an ID token which is exchanged with the backend via `/api/oauth/google` (make sure the backend is reachable and configured).
- Use `smoke-oauth` workflow to test invalid token rejection while developing (`workflow_dispatch` or push triggers).


If you want, I can produce a ready-made patch file or open a PR in this repo with these changes; I can also test it in CI if you provide a branch with the Flutter app included (or let me know the repo path to target).
