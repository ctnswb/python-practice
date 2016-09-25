# Write a method that takes in a number and returns true if it is a
# power of 2. Otherwise, return false.
#
# You may want to use the `%` modulo operation. `5 % 2` returns the
# remainder when dividing 5 by 2; therefore, `5 % 2 == 1`. In the case
# of `6 % 2`, since 2 evenly divides 6 with no remainder, `6 % 2 == 0`.
#
# Difficulty: medium.

def is_power_of_two(num):
    current = num
    is_power = False
    while current > 0:
        if current == 1:
            return True
        elif current%2==1:
            return False
        current /= 2
    return is_power
            

print "\nTests for #is_power_of_two?"
print 'is_power_of_two?(1) == true: ' + str(is_power_of_two(1))
print 'is_power_of_two?(16) == true: ' + str(is_power_of_two(16))
print 'is_power_of_two?(64) == true: ' + str(is_power_of_two(64))
print 'is_power_of_two?(78) == false: ' + str(is_power_of_two(78))
print'is_power_of_two?(0) == false: ' + str(is_power_of_two(0))
