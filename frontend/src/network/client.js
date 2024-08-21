

const baseUrl = "http://localhost:5001/api/"

async function perform_sentiment_analysis(text) {
    try {
        const endpointUrl = baseUrl + "sentimentanalysis"

        const response = await fetch(endpointUrl, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text }),
        });

        if (!response.ok) {
            throw new Error('An unexpected error occurred processing your request');
        }

        const analysis_result = await response.json();
        return analysis_result
    }
    catch (error) {
        throw new Error('An unexpected network error occurred')
    }
}

async function fetch_sentiment_analysis_history() {
    try {
        const endpointUrl = baseUrl + "sentimentanalysis"

        const response = await fetch(endpointUrl, {
            method: 'GET'
        });

        if (!response.ok) {
            throw new Error('An unexpected error occurred fetching history of requests');
        }

        const history = await response.json();
        return history
    }
    catch (error) {
        throw new Error('An unexpected network error occurred fetching history')
    }
}

export {
    perform_sentiment_analysis,
    fetch_sentiment_analysis_history
};