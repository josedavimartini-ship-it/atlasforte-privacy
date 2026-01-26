"""Simple smoke test for POST /api/oauth/google

Usage:
  API_BASE=http://localhost:5000 python -m pytest tests/smoke_oauth_google.py
or
  python tests/smoke_oauth_google.py

The test verifies the endpoint returns a 4xx status when provided an invalid id_token.
"""

import os
import sys
import json

try:
    import requests
except ImportError:
    print('Please install requests to run this test: pip install requests')
    sys.exit(2)

API_BASE = os.environ.get('API_BASE', 'http://localhost:5000')
URL = f"{API_BASE.rstrip('/')}/api/oauth/google"

INVALID_TOKEN = 'invalid_id_token_for_local_testing'


def main():
    resp = requests.post(URL, json={'id_token': INVALID_TOKEN}, timeout=10)
    # Expect the server to reject an invalid token (HTTP 400 or 401 or similar)
    if resp.status_code >= 400 and resp.status_code < 500:
        print('PASS: endpoint rejected invalid token with status', resp.status_code)
        return 0
    else:
        print('FAIL: unexpected response code', resp.status_code)
        print('Response body:', resp.text)
        return 1


if __name__ == '__main__':
    sys.exit(main())
