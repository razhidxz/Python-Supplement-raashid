# Problem 89: Check if number is palindrome
# Find and fix the error

def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

print(f"Is 121 palindrome? {is_palindrome_number(121)}")
