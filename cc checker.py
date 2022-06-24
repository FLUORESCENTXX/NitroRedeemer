import requests
import os
import json

def checker
url  = 'https://api.stripe.com/v1/tokens'
    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'origin': 'https://checkout.stripe.com',
        'sec-fetch-dest': 'empty',
        'accept-language': 'en-GB',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'referer': 'https://checkout.stripe.com/m/v3/index-',
    }
  
  
data = { 

 'ccnumber' 
 'ccexpdate'
 'cccvv'
}

try:
  response = requests.post(url,headers=headers)
  
 

 if (responser.status_code == 200):
    print("Card is unavaliable")
    else
    
  print("Card is valid")
