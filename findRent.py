import urllib2

# def estate_detail(website):
website = "http://www.zillow.com/homedetails/1000-Northside-Dr-NW-131362-Atlanta-GA-30318/2113036558_zpid/"
response = urllib2.urlopen(website)
pageSource = response.read()
rentPos = pageSource.find('"For rent: $')
print rentPos
if rentPos != -1:
    rentFeeBeg = pageSource.find("$",rentPos)
    rentFeeEnd = pageSource.find('"',rentPos)
    fee = pageSource[rentFeeBeg+1:rentFeeEnd]
    fee = fee.replace(",","")
    print fee
else:
    print "Off Market"