import requests

BASE_URL = "https://app.archscale.in"

def verify_roles():
    """
    Verify role-based access control.
    """
    # Placeholder: simulate accessing a protected resource
    resp = requests.get(f"{BASE_URL}/api/protected")
    return {
        "endpoint": "/api/protected",
        "status": resp.status_code,
        "note": "Check if unauthorized users can access restricted objects"
    }
