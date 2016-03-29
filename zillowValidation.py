from urllib2 import Request, urlopen
import csv
import xml.dom.minidom

# existenceCheck.py
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

place_id = []
map_address = []
estate_name = []
x_coord = []
y_coord = []
phone = []
address = []
city = []
zipcode = []

zws_id = []
zws_id.append("X1-ZWz1f7h2iat91n_5dugt") # 446042552@qq.com DONE
zws_id.append("X1-ZWz19v596wpma3_1d5w6") # jiahao.luo2014@gmail.com DONE
zws_id.append("X1-ZWz19tpydza9e3_7x5fi") # jluo80@gatech.edu 700 DONE
zws_id.append("X1-ZWz1f6smiiks23_7yjzz") # yusu.lo@gmail.com

estate_final = []

# The parameters of the API are:

# PARAMETER      DESCRIPTION                                                                    REQUIRED
# zws-id         The Zillow Web Service Identifier.                                             Yes
# address        The address of the property to search.                                         Yes
# citystatezip   The city+state combination and ZIP code for which to search.
#                Note that giving both city and state is required.                              Yes
# rentzestimate  Return Rent Zestimate information. (boolean true/false, default: false)        No

# Zillow API example:
# GetDeepSearchResults.htm?zws-id=X1-ZWz19v596wpma3_1d5w6&address=150+Old_Ivy+St&citystatezip=Atlanta+GA&rentzestimate=true

# Zillow format notes:
# 1. case-insensitive.
# 2. address parameters can be concatenated by "+" sign.
# 3. Zillow will auto-detect the address by the first two characters.(which is kind of weird.)

with open("estate_0319.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader: #reader will read each row when it has been called.
        map_address.append(row)
    # print map_address
# Encode address string to a URL format

    for i in map_address:
        # place_id.append(i[0])
        # estate_name.append(i[1])
        # x_coord.append(i[2])
        # y_coord.append(i[3])
        # phone.append(i[4])
        # address.append(i[5])
        i[5] = i[5].replace(" ", "+")
        # city.append(i[6])
        i[6] = i[6].replace(" ", "+")
        # zipcode.append(i[7])

# Since the API request is limited to 1000 times per day,
# the range each request will be set as [0,700), [700,1458)
# and will be combined later.

#len(map_address)):
for i in range(21,30):
    address = map_address[i][5]
    city = map_address[i][6]
    zipcode = map_address[i][7]
    # break
    url = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id='+zws_id[2]+'&address='+address+'&citystatezip='+city+'+GA+'+zipcode+'&rentzestimate=true'
    # print url
    # url = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id=X1-ZWz19v596wpma3_1d5w6&address=171+Auburn+Ave&citystatezip=Atlanta+GA&rentzestimate=true'
    request = Request(url)
    xml_string = urlopen(request).read()
    status = get_valid_exist(xml_string)
    # print status
    if status:
        # print map_address[i][5]
        map_address[i][5] = map_address[i][5].replace("+", " ")
        map_address[i][6] = map_address[i][6].replace("+", " ")
        estate_final.append(map_address[i])
    # print estate_final
        print url

# Save the valid estate results in Zillow database to estatelist_new.csv file.
# w for writing to the file (causing any existing file with that name to be overwritten),
# or a for appending to the end of an existing file.
with open("estate_final.csv","ab") as f:
    writer = csv.writer(f)
    # writer.writerow(["Place ID","Estate name","X","Y","Phone nunber","Address","City","Zipcode"])
    writer.writerows(estate_final)
    f.close()