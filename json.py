"""
JSON
A human readable data structure that applications use to store, transfer, and read data
A data-interchange text format
Notated with {} for objects and [] for arrays
key/value representation -> "key":value
Whitespace is not significant

Data surrouded by {}
An object can contain other objects or data entries
Key/vale set separated by comma
No comma at the end

import json
from pprint import pprint

json_example = open ("json_example.json").read()
pprint(json_example)

json_python = json.loads(json_example)
pprint(json_python)

int_name = json_python["ietf-interfaces:interface"]["name"]
print(int_name)

pprint(json.dumps(json_python)


