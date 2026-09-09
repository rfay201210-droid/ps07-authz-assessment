import requests

BASE_URL = "https://app.archscale.in"

def check_parity():
    """
    Confirm backend APIs enforce same access controls as UI.
    """
    endpoints = ["/api/data", "/api/admin"]
    results = []
    for ep in endpoints:
        resp = requests.get(f"{BASE_URL}{ep}")
        results.append({"endpoint": ep, "status": resp.status_code})
    return results
