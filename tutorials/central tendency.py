import statistics

# Sample dataset
data = [15, 16, 14, 15, 17, 16, 15, 18, 15]

# Calculate Mean (Arithmetic Representation)
mean_value = sum(data) / len(data)  
# Formula: Mean = (Sum of all values) / (Number of values)
# Mean = (15 + 16 + 14 + 15 + 17 + 16 + 15 + 18 + 15) / 9

# Calculate Median (Middle Value)
median_value = statistics.median(data)  
# Sorted data: [14, 15, 15, 15, 15, 16, 16, 17, 18]
# Median is the middle value (5th value): 15

# Calculate Mode (Most Frequent Value)
mode_value = statistics.mode(data)  
# The most frequent number is 15 (appears 4 times)

# Display Results
print(f"Mean: {mean_value} (Calculated as: (Sum of values) / (Count))")
print(f"Median: {median_value} (Middle value of sorted data)")
print(f"Mode: {mode_value} (Most frequently occurring value)")
