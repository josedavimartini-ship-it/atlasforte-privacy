<#
PowerShell script to delete generated store assets listed in TO_DELETE_BY_REQUEST.txt
Run this from the repository root (where your .git folder is).
Usage: .\assets\store_listing\delete_generated_assets.ps1
#>

$ErrorActionPreference = 'Stop'

$list = Join-Path $PSScriptRoot 'TO_DELETE_BY_REQUEST.txt'
if (-not (Test-Path $list)) {
  Write-Host "List file not found: $list" -ForegroundColor Yellow
  exit 1
}

$files = Get-Content $list | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }

Write-Host "Preparing to delete $($files.Count) files listed in TO_DELETE_BY_REQUEST.txt" -ForegroundColor Cyan

foreach ($f in $files) {
  $path = Join-Path $PSScriptRoot $f
  if (Test-Path $path) {
    Write-Host "Deleting: $path"
    Remove-Item -Force -ErrorAction Stop $path
  } else {
    Write-Host "Not found (skipping): $path" -ForegroundColor Yellow
  }
}

# If this is a git repo, stage deletions and commit
try {
  git rev-parse --is-inside-work-tree > $null 2>&1
  Write-Host "Git repository detected — staging deletions and committing" -ForegroundColor Green
  git add -A
  git commit -m "chore(store): remove generated store assets per user request"
  Write-Host "Committed deletions. Please push manually with: git push origin HEAD" -ForegroundColor Green
} catch {
  Write-Host "Not a git repository or git not available — files removed locally only." -ForegroundColor Yellow
}

Write-Host "Done." -ForegroundColor Cyan