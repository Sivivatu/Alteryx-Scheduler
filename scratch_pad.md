docker run --hostname=3c08ac278ba1 --env=POSTGRES_USER=postgres --env=POSTGRES_DB=postgres --env=POSTGRES_PASSWORD=postgres --env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/16/bin --env=GOSU_VERSION=1.16 --env=LANG=en_US.utf8 --env=PG_MAJOR=16 --env=PG_VERSION=16.1-1.pgdg120+1 --env=PGDATA=/var/lib/postgresql/data --volume=/var/lib/postgresql/data --network=alteryx-scheduler_devcontainer_default --restart=unless-stopped --label='com.docker.compose.config-hash=43618a57865b8e2122e328843ac91c8b8cac678918ed9aa34052008eefe66247' --label='com.docker.compose.container-number=1' --label='com.docker.compose.depends_on=' --label='com.docker.compose.image=sha256:75b7bff7c3ad1ae4468a2107724459061dc87d2176f8f02747a360c32b8c58b9' --label='com.docker.compose.oneoff=False' --label='com.docker.compose.project=alteryx-scheduler_devcontainer' --label='com.docker.compose.project.config_files=/workspaces/Alteryx-Scheduler/.devcontainer/docker-compose.yml,/tmp/devcontainercli-root/docker-compose/docker-compose.devcontainer.build-1706208978333.yml,/tmp/devcontainercli-root/docker-compose/docker-compose.devcontainer.containerFeatures-1706208978890.yml' --label='com.docker.compose.project.working_dir=/workspaces/Alteryx-Scheduler/.devcontainer' --label='com.docker.compose.service=db' --label='com.docker.compose.version=2.12.2' --runtime=runc -d postgres:latest


### possible db url
DATABASE_URL=postgresql+asyncpg://postgres:postgres@alteryx-scheduler_devcontainer-db-1:5432/axy_scheduler



```python
#################################
# List all non-standard packages to be imported by your 
# script here (only missing packages will be installed)
# from ayx import Package
# Package.installPackages(['oauthlib','requests-oauthlib'])


#################################
from ayx import Alteryx, Package
import pandas as pd
import datetime as dt
from urllib.parse import urlparse
import requests
import urllib3.exceptions

missingPackageArray=[]

try:
    import pip_system_certs
except:
    print("Checking for missing packages")
    packages=['pip_system_certs']
    for package in packages:
        if Package.isPackageInstalled(package)==False:
#             print("Package not found: "+package)
            missingPackageArray.append(package)
    
if missingPackageArray!=[]:
    missingPackageDF=pd.DataFrame(data=missingPackageArray,columns=['MissingPackage'])
    print(missingPackageDF)
    Alteryx.write(missingPackageDF,5)


inputDF = Alteryx.read("#1")


#################################
# create function to check for http/https and adjust tranport flag
def toggleSecureTransport():
    print('baseUrl has scheme:',urlparse(baseUrl).scheme)
    if urlparse(baseUrl).scheme =='http':
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
    
```