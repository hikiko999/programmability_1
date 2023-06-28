#! https://blog.wimwauters.com/networkprogrammability/2020-01-14-parse_yaml_python/
import yaml
from pprint import pprint

with open("sample.yaml") as f:
    yml_file = f.read()
pprint(yml_file)
yml_dict = yaml.load(yml_file,yaml.SafeLoader)
# convert string to python dict

print(yml_dict)
tenant_name = yml_dict['tenant']
vrf_name = yml_dict['vrf']
bd_name = yml_dict['bridge_domains'][0]['bd']
# bridge_domains is a list

print("The variables are: ")
print(f"Tenant name {tenant_name}")
print(f"VRF name {vrf_name}")
print(f"BD name {bd_name}")