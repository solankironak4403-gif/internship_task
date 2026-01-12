#Real-World Data Analysis Workflow (Mini Simulation)

raw_data = ["23", "45", "NA", "34", "", "56", "error", "42"]

clean_data = []

for value in raw_data:
    try:
        clean_data.append(int(value))
    except ValueError:
        continue

print("Cleaned Data:", clean_data)
