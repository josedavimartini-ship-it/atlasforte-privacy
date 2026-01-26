import 'dart:ui';
import 'package:flutter/material.dart';

/// AFF design tokens — cores, espaçamentos, raios, estados e helpers
class AffTokens {
  // Surfaces
  static const surface0 = Color(0xFFE7E4DF); // fundo app (mineral claro)
  static const surface1 = Color(0xFFDEDAD4); // cards
  static const surface2 = Color(0xFFD4D0CA); // elevated
  static const divider  = Color(0xFFB9B4AD);

  // Ink / textos
  static const ink0 = Color(0xFF1F2428); // principal (grafite profundo)
  static const ink1 = Color(0xFF2D353C); // secundário
  static const ink2 = Color(0xFF4A545D); // terciário

  // Brand (petroleum)
  static const petroleum0 = Color(0xFF0F2C33);
  static const petroleum1 = Color(0xFF163A42);

  // Accent (bronze muted)
  static const bronze0 = Color(0xFF7A6048);
  static const bronze1 = Color(0xFF6A523E);

  // Estados
  static const positive = Color(0xFF1F4D3A);
  static const negative = Color(0xFF5A2326);
  static const warning  = Color(0xFF6A4A24);

  // Spacing
  static const spaceSmall = 4.0;
  static const spaceXS = 8.0;
  static const spaceSm = 12.0;
  static const spaceMd = 16.0;
  static const spaceLg = 20.0;
  static const spaceXL = 24.0;
  static const spaceXXL = 32.0;

  // Radii
  static const radiusSm = 12.0;
  static const radiusMd = 16.0;
  static const radiusLg = 22.0;

  // Helpers for shapes
  static RoundedRectangleBorder cardShape([double radius = radiusMd]) =>
      RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(radius),
        side: const BorderSide(color: divider, width: 1),
      );

  // Text styles (helpers)
  static TextStyle affTextStyleMoney([Color? color, double size = 20]) =>
      TextStyle(
        color: color ?? ink0,
        fontSize: size,
        fontWeight: FontWeight.w600,
        fontFeatures: const [FontFeature.tabularFigures()],
      );

  static TextStyle affTextStyleLabel([Color? color, double size = 12]) =>
      TextStyle(
        color: color ?? ink1,
        fontSize: size,
        fontWeight: FontWeight.w400,
      );
}
