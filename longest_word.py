# Write a method that takes in a string. Return the longest word in
# the string. You may assume that the string contains only letters and
# spaces.
#
# You may use the String `split` method to aid you in your quest.
#
# Difficulty: easy.

def longest_word(sentence):
    a = sentence.split()
    longest = ""
    for i in range(len(a)):
        if len(a[i]) > len(longest):
            longest = a[i]

    return longest

print "Test for longest word"
print "longest_word('short longest') == 'longest':" + str(longest_word('short longest'))
print "longest_word('one') == 'one':" + str(longest_word('one'))
print "longest_word('abc def abcde') == 'abcde':" + str(longest_word('abc def abcde'))
print "longest_word('') == '':" + str(longest_word(''))
