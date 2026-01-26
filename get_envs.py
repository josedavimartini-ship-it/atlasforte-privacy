import os, json, urllib.request, urllib.error

# Read Render API token from env var to avoid hard-coded secrets
token = os.environ.get('RENDER_TOKEN')
if not token:
    raise SystemExit('RENDER_TOKEN environment variable is required')

service = os.environ.get('SERVICE_ID', 'srv-d4vhscu3jp1c73eltvog')
try:
    req=urllib.request.Request(f'https://api.render.com/v1/services/{service}/env-vars', headers={'Authorization':f'Bearer {token}'})
    with urllib.request.urlopen(req, timeout=30) as r:
        data=json.load(r)
    print(json.dumps(data, indent=2))
except Exception as e:
    print('ERROR', repr(e))
