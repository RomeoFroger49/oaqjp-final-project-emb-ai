"""
    Import necessary libraries
"""
import json
import requests

def predict_emotion(text_to_analyse):
    """
    Function to predict the emotion of a given text.
    """

    api_url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(api_url, json=payload, headers=header, timeout=10)

    formatted_response = json.loads(response.text)

    # Handle error response 400
    if response.status_code == 400:
        return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominate_emotion': None
    }

    # Exctract of all the emotion score
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    # determine the dominant emotion
    dominate_emotion = max(
        ['anger', 'disgust', 'fear', 'joy', 'sadness'],
        key=lambda k: {'anger': anger_score,
                       'disgust': disgust_score,
                       'fear': fear_score,
                       'joy': joy_score,
                       'sadness': sadness_score}[k]
    )

    # return the correct output format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominate_emotion': dominate_emotion    
    }
