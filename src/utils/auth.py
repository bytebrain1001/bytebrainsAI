import streamlit as st
from datetime import datetime, timedelta
from typing import Dict, Optional

class AuthenticationError(Exception):
    """Custom exception for authentication errors"""
    pass

# Sample user database (in production, this would be a real database)
SAMPLE_USERS = {
    "admin": {
        "password": "admin123",  # In production, use hashed passwords
        "role": "admin",
        "name": "Admin User"
    },
    "support": {
        "password": "support123",
        "role": "support",
        "name": "Support User"
    },
    "viewer": {
        "password": "viewer123",
        "role": "viewer",
        "name": "Viewer User"
    }
}

def check_authentication() -> bool:
    """
    Check if user is authenticated
    Returns:
        bool: True if authenticated, False otherwise
    """
    # Initialize session state for authentication
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.user = None
        st.session_state.role = None
        st.session_state.login_time = None

    # If already authenticated, check session expiry
    if st.session_state.authenticated:
        if check_session_expired():
            logout_user()
            st.error("Session expired. Please login again.")
            return False
        return True

    # If not authenticated, show login form
    return show_login_form()

def show_login_form() -> bool:
    """
    Display login form and handle login
    Returns:
        bool: True if login successful, False otherwise
    """
    st.sidebar.title("Login")
    
    # Login form
    with st.sidebar.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            try:
                user = authenticate_user(username, password)
                if user:
                    # Set session state
                    st.session_state.authenticated = True
                    st.session_state.user = user["name"]
                    st.session_state.role = user["role"]
                    st.session_state.login_time = datetime.now()
                    st.success(f"Welcome {user['name']}!")
                    st.rerun()
                    return True
            except AuthenticationError as e:
                st.error(str(e))
                return False

    return False

def authenticate_user(username: str, password: str) -> Optional[Dict]:
    """
    Authenticate user credentials
    Args:
        username: Username
        password: Password
    Returns:
        Dict containing user information if authenticated
    Raises:
        AuthenticationError if authentication fails
    """
    if not username or not password:
        raise AuthenticationError("Please enter both username and password")

    user = SAMPLE_USERS.get(username)
    if not user:
        raise AuthenticationError("Invalid username")

    if user["password"] != password:  # In production, use proper password hashing
        raise AuthenticationError("Invalid password")

    return {
        "name": user["name"],
        "role": user["role"]
    }

def check_session_expired() -> bool:
    """
    Check if current session has expired
    Returns:
        bool: True if session expired, False otherwise
    """
    if not st.session_state.login_time:
        return True

    # Session timeout after 8 hours
    session_timeout = timedelta(hours=8)
    return datetime.now() - st.session_state.login_time > session_timeout

def logout_user():
    """Clear authentication session state"""
    st.session_state.authenticated = False
    st.session_state.user = None
    st.session_state.role = None
    st.session_state.login_time = None

def check_role_permission(required_role: str) -> bool:
    """
    Check if current user has required role
    Args:
        required_role: Required role for access
    Returns:
        bool: True if user has required role, False otherwise
    """
    if not st.session_state.authenticated:
        return False

    role_hierarchy = {
        "admin": 3,
        "support": 2,
        "viewer": 1
    }

    user_role = st.session_state.role
    return role_hierarchy.get(user_role, 0) >= role_hierarchy.get(required_role, 0)

def get_current_user() -> Optional[Dict]:
    """
    Get current user information
    Returns:
        Dict containing user information if authenticated, None otherwise
    """
    if not st.session_state.authenticated:
        return None

    return {
        "name": st.session_state.user,
        "role": st.session_state.role,
        "login_time": st.session_state.login_time
    }

def render_user_info():
    """Render user information in sidebar"""
    if st.session_state.authenticated:
        with st.sidebar:
            st.markdown("---")
            st.subheader("User Information")
            st.write(f"Name: {st.session_state.user}")
            st.write(f"Role: {st.session_state.role}")
            if st.session_state.login_time:
                st.write(f"Login Time: {st.session_state.login_time.strftime('%Y-%m-%d %H:%M:%S')}")
            # Add unique key to the logout button
            if st.button("Logout", key="auth_logout_button"):
                logout_user()
                st.rerun() 