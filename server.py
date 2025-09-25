"""
Flask server for Emotion Detection application.
Exposes an endpoint to analyze emotions in text using the emotion_detector function.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the index.html template as the home page.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_endpoint():
    """
    Endpoint to analyze emotions in the given text.
    Returns a formatted string with emotion scores and the dominant emotion.
    Handles invalid or blank input gracefully.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Invalid text! Please try again!", 400

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!", 400

    response_str = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_str


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
