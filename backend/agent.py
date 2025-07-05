import os
from typing import Optional, Dict, Any
import google.generativeai as genai
from dotenv import load_dotenv
from form_tool import FormTool

class AIAgent:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])
        self.form_tool = FormTool()
        
    async def process_text(self, text: str) -> str:
        """Process text input and generate response."""
        # Check for form-related commands
        if "open form" in text.lower():
            self.form_tool.open_form()
            return "Form has been opened. You can now fill in your details."
        
        if "fill form" in text.lower():
            # Extract name and email using simple pattern matching
            # In a real app, use more robust NLP for entity extraction
            words = text.lower().split()
            try:
                name_idx = words.index("name")
                email_idx = words.index("email")
                
                name = " ".join(words[name_idx+1:email_idx])
                email = words[email_idx+1]
                
                result = self.form_tool.fill_form(name=name, email=email)
                return f"Form updated: {result['message']}"
            except (ValueError, IndexError):
                return "Please provide both name and email in the format: fill form name John Doe email john@example.com"
        
        # Regular conversation
        try:
            response = await self.chat.send_message_async(text)
            return response.text
        except Exception as e:
            return f"Error processing message: {str(e)}"
    
    async def process_audio(self, text_input: str) -> str:
        """Process audio input (transcribed text) and return response text."""
        return await self.process_text(text_input)