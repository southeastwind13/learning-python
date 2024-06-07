'''
all

Function to check all elements in an iterable are true.

Syntax
all(iterable)

Parameters
iterable: The iterable to check.    

Returns
True if all elements are true, otherwise False.
'''

a = []
b = [1, 2, 3 ,4]
c = [1, 2, 3, 4, False]
d = [1, 2, 3, 4, 0]

print(all(a))
print(all(b))
print(all(c))
print(all(d))