<#
Import new icon art from a local folder into the repository and regenerate final store assets.

Usage examples (run from repository root):
  # Copy icons from a backup folder, keep a backup of existing final assets and regenerate
  .\scripts\import_new_icons.ps1 -SourcePath 'D:\Bkp SSD\Downloads\JoseDaviDownloads\AtlasForteFinancial' -Force

Parameters:
  -SourcePath (required): Local folder containing PNG/JPG icon art.
  -Out (optional): Destination folder in repository. Default: 'assets/store_listing/final'
  -Force (switch): Overwrite existing outputs during regeneration.

What the script does:
  1. Validates the source folder exists and contains image files.
  2. Creates a timestamped backup of current contents of the output folder (if any).
  3. Copies all PNG/JPG files from the source folder to the output folder. The primary file is copied as `icon_source.png` (heuristic: file name containing 'icon' or '512', otherwise largest file).
  4. Runs the Python generators to produce `icon_512.png`, `feature_1024x500.png` and screenshots.
#>
param(
    [Parameter(Mandatory=$true)] [string]$SourcePath,
    [string]$Out = 'assets/store_listing/final',
    [switch]$Force
)

Set-StrictMode -Version Latest

# Resolve paths
$src = Resolve-Path -Path $SourcePath -ErrorAction Stop
$outdir = Resolve-Path -Path $Out -ErrorAction SilentlyContinue
if (-not $outdir) { New-Item -ItemType Directory -Path $Out -Force | Out-Null }
$outdir = Resolve-Path -Path $Out

# Find images
$images = Get-ChildItem -Path $src -Include *.png, *.jpg, *.jpeg -File -ErrorAction SilentlyContinue
if (-not $images -or $images.Count -eq 0) {
    Write-Error "No PNG/JPG files found in $SourcePath"
    exit 1
}

# Backup existing outputs
$timestamp = (Get-Date -Format 'yyyyMMdd_HHmmss')
$backupDir = Join-Path -Path (Split-Path -Parent $Out) -ChildPath "removed_assets_$timestamp"
if (Get-ChildItem -Path $Out -File -ErrorAction SilentlyContinue) {
    New-Item -ItemType Directory -Path $backupDir -Force | Out-Null
    Get-ChildItem -Path $Out -File | ForEach-Object { Move-Item -Path $_.FullName -Destination $backupDir -Force }
    Write-Host "Backed up existing assets to $backupDir"
} else {
    Write-Host "No existing assets to back up in $Out"
}

# Choose a primary source file for icon_source.png
$primary = $images | Where-Object { $_.Name -match 'icon|512' } | Select-Object -First 1
if (-not $primary) { $primary = $images | Sort-Object Length -Descending | Select-Object -First 1 }
$primaryDst = Join-Path $outdir 'icon_source.png'
Copy-Item -Path $primary.FullName -Destination $primaryDst -Force
Write-Host "Selected primary icon: $($primary.Name) -> $primaryDst"

# Copy remaining images (if any)
foreach ($img in $images) {
    $dst = Join-Path $outdir $img.Name
    Copy-Item -Path $img.FullName -Destination $dst -Force
}
Write-Host "Copied $($images.Count) image(s) from $SourcePath to $Out"

# Run python generators
$python = 'python'
$genScript = 'scripts/generate_store_assets.py'
$screensScript = 'scripts/generate_final_screenshots.py'
$forceArg = ''
if ($Force) { $forceArg = '--force' }

Write-Host "Running asset generator: $genScript"
& $python $genScript -s $primaryDst -o $Out $forceArg
if ($LASTEXITCODE -ne 0) { Write-Error "generate_store_assets.py failed (exit $LASTEXITCODE)"; exit $LASTEXITCODE }

Write-Host "Generating final screenshots"
& $python $screensScript -s $primaryDst -o $Out
if ($LASTEXITCODE -ne 0) { Write-Error "generate_final_screenshots.py failed (exit $LASTEXITCODE)"; exit $LASTEXITCODE }

Write-Host "Import complete. New assets are in: $Out"
Write-Host "Backup of previous assets (if any) is at: $backupDir"

# End script
