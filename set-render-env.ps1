# Sanitized PowerShell helper: use RENDER_TOKEN from environment (do NOT hard-code tokens)
$token = $env:RENDER_TOKEN
if (-not $token) {
  Write-Error "RENDER_TOKEN environment variable is required"
  exit 1
}
$service = 'srv-d4vhscu3jp1c73eltvog'
$envPath = 'C:\projetos\melhorias_planilha\.env'

# Invoke Python helper to sync env vars
python set_render_env.py -t $token -s $service -e $envPath

