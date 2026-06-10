"""Server for the final project"""
from flask import Flask,render_template,request
from .emotion_detection import emotion_detector

app = Flask("Sentiment Analyzer")
@app.route("/emotionDetector")
def sent_analyzer():
    """Handle /emotionDetect"""
    text = request.args.get('textToAnalyze')
    response = emotion_detector(text)
    if response['dominant_emotion'] is not None:
        return (f"For the given statement, the system response is 'anger':"
        f" {response['anger']}, 'disgust': {response['disgust']}, "
        f" 'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>.")
    return '<b>Invalid text! Please try again!</b>'


@app.route("/")
def render_index_page():
    """Handle /"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
