

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

        const result = await response.json();
        return result
    }
    catch (error) {
        throw new Error('An unexpected network error occurred')
    }
}

export default perform_sentiment_analysis;