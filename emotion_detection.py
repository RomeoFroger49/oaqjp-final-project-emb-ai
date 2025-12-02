import requests, json

def predict_emotion(text_to_analyse):
    """
    Function to predict the emotion of a given text.
    """

    api_url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(api_url, json=payload, headers=header)

    formatted_response = json.loads(response.text)

    return formatted_response
