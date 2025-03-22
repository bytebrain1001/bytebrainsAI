import streamlit as st
from services.data_service import DataService
from utils.openai_service import OpenAIService
import pandas as pd

class ChatInterface:
    def __init__(self):
        self.data_service = DataService()
        self.openai_service = OpenAIService()

    def render(self):
        st.header("AI Support Assistant")

        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Load sample data for context
        incidents = self.data_service.get_incidents()
        kb_articles = self.data_service.get_kb_articles()

        # Chat input
        if prompt := st.chat_input("How can I help you?"):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})

            # Get relevant context
            relevant_incidents = self.find_relevant_incidents(prompt, incidents)
            relevant_articles = self.find_relevant_articles(prompt, kb_articles)

            # Enhance prompt with context
            enhanced_prompt = self.enhance_prompt(prompt, relevant_incidents, relevant_articles)

            # Get AI response
            response = self.openai_service.get_completion(enhanced_prompt)

            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})

        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def find_relevant_incidents(self, query: str, incidents: pd.DataFrame) -> pd.DataFrame:
        """Simple keyword-based search for relevant incidents"""
        return incidents[
            incidents['title'].str.contains(query, case=False) |
            incidents['description'].str.contains(query, case=False)
        ].head(3)

    def find_relevant_articles(self, query: str, articles: pd.DataFrame) -> pd.DataFrame:
        """Simple keyword-based search for relevant KB articles"""
        return articles[
            articles['title'].str.contains(query, case=False) |
            articles['content'].str.contains(query, case=False)
        ].head(3)

    def enhance_prompt(self, prompt: str, incidents: pd.DataFrame, articles: pd.DataFrame) -> str:
        """Enhance user prompt with relevant context"""
        context = "Context:\n"
        
        if not incidents.empty:
            context += "\nRelevant Incidents:\n"
            for _, incident in incidents.iterrows():
                context += f"- {incident['title']} ({incident['status']})\n"

        if not articles.empty:
            context += "\nRelevant KB Articles:\n"
            for _, article in articles.iterrows():
                context += f"- {article['title']}\n"

        return f"{context}\nUser Query: {prompt}\n\nPlease provide a response considering the above context."