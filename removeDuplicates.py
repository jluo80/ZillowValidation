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