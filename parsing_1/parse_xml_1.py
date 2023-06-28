#! https://blog.wimwauters.com/networkprogrammability/2020-01-09-parse_xml_python/
import xmltodict

with open('sample.xml') as f:
    xml_content = f.read()

xml_dict = xmltodict.parse(xml_content)

customers = xml_dict['Root']['Customers']
orders = xml_dict['Root']['Orders']

customer_list = []
for customer in customers['Customer']:
   customer_list.append(customer['@CustomerID']) 
   # customer_list = ['GREAL', 'HUNGC', 'LAZYK', 'LETSS']

for customer in customer_list: 
   print(f"Orders for: {customer}")
   for order in orders['Order']:
      if(customer == order['CustomerID']):
         print(f"  ==>Employee {order['EmployeeID']} placed an order on {order['OrderDate']}")

"""
for customer in customers['Customer']:
    print(f"Customer ID: {customer['@CustomerID']}") 
    # @ for parameters within tags
    print(f"Company Name: {customer['CompanyName']}")
    print(f"Contact Name: {customer['ContactName']}")
    print(f"  ==>  Street: {customer['FullAddress']['Address']}")
    print(f"  ==>  City: {customer['FullAddress']['City']}")
    print(50 * "-")
"""