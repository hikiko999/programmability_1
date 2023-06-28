#! https://blog.wimwauters.com/networkprogrammability/2020-01-11-parse_json_python/
import json

with open('sample.json') as f:
    json_content = f.read()
    # reads it to string

json_dict = json.loads(json_content)
# print(json_dict)
# print(type(json_dict))
# returns dict

customers = json_dict['Root']['Customers']
orders = json_dict['Root']['Orders']

"""
for customer in customers['Customer']:
   print(f"Customer ID: {customer['@CustomerID']}")
   print(f"Company Name: {customer['CompanyName']}")
   print(f"Contact Name: {customer['ContactName']}")
   print(f"  ==>  Street: {customer['FullAddress']['Address']}")
   print(f"  ==>  City: {customer['FullAddress']['City']}")
   print(50* "-")
"""

customer_list = []

for customer in customers['Customer']:
    customer_list.append(customer['@CustomerID'])

for customer in customer_list: 
   print(f"Orders for: {customer}")
   for order in orders['Order']:
      if(customer == order['CustomerID']):
         print(f"  ==>Employee {order['EmployeeID']} placed an order on {order['OrderDate']}")
