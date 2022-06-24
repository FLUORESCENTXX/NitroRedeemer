import requests
import os
import re
import time
import json
os.system("cls")
os.system(f"title Discord-Checker Codes")

with open('token.json', 'r') as fp:
    cfg = json.loads(fp.read())
    print('Config Loaded')

def check(nitro):
    header = {"authorization": cfg['token']}
    url = 'https://discordapp.com/api/v9/entitlements/gift-codes/{}?with_application=false&with_subscription_plan=true'.format(nitro)
    r = requests.get(url, headers=header)
    get_json = r.json()
    if r.status_code == 429:
        time.sleep(70)
        print('LIMIT SLEEP 70 SEC')
    if r.status_code == 200:
        if get_json['promotion']['inbound_body_text'] == 'We hope you enjoy your 3 free months of Nitro.':
            print("Code: {} - valid".format(nitro))
            with open("valid.txt", "a") as f:
                f.write('{}'.format(nitro) + '\n')
    else:
        print("Code: {} - invalid".format(nitro))


f = open('codes.txt', 'r') 
Lines = f.readlines()
for line in Lines:
    nitro_code = re.search('https://discord.com/billing/promotions/(.+)', line.strip())
    if nitro_code:
        print('Check code: {}'.format(nitro_code.group(1)))
        check(nitro_code.group(1))
