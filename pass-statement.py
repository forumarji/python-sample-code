# The pass statement done nothing.
# It can be used when statement is required systactically but the program requires no action
# This is commonly used for creating minimul classes:
class MyEmptyClass:
    pass

# Another place pass can be used is as place-holder for function or conditional body when you are working on new code,
# allowing to keep thinking at a more abstract level.
# The pass is silently ignored
def initlog(*args):
        pass # Remember to implement this!

while True:
    pass # Busy-wait for keyboard interrupt (Ctrl+c)
