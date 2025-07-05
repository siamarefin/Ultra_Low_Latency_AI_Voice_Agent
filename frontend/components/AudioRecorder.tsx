import { useEffect, useRef, useState } from 'react'

const socket = new WebSocket("ws://localhost:8000/ws/audio")

export default function AudioRecorder() {
  const mediaRecorderRef = useRef<MediaRecorder | null>(null)
  const [status, setStatus] = useState('connecting')
  const [isRecording, setIsRecording] = useState(false)

  useEffect(() => {
    // WebSocket connection handling
    socket.onopen = () => {
      setStatus('connected')
      startRecording()
    }
    socket.onclose = () => setStatus('disconnected')
    socket.onerror = () => setStatus('error')

    return () => {
      socket.close()
      if (mediaRecorderRef.current) {
        mediaRecorderRef.current.stop()
      }
    }
  }, [])

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
      const recorder = new MediaRecorder(stream)
      
      recorder.ondataavailable = (e) => {
        if (socket.readyState === WebSocket.OPEN) {
          socket.send(e.data)
        }
      }

      recorder.onstart = () => setIsRecording(true)
      recorder.onstop = () => setIsRecording(false)
      
      recorder.start(100)
      mediaRecorderRef.current = recorder
    } catch (err) {
      console.error('Error accessing microphone:', err)
      setStatus('error')
    }
  }

  // Handle audio playback from server
  socket.onmessage = (e) => {
    const audio = new Audio(URL.createObjectURL(new Blob([e.data])))
    audio.play()
  }

  return (
    <div className="audio-recorder">
      <div className={`status-indicator ${status}`}>
        {status === 'connecting' && '🔄 Connecting...'}
        {status === 'connected' && '🟢 Connected'}
        {status === 'disconnected' && '🔴 Disconnected'}
        {status === 'error' && '⚠️ Error'}
      </div>
      
      <div className="mic-status">
        {isRecording ? (
          <div className="recording-indicator">
            🎤 Listening...
            <span className="pulse"></span>
          </div>
        ) : (
          <div>🎤 Starting microphone...</div>
        )}
      </div>
    </div>
  )
}
