import json
from solution import isAccessible
from solution import bubbleSort


with open('Data/mockData.json', 'r') as file: 
    mockData = json.load(file)

print('MOCK DATA')
#print(mockData)

accessibleData = isAccessible(mockData)
#print(accessibleData)

sorted_data = bubbleSort(accessibleData)
# Santity check
#for i in range(len(sorted_data)): 
#    print(sorted_data[i]['distance'], ' -- ', sorted_data[i]['accessible'])