#! https://blog.wimwauters.com/networkprogrammability/2020-02-27-aci_python_requests_jinja_part1/
# from jinja2 import Template
import jinja2
"""
template = Template("Hello{{something}}!")
print(template.render(something="World!"))

template_vars = {
    "vlan_id": 620,
    "vlan_name": "vlan-620"
}

vlan_template = """
#vlan {{ vlan_id }}
#    name {{ vlan_name }}
"""

template = jinja2.Template(vlan_template)
print(template.render(template_vars))
"""

vlans = {
   "620": "VLAN-620",
   "621": "VLAN-621", 
   "622": "VLAN-622", 
   "633": "VLAN-623",   
}

template_vars = {
   "vlans": vlans
   # dictionary
}

vlan_template = """
{%- for vlan_id, vlan_name in vlans.items() %}
vlan {{ vlan_id }}
   name {{ vlan_name }}
{%- endfor %}
"""
# (-) for no whitespace

template = jinja2.Template(vlan_template)
print(template.render(template_vars))