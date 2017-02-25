# Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence. For example (no pun intended):
# Measure some strings:
words = ['Java', 'PHP', 'Python']
print("Length of Strings in list")
for w in words:
    print(w, len(w))

# Loop over a slice copy of the entice list
for w in words[:]:
    if len(w) > 5:
        print("If Length of item > 5, Insert Item at the index 0")
        words.insert(0,'C')

print(words)
