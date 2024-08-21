import React from 'react'
import "./SentimentAnalysisHistoryBox.css"

function SentimentAnalysisHistoryBox({ entries }) {
    return (
        <div className="sentiment-analysis-history-box">
          <h2>Sentiment Analysis History</h2>
          <table>
            <thead>
              <tr>
                <th>Text</th>
                <th>Polarity</th>
                <th>Subjectivity</th>
                <th>Timestamp</th>
              </tr>
            </thead>
            <tbody>
              {entries.map(entry => (
                <tr key={entry.timestamp}>
                  <td>{entry.text}</td>
                  <td>{entry.polarity}</td>
                  <td>{entry.subjectivity}</td>
                  <td>{entry.timestamp}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      );
}

export default SentimentAnalysisHistoryBox;
