from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def detect_emotion():
    # Retrieve user input
    text_to_analyze = request.args.get('textToAnalyze')

    # Determine the emotion scores of the text input
    emotion_scores = emotion_detector(text_to_analyze)
    
    # Format output message in accordance to the project requirement
    message = "For the given statement, the system response is "
    for emotion, score in emotion_scores.items():
        if emotion == "dominant_emotion":
            message += f"The dominant emotion is {score}."
        elif emotion == "sadness":
            message = message[:-2]
            message += f" and '{emotion}': {score}. "
        else:
            message += f"'{emotion}': {score}, "

    return message

@app.route('/')
def render_index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
            