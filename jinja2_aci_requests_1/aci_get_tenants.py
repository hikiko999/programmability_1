#! https://blog.wimwauters.com/networkprogrammability/2020-03-19-aci_python_requests/
import requests
import json
from aci_get_token import get_token

def get_tenants():
   token = get_token()
   # uses get_token function from aci_get_token

   url = "https://sandboxapicdc.cisco.com/api/node/class/fvTenant.json"
   
   headers = {
      "Cookie" : f"APIC-Cookie={token}", 
   }

   # uses token for cookie

   requests.packages.urllib3.disable_warnings()
   response = requests.get(url, headers=headers, verify=False)

   return response

if __name__ == "__main__":
   response = get_tenants().json()
   # converts into json
   # https://www.geeksforgeeks.org/response-json-python-requests/#
   # json read as dict
   tenants = response['imdata']
   # manipulate imdata key
   
   for tenant in tenants:
      print(f"Tenant name: {tenant['fvTenant']['attributes']['name']}")