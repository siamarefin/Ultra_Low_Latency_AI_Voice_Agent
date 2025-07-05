import google.generativeai as genai
from pipecat import Pipecat

def get_agent():
    genai.configure(api_key="YOUR_GEMINI_API_KEY")
    agent = Pipecat(
        llm="gemini",
        voice=True,
        functions=[
            {
                "name": "open_form",
                "description": "Opens form on command",
            },
            {
                "name": "fill_form",
                "description": "Fills form fields",
                "parameters": {"name": "str", "email": "str"},
            },
        ],
    )
    return agent
