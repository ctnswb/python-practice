# Write a method that takes an array of numbers. If a pair of numbers
# in the array sums to zero, return the positions of those two numbers.
# If no pair of numbers sums to zero, return `nil`.
#
# Difficulty: medium.

def two_sum(nums):
    for i in range (0, len(nums)):
        for j in range (i+1, len(nums)):
            if nums[i] + nums[j] == 0:
                return [i, j]
    return None

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print "\nTests for #two_sum"
print 'two_sum([1, 3, 5, -3]) == [1, 3]: ' + str(two_sum([1, 3, 5, -3]))
print 'two_sum([1, 3, 5]) == nil: ' + str(two_sum([1, 3, 5]))
print 'two_sum([1, 3, 5, -5]) == nil: ' + str(two_sum([1, 3, 5, -5]))
print 'two_sum([1, 3, 5, -1, -3]) == nil: ' + str(two_sum([1, 3, 5, -1, -3]))


# I am assuming that there is only one such pair (if any) in the set
