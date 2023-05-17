"""
A human readable data structure that applications use to store, transfer, and read data

It is designed for the internet
Schema and namespace defines data model
<tag></tag> surround elements for structure and layout
key/value representation  <key>value</key>
Whitespace is not significant

import xmltodict
from pprint import pprint

xml_example = open ("xml_example.xml").read()
pprint(xml_example)
int_name = xml_dict["interface"]["name']
pprint(int_name)
xmlunparsed=xmltodict.unparse(xml_dict)
pprint(xmlunparsed)

"""
