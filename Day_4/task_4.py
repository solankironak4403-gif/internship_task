# Function to Find Maximum and Minimum Values

def find_max_min(numbers):
    return max(numbers), min(numbers)

data = [23, 45, 12, 67, 34]
maximum, minimum = find_max_min(data)

print("Maximum:", maximum)
print("Minimum:", minimum)