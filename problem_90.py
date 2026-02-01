# Problem 90: Find median of a list
# Find and fix the error

def find_median(lst):
    lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    return (lst[mid] + lst[-mid-1]) / 2 if n % 2 == 0 else lst[mid]
