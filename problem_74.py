# Problem 74: Find first non-repeating character
# Find and fix the error

def max_difference(arr):
    if len(arr) < 2:
        return 0, None  
    min_val = arr[0]
    max_diff = arr[1] - arr[0]  
    pair = (arr[0], arr[1])
    
    for i in range(1, len(arr)):
        current_diff = arr[i] - min_val
        if current_diff > max_diff:
            max_diff = current_diff
            pair = (min_val, arr[i])
        if arr[i] < min_val:
            min_val = arr[i]
    
    return max_diff, pair

numbers = [7, 1, 5, 3, 6, 4]
diff, pair = max_difference(numbers)
print(f"Max difference: {diff}, Pair: {pair}")

