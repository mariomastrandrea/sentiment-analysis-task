import React, { useState, useEffect } from 'react'
import './SentimentAnalysisPage.css'
import SimpleTextAreaForm from '../common/SimpleTextAreaForm';
import { perform_sentiment_analysis, fetch_sentiment_analysis_history } from '../../network/client'
import SentimentAnalysisResultBox from '../common/SentimentAnalysisResultBox';
import SentimentAnalysisHistoryBox from '../common/SentimentAnalysisHistoryBox/SentimentAnalysisHistoryBox';

function SentimentAnalysisPage() {
    const [outputMetrics, setOutputMetrics] = useState(null);
    const [error, setError] = useState(null);
    const [history, setHistory] = useState(null)

    const fetchData = async () => {
      try {
          const fetched_history = await fetch_sentiment_analysis_history()

          setHistory(
              fetched_history
                .sort((a, b) => b.timestamp - a.timestamp)    // inverse chronological order
                .map(x => ({
                    text: x.text,
                    polarity: x.polarity,
                    subjectivity: x.subjectivity,
                    timestamp: new Date(x.timestamp * 1000).toLocaleString()
                }))
          )
      }
      catch (error) {
          setError(error.message)
      }
  }

    useEffect(() => {
        fetchData()
    }, [outputMetrics])

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
        <div className='sentiment-analysis-page'>
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

          {history && <SentimentAnalysisHistoryBox entries={history} />}
        </header>
      </div>
    );
}

export default SentimentAnalysisPage;