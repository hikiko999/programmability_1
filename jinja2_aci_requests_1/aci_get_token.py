#! https://blog.wimwauters.com/networkprogrammability/2020-03-19-aci_python_requests/
# not jinja

import json
import requests


def get_token():  
   url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json" # "https://10.48.109.10/api/aaaLogin.json"

   payload = {
      "aaaUser": {
         "attributes": {
            "name":"admin",
            "pwd":"!v3G@!4@Y"
         }
      }
   }

   # prepare payload

   headers = {
      "Content-Type" : "application/json"
   }

   # create headers

   requests.packages.urllib3.disable_warnings()
   response = requests.post(url,data=json.dumps(payload), headers=headers, verify=False).json()

   token = response['imdata'][0]['aaaLogin']['attributes']['token']
   return token

   # send request

def main():
   token = get_token()
   print("The token is: " + token)

if __name__ == "__main__":
   main()
