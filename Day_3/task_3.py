# find unique elements and theire frequency 
elements = [1, 2, 2, 3, 4, 4, 4, 5]
frequency = {}
for element in elements:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1
print("Element frequencies:", frequency)

