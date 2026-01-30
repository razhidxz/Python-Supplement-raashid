# Problem 18: Count words in a sentence
# Find and fix the error

def count_words(sentence):
    return len(sentence.split())

sentence = "Python is a great programming language"
word_count = count_words(sentence)
print(f"Number of words: {word_count}")
