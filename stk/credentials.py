import json 
import base64
from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv


load_dotenv()

#apis are also authenticated

class Credentials:
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret =os.getenv("CONSUMER_SECRET")
    passkey = os.getenv('PASSKEY')

    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    #if i go live, the sandbox part will be replaced with live etc
class MpesaAccessToken:
    #the token is given by mpesa 
    token = requests.get(Credentials.api_url,auth= HTTPBasicAuth(Credentials.consumer_key,Credentials.consumer_secret))
    #however , saf have to auth us, thus we now use auth, to be able to access the 
    access_token = json.loads(token.text)
    #converts the token in json form
    validated_token = access_token['access_token']

class MpesaPassword:
    shortcode = "174379"
    passkey= Credentials.passkey
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

    encode_str =  shortcode + passkey + timestamp 

    # this hashes it
    encoded = base64.b64encode(encode_str.encode())

    # decoded_password = base64.b64decode(encoded.decode())
    decoded_password = encoded.decode('utf-8')

    

