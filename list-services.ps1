# List Render services safely using RENDER_TOKEN from environment
$token = $env:RENDER_TOKEN
if (-not $token) {
  Write-Error "RENDER_TOKEN environment variable is required"
  exit 1
}
$headers = @{ Authorization = "Bearer $token" }
try {
  Invoke-RestMethod -Uri 'https://api.render.com/v1/services' -Headers $headers | ConvertTo-Json -Depth 5
} catch {
  Write-Error "Failed to list services: $_"
  exit 1
}
