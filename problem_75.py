# Problem 75: Check if parentheses are balanced
# Find and fix the error

def are_balanced(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

expr = "((a + b) * (c - d))"
print(are_balanced(expr))  # True
