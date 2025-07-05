from fastapi import FastAPI, WebSocket
from agent import get_agent

app = FastAPI()
agent = get_agent()

@app.websocket("/ws/audio")
async def audio_stream(websocket: WebSocket):
    await websocket.accept()
    async for message in websocket.iter_bytes():
        response_audio = await agent.process_audio(message)
        await websocket.send_bytes(response_audio)
