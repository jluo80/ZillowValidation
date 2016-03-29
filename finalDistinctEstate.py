import csv

# remove duplicate addresses
# A set is an unordered collection with no duplicate elements.
# Basic uses include membership testing and eliminating duplicate entries.
# Set objects also support mathematical operations like union, intersection,
# difference, and symmetric difference.
def remove_duplicates(map_address):
    output = []
    seen = set()
    for i in map_address:
        value = i[5]
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(i)
            seen.add(i[5])
    return output

map_address = []
address_left = []
with open("estate_final.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader: #reader will read each row when it has been called.
        map_address.append(row)
    # print map_address
    address_left = remove_duplicates(map_address)

with open("estate_final_distinct.csv","ab") as f:
    writer = csv.writer(f)
    # writer.writerow(["Place ID","Estate name","X","Y","Phone nunber","Address","City","Zipcode"])
    writer.writerows(address_left)
    f.close()