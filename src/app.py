import streamlit as st
from config.config import Config
from components.sidebar import render_sidebar
from components.chat_interface import ChatInterface
from components.telemetry_dashboard import TelemetryDashboard
from components.automation_panel import AutomationPanel
from components.knowledge_base import KnowledgeBase
from utils.session_state import initialize_session_state
from utils.auth import check_authentication, check_role_permission
from utils.openai_service import OpenAIService

def main():
    try:
        # Validate configuration
        Config.validate()
        
        st.set_page_config(
            page_title="Integrated Platform Environment (IPE)",
            layout="wide",
            initial_sidebar_state="expanded"
        )

        # Initialize session state
        initialize_session_state()

        # Check authentication before proceeding
        if not check_authentication():
            return

        # Main application layout
        st.title("Integrated Platform Environment (IPE)")

        # Render sidebar and get current page
        current_page = render_sidebar()

        # Main content area based on selected page
        if current_page == "Dashboard":
            if check_role_permission("viewer"):
                TelemetryDashboard().render()
            else:
                st.error("Insufficient permissions")
                
        elif current_page == "Chat Support":
            if check_role_permission("support"):
                ChatInterface().render()
            else:
                st.error("Insufficient permissions")
                
        elif current_page == "Automation":
            if check_role_permission("support"):
                AutomationPanel().render()
            else:
                st.error("Insufficient permissions")
                
        elif current_page == "Knowledge Base":
            if check_role_permission("viewer"):
                KnowledgeBase().render()
            else:
                st.error("Insufficient permissions")

        # Initialize the service
        openai_service = OpenAIService()

        # Get a completion
        response = openai_service.get_completion("How do I troubleshoot high CPU usage?")

        # Get embeddings
        embeddings = openai_service.get_embeddings("Sample text")

        # Analyze sentiment
        sentiment = openai_service.analyze_sentiment("Great service!")

        # Summarize text
        summary = openai_service.summarize_text("Long text here...", max_length=100)

    except ValueError as e:
        st.error(f"Configuration Error: {str(e)}")
        st.info("Please set up your .env file with the required API keys.")
        return

if __name__ == "__main__":
    main() 