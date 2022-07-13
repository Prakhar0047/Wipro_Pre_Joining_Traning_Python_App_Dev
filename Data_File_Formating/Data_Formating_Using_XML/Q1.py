import xml.etree.ElementTree as ET

tree = ET.parse("sample.xml")
root = tree.getroot()

for child in root:

  print(child.attrib)
  # Printing Attribute and Tags, type(ch) == dict
  ch = child.attrib
  ch_tags = child.tag

  for val in child:
    print("Tag: ", val.tag)
    print("Values: ", val.text)
