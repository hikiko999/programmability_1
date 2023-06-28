#! https://www.geeksforgeeks.org/python-xml-to-json/#
import json
import xmltodict
# xmltodict is a Python module that makes working with XML feel 
# like you are working with JSON

with open("sample.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
    # creates json object

json_data = json.dumps(data_dict)
# json => string

# print(json.loads(json_data))
# string => json

with open("sample.json", "w") as json_file:
    json_file.write(json_data)