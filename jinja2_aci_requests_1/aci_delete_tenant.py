#! https://blog.wimwauters.com/networkprogrammability/2020-03-19-aci_python_requests/
import requests
import json
from aci_get_token import get_token

def delete_tenant():
   token = get_token()

   url = "https://sandboxapicdc.cisco.com/api/mo/uni.json"
   

   payload = {
      "fvTenant": {
         "attributes": {
            "name": "Tenant_Python",
            "status": "deleted"
         }
      }
   }

   headers = {
      "Cookie" : f"APIC-Cookie={token}", 
   }

   requests.packages.urllib3.disable_warnings()
   response = requests.post(url,data=json.dumps(payload), headers=headers, verify=False)
   
   if (response.status_code == 200):
      print("Successfully deleted tenant")
   else:
      print("Issue with deleting tenant")

if __name__ == "__main__":
   delete_tenant()