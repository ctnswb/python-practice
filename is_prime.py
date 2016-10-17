# Write a method that takes in an integer (greater than one) and
# returns true if it is prime; otherwise return false.
#
# You may want to use the `%` modulo operation. `5 % 2` returns the
# remainder when dividing 5 by 2; therefore, `5 % 2 == 1`. In the case
# of `6 % 2`, since 2 evenly divides 6 with no remainder, `6 % 2 == 0`.
# More generally, if `m` and `n` are integers, `m % n == 0` if and only
# if `n` divides `m` evenly.
#
# You would not be expected to already know about modulo for the
# challenge.
#
# Difficulty: medium.

def is_prime(number):
    if number < 4:
        return True
    if number%2 == 0:
        return False
    if number%3 == 0:
        return False
    for i in range (1,int(number**(0.5))):
        if number % (6*i+1) == 0:
            return False
        if number % (6*i-1) ==0:
            return False
    return True


# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print "\nTests for #is_prime?"
print 'is_prime(2) == true: ' + str(is_prime(2))
print'is_prime(3) == true: ' + str(is_prime(3))
print'is_prime(4) == false: ' + str(is_prime(4))
print 'is_prime(9) == false: ' + str(is_prime(9))
print 'is_prime(131) == true: ' + str(is_prime(131))
print 'is_prime(719) == true: ' + str(is_prime(719))
print 'is_prime(460) == false: ' + str(is_prime(460))


#A more efficient method is to test if n is divisible by 2 or 3,
#then to check through all the numbers of form 6k+or-1 <= sqrt{n}
