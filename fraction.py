class Fraction(object):
    """
    A simple fraction class.
    """

    def __init__(self, numerator=1, denominator=1):
        """
        Creates a new fraction.
        """
        self._numerator = numerator
        self._denominator = denominator
    
    def __str__(self):
        """
        1. Prints the fraction as numerator/denominator.
        """
        return str(self._numerator)+'/'+str(self._denominator)
    
    def __add__(self, other):
        """
        2. Adds up two fractions.
        """
        numerator = (self._numerator * other._denominator +
                     self._denominator * other._numerator)
        denominator = self._denominator * other._denominator
        return Fraction(numerator, denominator)
    
    def invert(self):
        """
        3. Inverts the fraction.
        """
        return Fraction(self._denominator,self._numerator)
    
    def to_float(self):
        """
        4. Decimal representation of the fraction.
        """
        numerator = float(self._numerator)
        return numerator/self._denominator
    
    def integer(self):
        """
        5. Returns the integer part of the fraction.
        """
        return self._numerator/self._denominator
    
    def __sub__(self, other):
        """
        6.1 Subtracts one fractions from the other.
        """
        numerator = (self._numerator * other._denominator -
                     self._denominator * other._numerator)
        denominator = self._demoninator * other._denominator
        return Fraction(numerator, denominator)
    
    def __mul__(self, other):
        """
        6.2 & 11 Multiplies two fractions or an integer and fraction.
        """
        if isinstance(other,int):
            numerator = other * self._numerator
            return Fraction(numerator,self._denominator)
        else:
            return Fraction((self._numerator * other._numerator), 
                             self._denominator * other._denominator)

    def __div__(self, other):
        """
        6.3 Divides the fraction from other fraction.
        """
        inverted = other.invert()
        return Fraction(self._numerator * inverted._numerator, 
                        self._denominator * inverted._denominator)
    
    def gcd(self):
        """
        Get greatest common divisor. Used for simplify().
        """
        a = self._numerator
        b = self._denominator
        while b:
            a, b = b, a % b
        return a
    
    def simplify(self):
        """
        7. Simplifies a fraction.
        """
        common_divisor = self.gcd()
        return Fraction(self._numerator/common_divisor, 
                        self._denominator/common_divisor)
    
    def __eq__(self, other):
        """
        9. Returns true when fractions are equal.
        """
        if self.to_float() == other.to_float():
            return True
        else:
            return False

"""
10. Use another self._numeratorNeg or something if the numerator is < 0. This
way it can be multiplied by -1 and then used in following functions. Did not 
have time to implement it. But this is what I would do. 

11. There are built in functions like __radd__ and __rmul___, but I am not sure
how to make functions commutative.

12. Write an if-statement in the __init__ function?
""" 
    
    
