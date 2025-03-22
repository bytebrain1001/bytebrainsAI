from openai import OpenAI
from typing import List, Dict, Any
from config.config import Config
import streamlit as st

class OpenAIService:
    def __init__(self):
        # Initialize OpenAI client with API key
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        self.model = Config.OPENAI_MODEL
        self.system_prompt = """You are an AI assistant for IT support. 
        You help with troubleshooting, incident management, and technical guidance. 
        Provide clear, concise responses and step-by-step solutions when applicable."""

    def get_completion(self, prompt: str) -> str:
        """
        Get completion from OpenAI API
        Args:
            prompt: User prompt with context
        Returns:
            str: AI response
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error getting AI response: {str(e)}"

    def get_embeddings(self, text: str) -> List[float]:
        """
        Get embeddings for text using OpenAI API
        Args:
            text: Text to get embeddings for
        Returns:
            List[float]: Text embeddings
        """
        try:
            response = self.client.embeddings.create(
                model="text-embedding-ada-002",
                input=text
            )
            return response.data[0].embedding
        except Exception as e:
            raise Exception(f"Error getting embeddings: {str(e)}")

    def analyze_sentiment(self, text: str) -> Dict[str, Any]:
        """
        Analyze sentiment of text using OpenAI
        Args:
            text: Text to analyze
        Returns:
            Dict containing sentiment analysis
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Analyze the sentiment and respond with only 'positive', 'negative', or 'neutral'."},
                    {"role": "user", "content": text}
                ],
                temperature=0.3
            )
            return {
                "text": text,
                "sentiment": response.choices[0].message.content.strip().lower(),
                "confidence": 0.8  # Placeholder confidence score
            }
        except Exception as e:
            return {
                "text": text,
                "sentiment": "unknown",
                "error": str(e)
            }

    def summarize_text(self, text: str, max_length: int = 100) -> str:
        """
        Summarize text using OpenAI
        Args:
            text: Text to summarize
            max_length: Maximum length of summary
        Returns:
            str: Summarized text
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": f"Summarize the following text in no more than {max_length} characters."},
                    {"role": "user", "content": text}
                ],
                temperature=0.5
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error summarizing text: {str(e)}"

    def categorize_text(self, text: str, categories: List[str]) -> str:
        """
        Categorize text into predefined categories
        Args:
            text: Text to categorize
            categories: List of possible categories
        Returns:
            str: Best matching category
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": f"Categorize the text into one of these categories: {categories}"},
                    {"role": "user", "content": text}
                ],
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error categorizing text: {str(e)}"

    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """
        Extract named entities from text
        Args:
            text: Text to analyze
        Returns:
            Dict containing extracted entities
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": """Extract and categorize entities into these categories:
                        - People
                        - Organizations
                        - Technical Terms
                        - Error Codes
                        Respond in JSON format."""},
                    {"role": "user", "content": text}
                ],
                temperature=0.3
            )
            return {
                "text": text,
                "entities": response.choices[0].message.content
            }
        except Exception as e:
            return {
                "text": text,
                "error": str(e)
            }

    def render_validation_form(self):
        with st.form("validation_form"):
            input_value = st.text_input("Required Field")
            submitted = st.form_submit_button("Submit")
            
            if submitted:
                if not input_value:
                    st.error("Please fill in all required fields")
                else:
                    st.success("Form submitted successfully!")

    def render_form_1(self):
        with st.form("form_1"):
            submitted_1 = st.form_submit_button("Submit 1")

    def render_form_2(self):
        with st.form("form_2"):
            submitted_2 = st.form_submit_button("Submit 2")

    def render_form_submission(self):
        if submitted:
            # Handle form submission outside the form
            st.success("Form submitted!")

    def render_form_with_unique_id(self):
        with st.form("unique_form_id"):
            # Form inputs here
            submitted = st.form_submit_button("Submit")

    def render_form_with_unique_id_2(self):
        with st.form("unique_form_id_2"):
            # Form inputs here
            submitted = st.form_submit_button("Submit") 