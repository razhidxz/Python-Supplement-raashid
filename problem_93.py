# Problem 93: Find longest common prefix
# Find and fix the error

def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = ""
    for chars in zip(*strs):
        if len(set(chars)) == 1:
            prefix += chars[0]
        else:
            break
    return prefix

