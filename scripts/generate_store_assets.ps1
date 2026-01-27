param(
    [Parameter(Mandatory=$true)][string]$Source,
    [string]$Out = 'assets/store_listing/final',
    [switch]$Force
)

# Run the Python generator. Assumes 'python' is on PATH (or use your active venv python).
$forceArg = ''
if ($Force) { $forceArg = '--force' }
python scripts/generate_store_assets.py -s $Source -o $Out $forceArg

if ($LASTEXITCODE -ne 0) { Write-Error 'Generator failed.'; exit $LASTEXITCODE }
Write-Host 'Generator completed. Check' $Out
