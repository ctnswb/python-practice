# Write a method that takes in a string. Your method should return the
# most common letter in the array, and a count of how many times it
# appears.
#
# Difficulty: medium.

def most_common_letter(string):
    count = []
    new = True
    most_common = []
    times = 0
    for i in range (0,len(string)):
        for j in range (0,len(count)):
            if count[j][0] == string[i]:
                count[j][1]+= 1
                new= False
                if count[j][1] > times:
                    most_common = count[j]
        if new:
            count.append([string[i],1])
    return most_common
            
            

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print "\nTests for #most_common_letter"
print 'most_common_letter("abca") == ["a", 2]: ' + str(most_common_letter('abca') == ['a', 2])
print 'most_common_letter("abbab") == ["b", 3]: ' + str(most_common_letter('abbab') == ['b', 3])
print 'most_common_letter("abebeabee") == ["e", 4]: ' + str(most_common_letter('abebeabee') == ['e', 4])
