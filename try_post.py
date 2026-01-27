import os, json, urllib.request, urllib.error

# Read token and service from environment for safety
token = os.environ.get('RENDER_TOKEN')
if not token:
    raise SystemExit('RENDER_TOKEN environment variable is required')
service = os.environ.get('SERVICE_ID', 'srv-d4vhscu3jp1c73eltvog')
headers={'Authorization':f'Bearer {token}','Content-Type':'application/json'}
# Try creating a test env var
payload = json.dumps({'envVar':{'key':'_TEST_VAR_FOR_SCRIPT','value':'testvalue'}}).encode('utf-8')
req = urllib.request.Request(f'https://api.render.com/v1/services/{service}/env-vars', data=payload, headers=headers, method='POST')
try:
    with urllib.request.urlopen(req) as r:
        print('Create response:', r.status, r.read())
except urllib.error.HTTPError as e:
    print('Create failed:', e.code, e.read())

# Try updating existing env var by deleting and recreating (if necessary) 
