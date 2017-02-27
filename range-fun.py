# If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:
print("range() function")
for i in range(5):
    print(i, end=',')
print("\nrange(5, 10) function")
for i in range(5, 10):
    print(i, end=',')
print("\nrange(0, 10, 3) function - here 3 is increament/step")
for i in range(0, 10, 3):
    print(i, end=',')
print("\nrange(-10, -100, -30) function - here -30 is increament/step")
for i in range(-10, -100, -30):
    print(i, end=',')

#To iterate over the indices of a sequence, you can combine range() and len() as follows:
print("\nTo iterate over the indices of a sequence")
a = ['I','Love','Python']
for i in range(len(a)):
    print(i, a[i])

print(range(10)) # It is an object which returns the successive items of the desired sequence when you iterate over it

print(list(range(5)))
