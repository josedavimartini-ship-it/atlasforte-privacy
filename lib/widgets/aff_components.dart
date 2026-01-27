import 'package:flutter/material.dart';
import '../theme/aff_tokens.dart';

// AffHeaderCard: título forte, subtítulo mais leve, ação opcional
class AffHeaderCard extends StatelessWidget {
  final String title;
  final String? subtitle;
  final Widget? action;

  const AffHeaderCard({super.key, required this.title, this.subtitle, this.action});

  @override
  Widget build(BuildContext context) {
    return Card(
      shape: AffTokens.cardShape(),
      child: Padding(
        padding: const EdgeInsets.all(AffTokens.spaceMd),
        child: Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(title, style: Theme.of(context).textTheme.titleLarge),
                  if (subtitle != null)
                    Padding(
                      padding: const EdgeInsets.only(top: 6.0),
                      child: Text(subtitle!, style: Theme.of(context).textTheme.bodyMedium?.copyWith(color: AffTokens.ink1)),
                    ),
                ],
              ),
            ),
            if (action != null) action!,
          ],
        ),
      ),
    );
  }
}

// AffMark: marca abstrata (A estrutural) simples
class AffMark extends StatelessWidget {
  final double size;
  final Color? color;
  const AffMark({super.key, this.size = 40, this.color});

  @override
  Widget build(BuildContext context) {
    final c = color ?? AffTokens.petroleum1;
    return Container(
      width: size,
      height: size,
      decoration: BoxDecoration(
        color: c,
        borderRadius: BorderRadius.circular(AffTokens.radiusSm),
      ),
      child: Center(
        child: Text('A', style: TextStyle(color: AffTokens.surface0, fontWeight: FontWeight.w700)),
      ),
    );
  }
}

// AffSurfaceCard: card padrão com padding e título opcional
class AffSurfaceCard extends StatelessWidget {
  final Widget child;
  final EdgeInsetsGeometry padding;
  final String? title;

  const AffSurfaceCard({super.key, required this.child, this.padding = const EdgeInsets.all(AffTokens.spaceMd), this.title});

  @override
  Widget build(BuildContext context) {
    return Card(
      shape: AffTokens.cardShape(),
      child: Padding(
        padding: padding,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            if (title != null) ...[
              Text(title!, style: Theme.of(context).textTheme.titleMedium),
              const SizedBox(height: AffTokens.spaceSm),
            ],
            child,
          ],
        ),
      ),
    );
  }
}

// AffMetricTile: label + valor + delta discreto
class AffMetricTile extends StatelessWidget {
  final String label;
  final String value;
  final String? delta;

  const AffMetricTile({super.key, required this.label, required this.value, this.delta});

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(label, style: Theme.of(context).textTheme.bodySmall?.copyWith(color: AffTokens.ink2)),
        const SizedBox(height: 6),
        Row(
          children: [
            Text(value, style: AffTokens.affTextStyleMoney(AffTokens.ink0, 22)),
            if (delta != null) ...[
              const SizedBox(width: 8),
              Text(delta!, style: Theme.of(context).textTheme.bodySmall?.copyWith(color: AffTokens.ink1)),
            ],
          ],
        )
      ],
    );
  }
}
