"""
1. int object in python is not limited by the mannitude unlike other languages (where standard integers are fixed size s.a. 16 bit, 32 bit and 64 bit) and the only constraint in python is the amount of memory and time required to manipulate larger numbers.

2. Python float is a 64 bit float number internally using binary representation officially known as binary64 or IEEE-75 standard; these are commonly called double in C-derived languages. 
Of the 64 bits within a Python float:
     1 bit is for the sign of the number;
     11 for exponent (the value to which the fraction is raised)
     52 for the fraction (also known as the mantissa or significant)

Owing to the way encoding works in conjunction with the sign, float effectively has 53 bits of binary precision. In decimal equivalent, float has 15 to 17 bits of decimal precision. In other words, any decimal numbers with 15 significant figures can be converted to python float without loss of information. 
To query the range of float, use sys.float__info attribute
"""

n1 = 1.12345678910111
print(n1)
n2 = 1.1234567891011121 # 17 sig figures cause loss of information
print(n2)
n3 = 1.1234567891011122 # 17 sig figures but happen to be fine without rounding error. 
print(n3)

import sys
max_float, min_float = sys.float_info.max, sys.float_info.min
print(max_float, min_float)


# float limitation due to internally it can hold at most 53 bits for the fraction 
n4 = float(2**53) # this is fine without any loss
print(n4 == 2**53)
print([n4 + i == 2**53 + i for i in range(1, 5)])

# since float has finite precision, fractions cannot be represented accurately as finite precision decimal; just like 1/3 cannot be represented as finite decimal.
print(0.8 - 0.7)


"""
Just like C#, to counter some of limitations of float in python, Decimal type is introduced in the std library (Decimal class within the decimal module) and it's a fast correctly rounded type for performing arithmetic in base 10. Crucially, the decimal type is still a float point with a base 10 rather than 2. It of course has finite precision, although user configurable rather than fixed and defaults to 28 digits of decimal precision.  
"""
import decimal
print(decimal.getcontext())
from decimal import Decimal
print(Decimal(5))
print(Decimal('5'))
print(Decimal(5) == Decimal('5'))

# for fractions it's very important to pass in as string
print(Decimal('0.8') - Decimal('0.7'))

""" Why is this wrong?
Because 0.8 and 0.7 are two float numbers with base 10 but they're internally represented as base 2 (converted by Python) but neither of them can be represented exactly using base 2 so some rounding errors occur. Then the rounded (wrong) values are used to convert to decimal before the final wrong result is calculated.
Hence it's important to pass in string fractions to avoid the inexact intermeidate base 2 conversion
"""
print(Decimal(0.8) - Decimal(0.7)) # WRONG!

# to avoid inadvertently consturcting decimal objects from floats 
decimal.getcontext().traps[decimal.FloatOperation] = True
# now this doesn't work anymore
# Decimal(0.5) 
# Decimal(0.8) > 0.5

#decimal perservers the decimal precision and precision is propagated through computations.
print(Decimal(2))
print(Decimal('2.0'))
d1 = Decimal('2.00')
print(d1 * 3)

# decimal supports Infinity and -Infinity, NaN
print(Decimal('Infinity'))
print(Decimal('-Infinity'))
print(Decimal('NaN'))


# there are some legacy reason why Decimal behaves differently in some operations like modulus.
print(-7 % 3) # 2 because -7 - (-9) = 2
print(Decimal(-7) % Decimal(3)) # -1 because -7 - (-6) = -1 
def is_odd(n): # only works for integer 
    return n & 1 == 1

print(is_odd(-7))

def is_odd_float(f):
    return f % 2  != 0
print(is_odd_float(-7.0))
print(is_odd_float(Decimal('-7.0')))

# // division is consistent with modulus operation
print(-7 // 3) # -3
print(Decimal(-7) // Decimal(3)) # -2

# so float can only represent c*2**n e.g. 8.0 = 8 = 2**3and decimal can only represent c*10**n where c is an int factor. But some irrational numbers cannot be represented by either binary or decimal format e.g. 2/3

from fractions import Fraction
f1 = Fraction(2, 3)
print(f1)
f2 = Fraction(239548234) # fractions from integer with 1 being denominator
print(f2)
f3 = Fraction(0.5)
print(f3)
f4 = Fraction(0.1) 
print(f4) # since 0.1 cannot be exactly represented using binary format
