#find second largest number in a list

numbers = [10, 20, 4, 45, 99, 99, 45]
unique_numbers = list(set(numbers))  
unique_numbers.sort()  
second_largest = unique_numbers[-2] 
print("The second largest number is:", second_largest)