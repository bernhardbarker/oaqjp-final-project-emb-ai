""" Detects emotion of statements """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Application")


@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """ Endpoint to detect emotion of statement """
    result = emotion_detector(request.args.get("textToAnalyze"))
    dominant = result.pop("dominant_emotion")
    if dominant is None:
        return "Invalid text! Please try again!"
    stringified = ", ".join([f"'{key}': {value}" for key, value in result.items()])
    return (f"For the given statement, the system response is {stringified}. "
            f"The dominant emotion is {dominant}.")

@app.route('/')
def home():
    """ Endpoint to render index template """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
