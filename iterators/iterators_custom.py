'''
Custom iterator

Building an iterator from scratch is easy in Python. We just have to implement 
the __iter__() and the __next__() methods,

__iter__() returns the iterator object itself. If required, some initialization 
can be performed.

__next__() must return the next item in the sequence. On reaching the end, and 
in subsequent calls, it must raise StopIteration.
'''

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
        
# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print(next(i)) # prints 1
print(next(i)) # prints 2
print(next(i)) # prints 4
print(next(i)) # prints 8
print(next(i)) # raises StopIteration exception