import numpy as np
import sounddevice as sd
import torch
import torchaudio
import whisper
from typing import Tuple, Optional
from scipy import signal

class AudioProcessor:
    def __init__(self):
        self.sample_rate = 16000  # Standard for speech processing
        self.model = whisper.load_model("base")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
    def process_audio_chunk(self, audio_data: bytes) -> Tuple[np.ndarray, int]:
        """Convert raw audio bytes to numpy array and preprocess."""
        # Convert bytes to numpy array (16-bit PCM)
        audio_array = np.frombuffer(audio_data, dtype=np.int16)
        
        # Convert to float32 and normalize
        audio_float = audio_array.astype(np.float32) / 32768.0
        
        # Resample if needed
        if self.sample_rate != 16000:
            audio_float = signal.resample(audio_float, 
                                        int(len(audio_float) * 16000 / self.sample_rate))
        
        return audio_float, self.sample_rate
    
    def transcribe_audio(self, audio_array: np.ndarray) -> str:
        """Transcribe audio using Whisper model."""
        # Convert numpy array to tensor
        audio_tensor = torch.from_numpy(audio_array).to(self.device)
        
        # Transcribe
        result = self.model.transcribe(audio_tensor.numpy())
        return result["text"]
    
    def text_to_speech(self, text: str) -> np.ndarray:
        """Convert text to speech using TorchAudio."""
        # Initialize TTS model (using default settings)
        processor = torchaudio.pipelines.TACOTRON2_WAVERNN_PHONE_LJSPEECH
        
        # Generate speech
        with torch.no_grad():
            waveforms, _ = processor.generate([text])
        
        # Convert to numpy array
        audio_array = waveforms.cpu().numpy().squeeze()
        return audio_array
    
    def prepare_audio_response(self, audio_array: np.ndarray) -> bytes:
        """Convert numpy array to bytes for transmission."""
        # Normalize and convert to 16-bit PCM
        audio_int16 = (audio_array * 32768.0).astype(np.int16)
        return audio_int16.tobytes()