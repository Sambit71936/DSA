# When a function calls itself is called recursion.

def greet():
    print("Hello, World!")
    greet()# This will lead to infinite recursion
def greet():
    print("Hello, World!")
    greet()# This will lead to infinite recursion


greet()