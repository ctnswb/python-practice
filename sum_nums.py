# Write a method that takes in an integer `num` and returns the sum of
# all integers between zero and num, up to and including `num`.
#
# Difficulty: easy.

def sum_nums(num):
    result = 0
    current = num
    while current > 0:
        result += current
        current -= 1
    return result

print "Tests for sum_nums"
print "sum_nums(1) == 1:" + str(sum_nums(1))
print "sum_nums(2) == 3:" + str(sum_nums(2))
print "sum_nums(3) == 6:" + str(sum_nums(3))
print "sum_nums(4) == 10:" + str(sum_nums(4))
print "sum_nums(5) == 15:" + str(sum_nums(5))
