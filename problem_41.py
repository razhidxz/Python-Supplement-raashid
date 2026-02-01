# Problem 41: Find index of element in list
# Find and fix the error

numbers = [10, 20, 30, 40, 50]
search = 30

index = numbers.index(search) if search in numbers else -1
print(f"Index of {search}: {index}")

