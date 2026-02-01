# Problem 65: Check if list has duplicates
# Find and fix the error

def has_duplicates(lst):
    seen = []
    for item in lst:
        if item in seen:
            return True
        seen.append(item)
    return False

numbers = [1, 2, 3, 4, 5]
print(f"Has duplicates: {has_duplicates(numbers)}")

