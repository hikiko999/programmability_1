#! https://blog.wimwauters.com/networkprogrammability/2020-02-27-aci_python_requests_jinja_part1/

from jinja2 import Environment
from jinja2 import FileSystemLoader
import yaml

my_template = Environment(loader=FileSystemLoader('.'))
# location of vlans

"""
vlans = {
   "620": "VLAN-620",
   "621": "VLAN-621", 
   "622": "VLAN-622", 
   "623": "VLAN-623",  
}
"""

vlans = yaml.load(open('vlans.yml'), Loader=yaml.SafeLoader)

template = my_template.get_template("vlans.j2")
# get template from file

result = template.render(vlans=vlans)
print(result)