

async function perform_sentiment_analysis(text) {
    try {
        const response = await fetch('http://localhost:5001/api/sentimentanalysis', {
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
        console.log(error)
        throw new Error('An unexpected network error occurred')
    }
}