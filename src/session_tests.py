import requests

BASE_URL = "https://app.archscale.in"

def inspect_sessions():
    """
    Inspect cookies, JWTs, refresh tokens, logout behavior.
    """
    session = requests.Session()
    resp = session.get(BASE_URL)
    cookies = session.cookies.get_dict()
    return {
        "initial_status": resp.status_code,
        "cookies": cookies,
        "note": "Extend with JWT decode, refresh token checks"
    }
