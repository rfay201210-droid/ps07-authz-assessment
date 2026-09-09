from src import auth_tests, session_tests, role_tests, api_tests

def run_all():
    print("Login Flow:", auth_tests.map_login_flow())
    print("Auth Boundaries:", auth_tests.test_boundaries())
    print("Session Handling:", session_tests.inspect_sessions())
    print("Role Checks:", role_tests.verify_roles())
    print("API Parity:", api_tests.check_parity())

if __name__ == "__main__":
    run_all()
