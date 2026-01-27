import os
import requests

API_BASE = os.environ.get('API_BASE', 'https://planilha-financeira-fam-lia-davi-martini.onrender.com')


def test_oauth_rejects_invalid_token():
    url = f"{API_BASE}/api/oauth/google"
    # send a known-bad id_token and expect 4xx response
    r = requests.post(url, json={"id_token": "invalid-token"}, timeout=10)
    assert r.status_code // 100 == 4


def test_account_deletion_endpoint_reachable():
    url = f"{API_BASE}/account/delete"
    r = requests.get(url, timeout=10)
    assert r.status_code == 200
