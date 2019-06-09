import xml.etree.ElementTree as ET

tree = ET.parse('AmazonReview.xml')
root = tree.getroot()

count=0
for item in root.findall('item'):
    count +=1
    num = ET.Element("num")
    num.text = str(count)
    num.tail = '\n'
    item.insert(0,num)

    tree.write("AmazonReview.xml", encoding="utf-8", xml_declaration=True)

