import 'dart:ui';
import 'package:flutter/material.dart';
import 'aff_tokens.dart';

class AffTheme {
  static ThemeData light() {
    final cs = ColorScheme(
      brightness: Brightness.light,
      primary: AffTokens.petroleum0,
      onPrimary: AffTokens.surface0,
      secondary: AffTokens.bronze0,
      onSecondary: AffTokens.surface0,
      error: AffTokens.negative,
      onError: AffTokens.surface0,
      surface: AffTokens.surface0,
      onSurface: AffTokens.ink0,
      background: AffTokens.surface0,
      onBackground: AffTokens.ink0,
      tertiary: AffTokens.petroleum1,
      onTertiary: AffTokens.surface0,
    );

    final base = ThemeData(
      useMaterial3: true,
      colorScheme: cs,
      scaffoldBackgroundColor: AffTokens.surface0,
      dividerColor: AffTokens.divider,
      visualDensity: VisualDensity.adaptivePlatformDensity,
      textTheme: Typography.material2021().black,
    );

    return base.copyWith(
      appBarTheme: AppBarTheme(
        backgroundColor: AffTokens.surface0,
        foregroundColor: AffTokens.ink0,
        elevation: 0,
        scrolledUnderElevation: 0,
        centerTitle: false,
        titleTextStyle: base.textTheme.titleLarge?.copyWith(
          color: AffTokens.ink0,
          fontWeight: FontWeight.w700,
        ),
      ),
      cardTheme: CardTheme(
        color: AffTokens.surface1,
        elevation: 0,
        shape: AffTokens.cardShape(AffTokens.radiusMd),
        margin: EdgeInsets.zero,
      ),
      textTheme: base.textTheme.apply(
        bodyColor: AffTokens.ink0,
        displayColor: AffTokens.ink0,
      ).copyWith(
        bodyMedium: base.textTheme.bodyMedium?.copyWith(
          height: 1.25,
          fontFeatures: const [FontFeature.tabularFigures()],
        ),
        titleMedium: base.textTheme.titleMedium?.copyWith(
          fontWeight: FontWeight.w600,
          letterSpacing: 0.1,
        ),
        titleLarge: base.textTheme.titleLarge?.copyWith(
          fontWeight: FontWeight.w700,
          letterSpacing: 0.2,
        ),
      ),
      inputDecorationTheme: InputDecorationTheme(
        filled: true,
        fillColor: AffTokens.surface2,
        contentPadding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(14),
          borderSide: const BorderSide(color: AffTokens.divider),
        ),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(14),
          borderSide: const BorderSide(color: AffTokens.divider),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(14),
          borderSide: BorderSide(color: AffTokens.petroleum1, width: 1.5),
        ),
      ),
      chipTheme: base.chipTheme.copyWith(
        backgroundColor: AffTokens.surface2,
        side: const BorderSide(color: AffTokens.divider),
        labelStyle: const TextStyle(color: AffTokens.ink1),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: AffTokens.petroleum0,
          foregroundColor: AffTokens.surface0,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        ),
      ),
      outlinedButtonTheme: OutlinedButtonThemeData(
        style: OutlinedButton.styleFrom(
          foregroundColor: AffTokens.ink0,
          side: const BorderSide(color: AffTokens.divider),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        ),
      ),
    );
  }
}
