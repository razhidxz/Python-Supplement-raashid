# Problem 92: Check if all elements are unique
# Find and fix the error

def all_unique(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return False
        seen.add(item)
    return True
