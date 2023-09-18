import requests
import json
from app.Logger import log
from app.models.UserKeys import UserKeys


BaseUri = "http://localhost:8030/api"

session = requests.Session()
session.trust_env = False


def sign_in(user_keys: UserKeys):
    try:
        #ping
        response = session.post(f'{BaseUri}/auth/ping')
        response.raise_for_status()
        ping = response.json()
        log.info("Request ping sucessful")
        #create-session
        payload = {
            'sessionKey': ping['data']['fingerprint'],
            'publicKey': user_keys.publicKey
        }
        response = session.post(f'{BaseUri}/auth/create-session', json=payload)
        response.raise_for_status()
        create_session = response.json()
        log.info("Request create-session sucessful")
        #generate-secret
        payload = {
            'publicKey': user_keys.publicKey,
            'sessionKey': create_session['data']['sessionKey'],
            'username': user_keys.username
        }
        print(payload)
        response = session.post(f'{BaseUri}/auth/generate-secret', json=payload)
        response.raise_for_status()
        generate_secret = response.json()
        log.info("Request create-session sucessful")
    except requests.exceptions.RequestException as error:
        log.error(f"Error in {error.strerror} Request")
        raise error


#         payload = {
#             'publicKey': obj['publicKey'],
#             'sessionKey': auth_state['sessionKey'],
#             'username': obj['username'],
#             'digit': decrypted_digit
#         }
#         response = requests.post('https://your-api-url/auth/sign-in', json=payload)
#         response.raise_for_status()
#         return response.json()

