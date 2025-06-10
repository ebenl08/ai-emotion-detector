''' A module used to detect the emotion associated with
    analysed text
'''
import requests
import json

def emotion_detector(text_to_analyse):
    ''' A function to detect the emotion type associated with a given text/string input.
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=header, timeout=8.0)
    return response.text

