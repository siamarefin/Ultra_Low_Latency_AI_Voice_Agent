from typing import Optional
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from agent import AIAgent
from utils.audio import AudioProcessor

app = FastAPI()
agent = AIAgent()
audio_processor = AudioProcessor()

@app.websocket("/ws/audio")
async def audio_stream(websocket: WebSocket) -> None:
    """Handle WebSocket connection for audio streaming.
    
    Args:
        websocket: WebSocket connection instance
    """
    try:
        await websocket.accept()
        print("Client connected")
        
        async for message in websocket.iter_bytes():
            try:
                # Process incoming audio
                audio_array, sample_rate = audio_processor.process_audio_chunk(message)
                
                # Transcribe audio to text
                text = audio_processor.transcribe_audio(audio_array)
                
                # Get AI response
                response_text = await agent.process_audio(text)
                
                # Convert response to speech
                response_audio = audio_processor.text_to_speech(response_text)
                
                # Prepare and send response
                response_bytes = audio_processor.prepare_audio_response(response_audio)
                await websocket.send_bytes(response_bytes)
                
            except Exception as e:
                error_msg = f"Error processing audio: {str(e)}"
                print(error_msg)
                await websocket.send_json({"error": error_msg})
                
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        error_msg = f"WebSocket error: {str(e)}"
        print(error_msg)
        try:
            await websocket.close()
        except:
            pass

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
