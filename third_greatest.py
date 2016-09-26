# Write a method that takes an array of numbers in. Your method should
# return the third greatest number in the array. You may assume that
# the array has at least three numbers in it.
#
# Difficulty: medium.

def third_greatest(nums):
    first = None
    second = None
    third = None
    for i in range (0, len(nums)):
        current = nums[i]
        if current > first:
            third = second
            second = first
            first = current
        elif current > second:
            third = second
            second = current
        elif current > third:
            third = current
    return third
            


# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print "Tests for #third_greatest"

print 'third_greatest([5, 3, 7]) == 3: ' + str(third_greatest([5, 3, 7]) == 3)
print 'third_greatest([5, 3, 7, 4]) == 4: ' + str(third_greatest([5, 3, 7, 4]) == 4)
print 'third_greatest([2, 3, 7, 4]) == 3: ' + str(third_greatest([2, 3, 7, 4]) == 3)
print 'third_greatest([1, 2, 3,5,6, 7, 4]) == 5: ' + str(third_greatest([1, 2, 3,5,6, 7, 4]) == 5)
