#! https://blog.wimwauters.com/networkprogrammability/2020-03-19-aci_python_requests/
import requests
import json
from aci_get_token import get_token

tenant_name = "Tenant_Python"

def create_tenant():
  
   token = get_token()

   # retrieve token

   url = "https://sandboxapicdc.cisco.com/api/mo/uni.json"
   
   payload = {
      "fvTenant": {
         "attributes": {
            "name": tenant_name
         }
      }
   }

   headers = {
      "Cookie" : f"APIC-Cookie={token}", 
   }

   requests.packages.urllib3.disable_warnings()
   response = requests.post(url,data=json.dumps(payload), headers=headers, verify=False)
   # dumps payload json to string

   if (response.status_code == 200):
      print("Successfully created tenant")
   else:
      print("Issue with creating tenant")

def get_tenant():
   return tenant_name



if __name__ == "__main__":
   create_tenant()