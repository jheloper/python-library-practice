import json
from decimal import Decimal

data = [{'id': 123, 'entities': {'url': 'python.org', 'hashtags': ['#python', '#pythonkor']}}]
print(json.dumps(data, indent=2))

json_str = '["ham", 1.0, {"a": false, "b": null}]'
print(json.loads(json_str))
print(json.loads(json_str, parse_float=Decimal))

with open('./sample.json', mode='r') as f:
    json_string = json.load(f)

print(json.dumps(json_string, indent=2))

json_string[0]['entities']['hashtags'].append('#pyhack')
with open('dump.json', mode='w') as f:
    json.dump(json_string, f, indent=2)