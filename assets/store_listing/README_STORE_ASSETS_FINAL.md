# Final store assets generated from user source icon

Files created:

- icon_source.png (original provided)
- icon_512.png (512x512 app icon)
- feature_1024x500.png (feature graphic)
- screenshot1_1080x1920.png .. screenshot4_1080x1920.png (phone screenshots)

Upload instructions:

- App icon: upload icon_512.png (PNG, 512x512)
- Feature graphic: upload feature_1024x500.png
- Screenshots: upload the 4 phone screenshots

How to regenerate

- Using Python (recommended):

  ```python
  python scripts/generate_store_assets.py -s assets/store_listing/final/icon_source.png
  ```

- Using PowerShell wrapper:

  ```powershell
  .\scripts\generate_store_assets.ps1 -Source .\assets\store_listing\final\icon_source.png
  ```

If you provide a new icon, drop it in `assets/store_listing/final/` as `icon_source.png` (or pass the path to `-s/--source`) and run the script. The generator will skip existing files unless you pass `--force`/`-f` to overwrite.

