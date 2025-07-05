# Ultra-Low Latency AI Voice Agent

A real-time AI voice agent that achieves sub-500ms voice-to-voice communication using Pipecat framework and Google Gemini Live API.

## Features

- 🎙️ Real-time voice-to-voice communication
- ⚡ Ultra-low latency (<500ms response time)
- 🔄 Natural conversation with interruption support
- 📝 Voice-controlled form filling

## Tech Stack

- **Frontend**: Next.js with WebSocket client
- **Backend**: FastAPI with Pipecat pipeline
- **AI**: Google Gemini Live API
- **Communication**: WebSocket with real-time audio streaming

## Setup

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy the example environment file and configure your API key:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your Gemini API key

5. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

## Usage

1. Open your browser and navigate to `http://localhost:3000`
2. Allow microphone access when prompted
3. Start speaking - the agent will respond in real-time
4. Try voice commands like:
   - "I want to fill a form"
   - "My name is John Smith"
   - "My email is john@example.com"

## Project Structure

```
├── backend/
│   ├── main.py          # FastAPI server setup
│   ├── agent.py         # Pipecat agent configuration
│   ├── form_tool.py     # Form handling functionality
│   └── requirements.txt  # Python dependencies
└── frontend/
    ├── components/      # React components
    ├── pages/           # Next.js pages
    └── styles/          # CSS styles
```

## Performance

- Voice-to-Voice Latency: <500ms
- Connection Setup: <2 seconds
- Tool Response: <1 second for form operations