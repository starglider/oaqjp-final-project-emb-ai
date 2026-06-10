import requests
import json


def emotion_detector(text):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text} } 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    try:
        response = requests.post(url, json = myobj, headers=header) 
        if response.status_code!=200:
            return "Error"
        return response.text
    except:
        return "Error"