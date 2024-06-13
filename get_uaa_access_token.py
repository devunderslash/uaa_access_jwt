# Description: This script is used to get the access token from UAA server
# Usage: 
# - Create a virtual environment: python3 -m venv venv
# - Activate Virtual Environment: source venv/bin/activate
# - Install dependencies: pip install -f requirements.txt
# - Run the script with the following arguments:
#       python get_uaa_access_token.py --url <uaa_url> --client_id <client_id> --client_secret <client_secret> --username <username> --password <password>
# Example: python get_uaa_access_token.py --url https://uaa.system-domain.com --client_id client_id --client_secret client_secret --username username --password password
# Output: access_token

import requests
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--url", help="uaa url without the appended /oauth/token path")
parser.add_argument("--client_id", help="uaa client_id")
parser.add_argument("--client_secret", help="uaa client_secret")
parser.add_argument("--username", help="uaa username")
parser.add_argument("--password", help="uaa password")
args = parser.parse_args()

url = args.url + "/oauth/token"

headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

data = f"client_id={args.client_id}&client_secret={args.client_secret}&username={args.username}&password={args.password}&grant_type=password"

response = requests.post(url, headers=headers, data=data)
access_token = response.json()["access_token"]

print(access_token)
