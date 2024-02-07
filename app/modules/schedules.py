from dataclasses import dataclass
import json
import logging
import os
from fastapi import APIRouter, Depends, HTTPException, routing, status
from dotenv import load_dotenv
import datetime as dt

import httpx

logger = logging.getLogger(__name__)
log_config_file = "/workspaces/Alteryx-Scheduler/app/app_logger/logging_configs/log_config.json"
with open(log_config_file) as f_in:
    config = json.load(f_in)
    logging.config.dictConfig(config)

load_dotenv()


base_url: str = os.getenv('SERVER_BASE_URL')
api_access_key: str = os.getenv('API_ACCESS_KEY')
api_access_secret: str = os.getenv('API_ACCESS_SECRET')


router = APIRouter()

# create function to check for http/https and adjust tranport flag
def toggleSecureTransport():
    print('base_url has scheme:',httpx.URL(base_url).scheme)
    if httpx.URL(base_url).scheme =='http':
        import os
        print('Adding OAUTHLIB_INSECURE_TRANSPORT flag to environment')
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


# toggleSecureTransport based on base_url
toggleSecureTransport()

try:
    # build auth_data object to retrieve token
    auth_data = {
        'grant_type': 'client_credentials',
        'client_id': api_access_key,
        'client_secret': api_access_secret
    }
    
    token = httpx.post(base_url+'/oauth2/token', data=auth_data)
    token=token.json()
    
    # add field for token expiration date
    token['expires_at']=dt.datetime.utcnow()+dt.timedelta(0,token['expires_in'])

    columns = []
    data = []
    for i in token:
        columns.append(i)
        data.append(token[i])

    outputDF = pd.DataFrame(data=[data], columns=columns)

    # build authorization and baseURL fields
    outputDF['Authorization']='Bearer '+outputDF['access_token']
    outputDF['baseURL']=base_url

    # return token

except urllib3.exceptions.SSLError as e:
    errorDF = pd.DataFrame([{"Error Message":e}])
    Alteryx.write(errorDF,1)
    print(f'Certificate verification failed: {e}')

except requests.exceptions.Timeout as e:
    errorDF = pd.DataFrame([{"Error Message":e}])
    Alteryx.write(errorDF,1)
    print(f'Request timed out: {e}')

# SSL errors will likely show up here because requests is reporting
# the error of an underlying library
except requests.exceptions.ConnectionError as e:
    errorDF = pd.DataFrame([{"Error Message":e}])
    Alteryx.write(errorDF,1)
    print(f'Connection error: {e}')

except requests.exceptions.RequestException as e:
    errorDF = pd.DataFrame([{"Error Message":e}])
    Alteryx.write(errorDF,1)
    print(f'Request exception: {e}')
    
except Exception as e:
    errorDF = pd.DataFrame([{"Error Message":e}])
    print(e)
    Alteryx.write(errorDF,1)


def Alteryx_Oauth():
    
    pass

@dataclass
class Alteryx_Environment:
    id: int
    server_url: str = os.getenv('SERVER_URL')
    api_access_key: str = os.getenv('API_ACCESS_KEY')
    api_access_secret: str = os.getenv('API_ACCESS_SECRET')
