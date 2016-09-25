# Write a method that takes an integer `n` in; it should return
# n*(n-1)*(n-2)*...*2*1. Assume n >= 0.
#
# As a special case, `factorial(0) == 1`.
#
# Difficulty: easy.

def factorial(n):
    if n < 0:
        return None
    i = 0
    x = n
    result = 1
    while x > 0:
        result *= x
        x -= 1
    return result

print "Tests for factorial"
print "factorial(0) == 1:" + str(factorial(0))
print "factorial(1) == 1:" + str(factorial(1))
print "factorial(2) == 2:" + str(factorial(2))
print "factorial(3) == 6:" + str(factorial(3))
print "factorial(4) == 24:" + str(factorial(4))
print "factorial(-2) == None:" + str(factorial(-2))
