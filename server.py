''' Flask application that are capable of detecting the emotion value
    or scores of a given text input using the model from 
    the Watson NLP Library 
'''
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def detect_emotion():
    ''' Retrieve and print emotion scores and the dominant 
        emotion from a given string text input
    '''
    # Retrieve user input
    text_to_analyze = request.args.get('textToAnalyze')

    # Determine the emotion scores of the text input
    emotion_scores = emotion_detector(text_to_analyze)

    # Handling NoneType values in emotion_scores
    if emotion_scores['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

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
    ''' Render the index.html (Frontend)
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
            