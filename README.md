# uaa_access_jwt
contains a script for getting uaa access token in jwt form

## Description: 
This script is used to get the access token from UAA server

## Usage: 
- Create a virtual environment: python3 -m venv venv
- Activate Virtual Environment: source venv/bin/activate
- Install dependencies: pip install -f requirements.txt
- Run the script with the following arguments:
'''
python get_uaa_access_token.py --url <uaa_url> --client_id <client_id> --client_secret <client_secret> --username <username> --password <password>
'''

## Example: 
'''
python get_uaa_access_token.py --url https://uaa.system-domain.com --client_id client_id --client_secret client_secret --username username --password password
'''
Output: access_token
