''' A module used to detect the emotion associated with
    analysed text
'''
import requests
import json



def emotion_detector(text_to_analyse):
    ''' A function to detect the emotion scores associated 
        with a given text/string input. The output is a dictionary of
        the scores for different emotion types and the dominant emotion type
    '''
    # Input & Configuration
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    #Empty score dictionary
    emotion_scores = { "anger": None, "disgust": None, "fear": None, 
            "joy": None, "sadness": None, 
            "dominant_emotion": None
        }
    
    # Send request to the model to process the text
    response = requests.post(url, json=myobj, headers=header, timeout=8.0)

    # Error handling
    if response.status_code == 400:
        return emotion_scores

    # Format the response text into JSON
    formatted_response = json.loads(response.text)

    #Processing Output
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores["dominant_emotion"] = dominant_emotion

    return emotion_scores

