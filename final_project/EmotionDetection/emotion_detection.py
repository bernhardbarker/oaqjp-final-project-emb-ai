import requests
import json

def emotion_detector(text_to_analyse: str) -> dict:
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(URL, headers=HEADERS, json={
        "raw_document": {
            "text": text_to_analyse
        }
    })
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }
    emotions = json.loads(response.text)["emotionPredictions"][0]["emotion"]
    dominant = next(key for key in emotions if emotions[key] == max(emotions.values()))
    emotions["dominant_emotion"] = dominant
    return emotions
