import os, json, urllib.request, urllib.error

# Read Render token from environment for safety
token = os.environ.get('RENDER_TOKEN')
if not token:
    raise SystemExit('RENDER_TOKEN environment variable is required')
service = os.environ.get('SERVICE_ID', 'srv-d4vhscu3jp1c73eltvog')
env_path = os.environ.get('ENV_PATH', r'C:\projetos\melhorias_planilha\.env')

def read_env(path):
    d = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                k, v = line.split('=', 1)
                d[k.strip()] = v.strip()
    return d

env = read_env(env_path)
vars = [
    {'name': 'STRIPE_SECRET_KEY', 'value': env.get('STRIPE_SECRET_KEY', ''), 'secure': True},
    {'name': 'STRIPE_PUBLISHABLE_KEY', 'value': env.get('STRIPE_PUBLISHABLE_KEY', ''), 'secure': True},
    {'name': 'STRIPE_WEBHOOK_SECRET', 'value': env.get('STRIPE_WEBHOOK_SECRET', ''), 'secure': True},
    {'name': 'APP_URL', 'value': 'https://planilha-financeira-fam-lia-davi-martini.onrender.com', 'secure': False},
    {'name': 'STRIPE_SUCCESS_URL', 'value': 'https://planilha-financeira-fam-lia-davi-martini.onrender.com/ads/success', 'secure': False},
    {'name': 'STRIPE_CANCEL_URL', 'value': 'https://planilha-financeira-fam-lia-davi-martini.onrender.com/ads/cancel', 'secure': False},
    {'name': 'ADS_AUTO_ACTIVATE', 'value': '1', 'secure': False},
]

headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

req = urllib.request.Request(f'https://api.render.com/v1/services/{service}/env-vars', headers={'Authorization': f'Bearer {token}'})
with urllib.request.urlopen(req) as resp:
    existing = json.load(resp)

for v in vars:
    exists = None
    for e in existing:
        if e.get('name') == v['name']:
            exists = e
            break
    data = json.dumps({'name': v['name'], 'value': v['value'], 'secure': v['secure']}).encode('utf-8')
    if exists:
        url = f'https://api.render.com/v1/services/{service}/env-vars/{exists['id']}'
        req = urllib.request.Request(url, data=data, headers=headers, method='PATCH')
        try:
            with urllib.request.urlopen(req) as r:
                print('Updated', v['name'])
        except urllib.error.HTTPError as e:
            print('Failed to update', v['name'], e.code, e.read())
    else:
        url = f'https://api.render.com/v1/services/{service}/env-vars'
        req = urllib.request.Request(url, data=data, headers=headers, method='POST')
        try:
            with urllib.request.urlopen(req) as r:
                print('Created', v['name'])
        except urllib.error.HTTPError as e:
            print('Failed to create', v['name'], e.code, e.read())
