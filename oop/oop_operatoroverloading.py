'''
Operator Overloading

- Operator overloading is a feature in Python that allows you to define
    operators for classes that do not support them.

List of operator

Operator	        Expression	    Internally
Addition	        p1 + p2	        p1.__add__(p2)
Subtraction	        p1 - p2	        p1.__sub__(p2)
Multiplication	    p1 * p2	        p1.__mul__(p2)
Power	            p1 ** p2	    p1.__pow__(p2)
Division	        p1 / p2	        p1.__truediv__(p2)
Floor Division	    p1 // p2	    p1.__floordiv__(p2)
Remainder (modulo)	p1 % p2	        p1.__mod__(p2)
Bitwise Left Shift	p1 << p2	    p1.__lshift__(p2)
Bitwise Right Shift	p1 >> p2	    p1.__rshift__(p2)
Bitwise AND	        p1 & p2	        p1.__and__(p2)
Bitwise OR	        p1 | p2	        p1.__or__(p2)
Bitwise XOR	        p1 ^ p2	        p1.__xor__(p2)
Bitwise NOT	        ~p1	            p1.__invert__()
'''

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    # Operator overloading for +
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1 = Point(1, 2)
p2 = Point(2, 3)
p3 = p1 + p2
print(p3)