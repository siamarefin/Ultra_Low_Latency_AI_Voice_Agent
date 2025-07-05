import AudioRecorder from '../components/AudioRecorder'
import Form from '../components/Form'

export default function Home() {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold text-center mb-8">🎙️ Ultra-Low Latency Voice Agent</h1>
      
      <div className="max-w-2xl mx-auto bg-white rounded-lg shadow-sm p-6 mb-8 text-center">
        <AudioRecorder />
        <p className="text-sm text-gray-600 mt-2">
          Try saying: "I want to fill a form" or "My name is John"
        </p>
      </div>

      <Form />
    </div>
  )
}
