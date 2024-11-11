import json

with open('Data/data.json', 'r') as file: 
    data = json.load(file)


def isAccessible(data):
    accessibleData = []
    for i in range(len(data)):
        if data[i]['accessible'] == True:
            accessibleData.append(data[i])

    return accessibleData

accessibleData = isAccessible(data)
#print(accessibleData)

# printing data to see if I can print it
# print(data)

# grabbing distance from data test
#print(data[0]['distance'])

def bubbleSort(data):
    # size is the number of entries in the data
    size = len(data)
    for i in range(size):
        swapped = False
        for j in range(0, size - i - 1):
            if data[j]['distance'] < data[j + 1]['distance']:
                # swapping of the data
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped: break

    return data


print("final answer:")
sorted_data = bubbleSort(accessibleData)
print(json.dumps(bubbleSort(sorted_data), indent = 4))


# Santity check
#for i in range(len(sorted_data)): 
#    print(sorted_data[i]['distance'], ' -- ', sorted_data[i]['accessible'])