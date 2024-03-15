from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
sentiment_analysis = pipeline('sentiment-analysis')

@app.route('/analyze', methods=['POST'])
def analyze_text():
    try:
        data = request.get_json()
        text = data['text']
        
        # Perform sentiment analysis
        result = sentiment_analysis(text)
        
        # Return the sentiment analysis result
        return jsonify({'sentiment': result[0]['label'], 'confidence': result[0]['score']})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

