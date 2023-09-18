import json
from app.Logger import log
from app.models.UserKeys import UserKeys
import app.APIHandler as API

def write_user_cache(user_keys, serverdata):
    try:
        user_data = {
            'username': user_keys.username,
            'publicKey': user_keys.publicKey,
            'privateKey': user_keys.privateKey,
            'serverdata': serverdata['data']
        }

        with open('user_cache.json', 'w') as file:
            json.dump(user_data, file)
        
        log.info('User cache updated')
    except Exception as e:
        log.error(f'Error writing usercache file: {str(e)}')
    

def sign_in(user_keys: UserKeys):
    try:
        validate(user_keys)
        Serverdata = API.sign_in(user_keys)
        #write_user_cache(user_keys, Serverdata)
    except Exception as e:
        log.error(f"Signin in failed: {e}")
        
def validate(user_keys):
    if user_keys.username=="" or user_keys.publicKey==""  or user_keys.privateKey=="" :
        raise Exception("ValidationException")
