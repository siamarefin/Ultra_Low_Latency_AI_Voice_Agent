import { useState } from 'react'

export default function Form() {
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')

  return (
    <form>
      <input placeholder="Name" value={name} onChange={e => setName(e.target.value)} />
      <input placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
      <button type="submit">Submit</button>
    </form>
  )
}
