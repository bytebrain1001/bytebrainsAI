import openai
from config.config import Config

class OpenAIService:
    def __init__(self):
        # Set OpenAI API key
        openai.api_key = Config.OPENAI_API_KEY
        self.model = Config.OPENAI_MODEL

    def get_completion(self, prompt: str) -> str:
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an AI assistant for IT support."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except openai.error.OpenAIError as e:
            raise Exception(f"OpenAI API error: {str(e)}") 