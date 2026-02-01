# Problem 81: Check if string has balanced brackets
# Find and fix the error

def balanced_brackets(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    closing = {')', ']', '}'}
    
    for char in s:
        if char in pairs:  # opening bracket
            stack.append(char)
        elif char in closing:  # closing bracket
            if not stack:
                return False
            if pairs[stack.pop()] != char:
                return False
    return len(stack) == 0

expr = "{[()]}"
print(f"Balanced: {balanced_brackets(expr)}")

