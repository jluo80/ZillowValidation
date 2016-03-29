import xml.dom.minidom
# Parse XML data structure by specific node.
# When return error code is 0, it means "Request successfully processed".
# Otherwise, request failed.
def get_tagname_code(input_xml_string):
    dom = xml.dom.minidom.parseString(input_xml_string)
    collection = dom.documentElement
    for node in dom.getElementsByTagName('amount'):
        if node.parentNode.tagName == "rentzestimate":
            fee = (int) (node.firstChild.nodeValue)
            if(fee > 0 and fee <= 600):
                return "600"
            elif(fee > 600 and fee <= 800):
                return "800"
            elif(fee > 800 and fee <= 1000):
                return "1000"
            elif(fee > 1000 and fee <= 1200):
                return "1200"
            elif(fee > 1200 and fee <= 1400):
                return "1400"
            elif(fee > 1400 and fee <= 1600):
                return "1600"
            elif(fee > 1600 and fee <= 1800):
                return "1800"
            else:
                return "over $1800"
