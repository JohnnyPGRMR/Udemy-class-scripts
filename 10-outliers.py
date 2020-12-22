data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 
        160, 170, 183, 185, 187, 188, 191, 350, 360]
# Delete first two entries.
# del data[0:2]
# print(data)
# # make sure it's position 14 since I already deleted the first two entries.
# del data[14:]
# print(data)

############### Create an automated sorter to automatically eliminate rogue data. #########################

min_valid = 100
max_valid = 200

# This doesn't work for the same reason as in the last code block above.

# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]

########### This method below only works on ordered lists. #####################
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)  # for debugging.
del data[:stop]
print(data)