#! https://blog.wimwauters.com/networkprogrammability/2020-02-27-aci_python_requests_jinja_part1/
import yaml
from jinja2 import Environment, FileSystemLoader

loopbacks = yaml.load(open('loopback.yml'), Loader=yaml.SafeLoader)

env = Environment(loader = FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('loopback.j2')
loopback_config = template.render(loopbacks)

print(loopback_config)
