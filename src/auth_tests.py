import requests

BASE_URL = "https://app.archscale.in"

def map_login_flow():
    """
    Map login, reset, and recovery endpoints.
    """
    return {
        "login": f"{BASE_URL}/login",
        "reset_password": f"{BASE_URL}/reset",
        "account_recovery": f"{BASE_URL}/recover"
    }

def test_boundaries():
    """
    Safe boundary tests: invalid creds, rate limit simulation.
    """
    results = []
    # Example: invalid login attempt
    resp = requests.post(f"{BASE_URL}/login", json={"email":"fake@user.com","password":"wrong"})
    results.append({"test":"Invalid login","status":resp.status_code})
    return results
