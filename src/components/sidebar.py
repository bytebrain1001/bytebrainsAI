import streamlit as st
from utils.session_state import get_current_incident, clear_current_incident, update_current_incident

def render_sidebar() -> str:
    """
    Render the sidebar navigation and return the selected page
    Returns:
        str: The currently selected page
    """
    with st.sidebar:
        st.header("Navigation")
        
        # Select page using radio buttons
        current_page = st.radio(
            "Select Page",
            options=[
                "Dashboard",
                "Chat Support",
                "Automation",
                "Knowledge Base"
            ],
            index=0  # Default to Dashboard
        )
        
        # Show current context if available
        current_incident = get_current_incident()
        if current_incident:
            st.sidebar.markdown("---")
            st.sidebar.subheader("Current Context")
            st.sidebar.info(
                f"Incident: {current_incident['id']} - {current_incident['title']}\n"
                f"Priority: {current_incident['priority']}"
            )
            if st.sidebar.button("Clear Incident", key="clear_incident_button"):
                clear_current_incident()
                st.rerun()
        
        # Add user info section
        st.sidebar.markdown("---")
        st.sidebar.subheader("User Info")
        if "user" in st.session_state:
            st.sidebar.text(f"User: {st.session_state.user}")
            if st.sidebar.button("Logout", key="sidebar_logout_button"):
                st.session_state.clear()
                st.rerun()

    return current_page 