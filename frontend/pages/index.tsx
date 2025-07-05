import AudioRecorder from '../components/AudioRecorder'
import Form from '../components/Form'

export default function Home() {
  return (
    <div>
      <h1>🎙️ Ultra-Low Latency Voice Agent</h1>
      <AudioRecorder />
      <Form />
    </div>
  )
}
