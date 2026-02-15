# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder:Riddhi
# Date:11/02/2026

print("--- Extracting Words from Text File ---\n")
length = int(input("Enter Length of Words: "))

with open("story.txt", "r") as file:
    text = file.read()

words = text.split()

result = set()

for word in words:
    word = word.lower()
    if len(word) == length:
        result.add(word)

sorted_words = sorted(result)

print(f"Following Unique words of length {length} present: {sorted_words}")




