import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class LLMClient:
    def __init__(self, provider="groq"):
        self.provider = provider
        
        if provider == "groq":
            self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
            self.model = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
        else:
            raise ValueError(f"Unsupported provider: {provider}")
        
    def generate_text(self, system_prompt, user_prompt, temperature=0.2):

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        
        if self.provider == "groq":
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature
            )
            
        
    
            if response and response.choices:
               return response.choices[0].message.content.strip()
   
        return ""
