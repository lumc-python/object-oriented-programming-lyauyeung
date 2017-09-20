from fraction import Fraction

if __name__ == '__main__':
    f1 = Fraction(1, 2)
    f2 = Fraction(10, 2)
    f3 = Fraction(3, 6)
    print f1
    print f1 + f2
    print f1.invert()
    print f2.to_float()
    print f2.integer()
    print f1 * f2
    print f2 / f1
    print f3.simplify()
    print f1 * 4