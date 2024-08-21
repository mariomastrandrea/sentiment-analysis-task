import React, { useState } from 'react'

function SimpleTextAreaForm({ buttonText, handleSubmittedText }) {
    const [text, setText] = useState('');
    
    const handleSubmit = async (e) => {
        e.preventDefault()
        handleSubmittedText(text)
    }
    
    return (
        <form onSubmit={handleSubmit}>
            <textarea
              value={text}
              onChange={(e) => setText(t => e.target.value)}
              placeholder="Enter text here..."
              rows="4"
              cols="50"
            />
            <br />
            <button type="submit">{buttonText}</button>
        </form>
    );
}

export default SimpleTextAreaForm;