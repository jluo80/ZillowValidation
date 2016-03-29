import xml.dom.minidom
# Parse XML data structure by specific node.
# When return error code is 0, it means "Request successfully processed".
# Otherwise, request failed.
def get_valid_exist(input_xml_string):
    dom = xml.dom.minidom.parseString(input_xml_string)
    for node in dom.getElementsByTagName('code'):
        if node.parentNode.tagName == "message" and node.firstChild.data == '0':
            if len(dom.getElementsByTagName('rentzestimate')) != 0:
                return True
        else:
            return False
