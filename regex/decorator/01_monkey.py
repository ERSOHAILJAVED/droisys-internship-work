from fractions import Fraction

# Monkey patching line :)
Fraction.inverse = lambda self: self.denominator/self.numerator

frac1 = Fraction(5,10)
print(frac1.inverse())

frac2 = Fraction(10,5)
print(frac2.inverse())