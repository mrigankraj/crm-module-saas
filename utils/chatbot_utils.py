import requests
from config import config

def get_chatbot_response(message, context):
    response = requests.post(
        'https://api.chatbot.com/v1/message',
        headers={'Authorization': f'Bearer {config.CHATBOT_API_KEY}'},
        json={'message': message, 'context': context}
    )
    return response.json()
