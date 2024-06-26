'''
any

Function to check if any element of an iterable is True.

Syntax
any(iterable)

Parameters
iterable: The iterable to check.

Returns
True if any element of an iterable is True, otherwise False.
'''

a = []
b = ('A')
c = [False]

print(any(a)) # False
print(any(b)) # True
print(any(c)) # False