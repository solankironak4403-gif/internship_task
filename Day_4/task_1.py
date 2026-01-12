# Function to Calculate Mean of a List

def calculate_mean(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

data = [10, 20, 30, 40, 50]
mean_value = calculate_mean(data)

print("Mean:", mean_value)

    