import React, { useState } from 'react'
import './SentimentAnalysisPage.css'
import SimpleTextAreaForm from '../common/SimpleTextAreaForm';

function SentimentAnalysisPage() {
    const [result, setResult] = useState(null);
    const [error, setError] = useState(null);

    const handleSubmittedText = async (text) => {
        setError(null);
        setResult(null);


    }

    return (
        <div className='SentimentAnalysisPage'>
          <header className="App-header">
          <h1>Sentiment Analysis</h1>
          
          <SimpleTextAreaForm 
              buttonText={"Analyze Sentiment"} 
              handleSubmittedText={handleSubmittedText} 
          />

          {error && <p className="error">Error: {error}</p>}

          {result && (
            <div className="result">
              <h2>Analysis Result</h2>
              <p><strong>Polarity:</strong> {result.polarity}</p>
              <p><strong>Subjectivity:</strong> {result.subjectivity}</p>
            </div>
          )}
        </header>
      </div>
    );
}

export default SentimentAnalysisPage;