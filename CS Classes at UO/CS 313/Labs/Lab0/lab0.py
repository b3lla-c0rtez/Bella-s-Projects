import math

class mathOps:
    """
    Simple math operations on a given pair of integers, u and v.
    This includes the lcm (least common multiple) and
    gcd (greatest common divisor) functions, each of returns an integer.
    """

    def __init__(self, u, v):
        '''Set the values of u and v to be used in the math operations.'''
        self.u = u
        self.v = v

    def __repr__(self):
        return "mathOps({}, {})".format(self.u, self.v)

    def valid(self):
        '''True if both u and v are integers.'''
        return isinstance(self.u, int) and isinstance(self.v, int)

    def gcd(self):
        '''Compute the greatest common divisor of member variables u and v.'''
        # Find the greatest common divisor of a and b
        # Hint: Use Euclid's Algorithm
        # https://en.wikipedia.org/wiki/Euclidean_algorithm#Procedure
        tempU = abs(math.ceil(self.u))
        tempV = abs(math.ceil(self.v))


        try:
            if tempU == (float("inf") or float("-inf")) or tempV == (float("inf") or float("-inf")):
                raise OverflowError
        # ENTER YOUR CODE HERE
        # Feel free to modify the exceptions, delete the try block etc or the entire funtion
        # Just keep the fucntion name as gcd

        except OverflowError:
            print("one or both the values of", tempU, " and ", tempV, "are equal to infinity")
            raise OverflowError

        try:
            if tempU == (int("0") and tempV == int("0")):
                raise OverflowError

        except OverflowError:
            print("one or both the values of ", tempU, " and ", tempV, "are equal to 0")
            raise OverflowError

        if tempV == 0:
            return tempU
        else:
            return mathOps(tempV, math.ceil(tempU % tempV)).gcd()



    def lcm(self):
        '''Compute the least common multiple of member variables u and v.'''
        # Hint: Use the gcd of a and b
        tempU = abs(math.ceil(self.u))
        tempV = abs(math.ceil(self.v))

        try:
            if tempU == (float("inf") or float("-inf")) or tempV == (float("inf") or float("-inf")):
                raise OverflowError

        # ENTER YOUR CODE HERE
        # Feel free to modify the exceptions, delete the try block etc or the entire funtion
        # Just keep the fucntion name as lcm

        except OverflowError:
            print("one or both the values of ", tempU, " and ", tempV, " are equal to infinity")
            raise OverflowError

        try:
            if tempU == (int("0") and tempV == int("0")):
                raise OverflowError

        except OverflowError:
            print("one or both the values of ", tempU, " and ", tempV, " are equal to 0")
            raise OverflowError


        num = tempU * tempV
        den = mathOps(tempU,tempV).gcd()
        sol = num/den
        return sol