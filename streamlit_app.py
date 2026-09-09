import streamlit as st
from src import auth_tests, session_tests, role_tests, api_tests

st.title("PS-07 AuthZ Assessment Demo")

st.sidebar.header("Test Modules")
choice = st.sidebar.selectbox("Select a test", ["Login Flow", "Authentication", "Session", "Authorization", "API Parity"])

if choice == "Login Flow":
    st.write(auth_tests.map_login_flow())
elif choice == "Authentication":
    st.write(auth_tests.test_boundaries())
elif choice == "Session":
    st.write(session_tests.inspect_sessions())
elif choice == "Authorization":
    st.write(role_tests.verify_roles())
elif choice == "API Parity":
    st.write(api_tests.check_parity())
