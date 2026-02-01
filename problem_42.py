# Problem 42: Convert list to string
# Find and fix the error

words = ["Hello", "World", "Python"]
sentence = ""
for word in words:
    sentence += word + " "
sentence = sentence.strip()  # remove trailing space

print(f"Sentence: {sentence}")

