from urllib2 import Request, urlopen
from rentFeeLevel import get_tagname_code
import csv

map_address = []
estate_name = []
x_coord = []
y_coord = []
phone = []
address = []
city = []
zipcode = []
fee = []
# zws_id = "X1-ZWz19v596wpma3_1d5w6" # jiahao.luo2014@gmail.com DONE
# zws_id = "X1-ZWz19tpydza9e3_7x5fi" # jluo80@gatech.edu 700 DONE
zws_id = "X1-ZWz1f6smiiks23_7yjzz" # yusu.lo@gmail.com
estatelist_new_fee= []

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

with open("estatelist_new.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader: #reader will read each row when it has been called.
        map_address.append(row)
    # print map_address

# Encode address string to a URL format
    for i in map_address:
        # estate_name.append(i[0])
        # x_coord.append(i[1])
        # y_coord.append(i[2])
        # phone.append(i[3])
        # address.append(i[4])
        i[4] = i[4].replace(" ", "+")
        # city.append(i[5])
        # zipcode.append(i[6])

# Since the API request is limited to 1000 times per day,
# the range each request will be set as [0,700), [700,1458)
# and will be combined later.

#len(map_address)):
for i in range(0,1):
    address = map_address[i][4]
    city = map_address[i][5]
    zipcode = map_address[i][6]
    # break
    # url = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id='+zws_id+'&address='+address+'&citystatezip='+city+'+GA+'+zipcode+'&rentzestimate=true'
    # print url
    # url = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id=X1-ZWz19v596wpma3_1d5w6&address=171+Auburn+Ave&citystatezip=Atlanta+GA&rentzestimate=true'
    url = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id=X1-ZWz19v596wpma3_1d5w6&address=171+Auburn+Ave&citystatezip=Atlanta+GA&rentzestimate=true'
    request = Request(url)
    xml_string = urlopen(request).read()
    fee_level = get_tagname_code(xml_string)
    print fee_level
    map_address[i].append(fee_level)
    estatelist_new_fee.append(map_address[i])
    # print estatelist_new

# Save the valid estate results in Zillow database to estatelist_new.csv file.
# w for writing to the file (causing any existing file with that name to be overwritten),
# or a for appending to the end of an existing file.
with open("estatelist_new_fee.csv","ab") as f:
    writer = csv.writer(f)
    # writer.writerow(["Estate name","X","Y","Phone nunber","address","City","Zipcode","Fee level"])
    writer.writerows(estatelist_new_fee)
    f.close()