class Vector(object):
    def __init__(self, *args):
        """ Create a vector, example: v = Vector(1,2) """
        if len(args) == 0:
            self.values = (0, 0)
        else:
            self.values = args

    def __add__(self, other):
        """ Returns the vector addition of self and other """
        added = tuple(a + b for a, b in zip(self.values, other.values))
        return Vector(*added)


v1 = Vector(1, 2)
v2 = Vector(10, 13)
v3 = v1 + v2
v3.values
#(11, 15)
