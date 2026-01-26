# Flutter Google Sign-in snippet (paste into `main.dart` / a widget)

Use this minimal code to add a "Sign in with Google" button which calls the helper `signInWithGoogleAndLogin(API_BASE)` (already provided in `lib/google_sign_in_helper.dart`). The snippet uses a `TextButton` but you can replace it with a branded `SignInButton` or package.

```dart
import 'package:flutter/material.dart';
import 'lib/google_sign_in_helper.dart'; // adjust import path as needed

class GoogleSignInButton extends StatefulWidget {
  final String apiBase;
  const GoogleSignInButton({super.key, required this.apiBase});

  @override
  _GoogleSignInButtonState createState() => _GoogleSignInButtonState();
}

class _GoogleSignInButtonState extends State<GoogleSignInButton> {
  bool _loading = false;

  Future<void> _handleSignIn() async {
    setState(() => _loading = true);
    try {
      final token = await signInWithGoogleAndLogin(widget.apiBase);
      if (token != null) {
        // Save token & update app state. Example: store in secure storage
        ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Signed in successfully')));
      } else {
        ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Sign in cancelled or failed')));
      }
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Sign-in error: $e')));
    } finally {
      setState(() => _loading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return TextButton.icon(
      onPressed: _loading ? null : _handleSignIn,
      icon: Icon(Icons.login),
      label: Text(_loading ? 'Signing in...' : 'Sign in with Google'),
    );
  }
}
```

Notes:

- Replace `API_BASE` or pass it from your `main.dart` environment config.
- Persist the returned token (JWT or legacy token) in secure storage; update UI accordingly.
- Test sign-in flow on an actual device/emulator with a Google account configured.

If you want, I can produce a ready-to-apply PR against the Flutter repo that inserts this button into the app's login screen (just point me to the Flutter project path or open a PR there).
