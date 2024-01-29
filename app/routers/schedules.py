from dataclasses import dataclass
import json
import logging
import os
from fastapi import APIRouter, Depends, HTTPException, routing, status
from dotenv import load_dotenv

import httpx

logger = logging.getLogger(__name__)
log_config_file = "/workspaces/Alteryx-Scheduler/app/app_logger/logging_configs/log_config.json"
with open(log_config_file) as f_in:
    config = json.load(f_in)
    logging.config.dictConfig(config)

load_dotenv()
router = APIRouter()

# create function to check for http/https and adjust tranport flag
def toggleSecureTransport():
    print('baseUrl has scheme:',httpx.URL(baseUrl).scheme)
    if httpx.URL(baseUrl).scheme =='http':
        import os
        print('Adding OAUTHLIB_INSECURE_TRANSPORT flag to environment')
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

baseUrl = inputDF.baseURL[0]

# toggleSecureTransport based on baseUrl
toggleSecureTransport()

try:
    # build auth_data object to retrieve token
    auth_data = {
        'grant_type': 'client_credentials',
        'client_id': inputDF.apiAccessKey[0],
        'client_secret': inputDF.apiAccessSecret[0]
    }
    
    token = requests.post(baseUrl+'/oauth2/token', data=auth_data)
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
    outputDF['baseURL']=baseUrl

    Alteryx.write(outputDF,3)



def Alteryx_Oauth():
    
    pass

@dataclass
class Alteryx_Environment:
    id: int
    server_url: str = os.getenv('SERVER_URL')
    api_access_key: str = os.getenv('API_ACCESS_KEY')
    api_access_secret: str = os.getenv('API_ACCESS_SECRET')

@router.get("/schedules", Depends(Alteryx_Oauth))
async def get_schedules():
    return {"message": "Hello World"}