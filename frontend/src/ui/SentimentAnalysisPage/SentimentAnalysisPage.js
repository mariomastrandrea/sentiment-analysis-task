import React, { useState } from 'react'
import './SentimentAnalysisPage.css'
import SimpleTextAreaForm from '../common/SimpleTextAreaForm';
import perform_sentiment_analysis from '../../network/client'
import SentimentAnalysisResultBox from '../common/SentimentAnalysisResultBox';

function SentimentAnalysisPage() {
    const [outputMetrics, setOutputMetrics] = useState(null);
    const [error, setError] = useState(null);

    const handleSubmittedText = async (text) => {
        setError(null);
        setOutputMetrics(null);

        try {
            const sentiment_analysis_result = await perform_sentiment_analysis(text ?? "")

            setOutputMetrics({
                polarity: sentiment_analysis_result.polarity,
                subjectivity: sentiment_analysis_result.subjectivity
            })
        }
        catch (error) {
            setError(error.message)
        }
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

          {outputMetrics && <SentimentAnalysisResultBox 
              polarity={outputMetrics.polarity}
              subjectivity={outputMetrics.subjectivity} 
          />}
        </header>
      </div>
    );
}

export default SentimentAnalysisPage;