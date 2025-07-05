import { useEffect, useRef } from 'react'
import io from 'socket.io-client'

const socket = new WebSocket("ws://localhost:8000/ws/audio")

export default function AudioRecorder() {
  const mediaRecorderRef = useRef<MediaRecorder | null>(null)

  useEffect(() => {
    navigator.mediaDevices.getUserMedia({ audio: true }).then((stream) => {
      const recorder = new MediaRecorder(stream)
      recorder.ondataavailable = (e) => {
        if (socket.readyState === WebSocket.OPEN) {
          socket.send(e.data)
        }
      }
      recorder.start(100)
      mediaRecorderRef.current = recorder
    })

    socket.onmessage = (e) => {
      const audio = new Audio(URL.createObjectURL(new Blob([e.data])))
      audio.play()
    }
  }, [])

  return <div>🎤 Mic Active. Speak Now!</div>
}
