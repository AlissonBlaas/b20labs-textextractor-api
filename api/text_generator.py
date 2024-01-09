import openai
import time

class TextGenerator:
    def generate_text(self, prompt):
        pass

class OpenAITextGenerator(TextGenerator):
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_text(self, prompt):
        try:
            response = openai.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=prompt,
                max_tokens=200,
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return {'GPT-3 error': str(e)}
