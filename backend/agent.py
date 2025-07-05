import os
import google.generativeai as genai
from pipecat import Pipecat
from dotenv import load_dotenv


def get_agent():
    genai.configure(api_key="AIzaSyBhR8sZEibkB2TWMTiAy2YCWpBL85eyp_E")
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
