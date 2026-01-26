import os, urllib.request, json, urllib.error

# Read token and service from environment (do not hard-code)
token = os.environ.get('RENDER_TOKEN')
if not token:
    raise SystemExit('RENDER_TOKEN environment variable is required')
service = os.environ.get('SERVICE_ID', 'srv-d4vhscu3jp1c73eltvog')
headers={'Authorization':f'Bearer {token}','Content-Type':'application/json'}
payload = json.dumps({'envVar':{'key':'_TEST_VAR_FOR_SCRIPT2','value':'testvalue2'}}).encode('utf-8')
req = urllib.request.Request(f'https://api.render.com/v1/services/{service}/env-vars', data=payload, headers=headers, method='POST')
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print('Created', r.status, r.read())
except urllib.error.HTTPError as e:
    print('Failed', e.code, e.read())
except Exception as e:
    print('ERROR', e)
