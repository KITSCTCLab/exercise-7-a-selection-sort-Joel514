from typing import List

def selectionSort(array, size):
  for j in range (0,size-1):
    smallest = j
    for i in range (j+1,size):
     if (array[ i ] < array[ smallest]):
      smallest= i
    array[ j ], array[ smallest ]= array[ smallest ],array[j]
  return array
# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
