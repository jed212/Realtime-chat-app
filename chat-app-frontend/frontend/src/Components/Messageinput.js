import React, { useState } from 'react'

export default function Messageinput() {
    const {inputValue, setInputValue} = useState('');
    const handleInputChange = (event) => {
        setInputValue(event.target.value)
    }

    const handleSendMessage = () => {
        console.log("MESSAGE SEND")
    }
  return (
    <div className='message-input'>
        <textarea
        placeholder='Type you message'
        value={inputValue}
        onchange={handleInputChange}
        />
        <button onClick={handleSendMessage}>Send</button>
    </div>
  )
}
