import { useState, useEffect } from 'react'

export default function Form() {
  const [isVisible, setIsVisible] = useState(false)
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')

  // Listen for form updates from voice commands
  useEffect(() => {
    const handleFormUpdate = (event: MessageEvent) => {
      const data = JSON.parse(event.data)
      if (data.type === 'form_update') {
        if (data.action === 'open') {
          setIsVisible(true)
        } else if (data.action === 'fill') {
          if (data.name) setName(data.name)
          if (data.email) setEmail(data.email)
        }
      }
    }

    // Subscribe to WebSocket messages
    if (typeof window !== 'undefined') {
      window.addEventListener('message', handleFormUpdate)
      return () => window.removeEventListener('message', handleFormUpdate)
    }
  }, [])

  if (!isVisible) return null

  return (
    <div className="form-container">
      <h2>Voice-Controlled Form</h2>
      <form className="voice-form">
        <div className="form-field">
          <label htmlFor="name">Name:</label>
          <input
            id="name"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Say: My name is [your name]"
          />
        </div>
        <div className="form-field">
          <label htmlFor="email">Email:</label>
          <input
            id="email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Say: My email is [your email]"
          />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  )
}
