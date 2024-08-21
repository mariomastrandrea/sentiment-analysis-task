import React from 'react'

function SentimentAnalysisResultBox({ polarity, subjectivity }) {
    return (
        <div className="result">
              <h2>Analysis Result</h2>
              <p><strong>Polarity:</strong> {polarity}</p>
              <p><strong>Subjectivity:</strong> {subjectivity}</p>
        </div>
    );
}

export default SentimentAnalysisResultBox;