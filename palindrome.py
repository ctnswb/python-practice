# Write a method that takes a string and returns true if it is a
# palindrome. A palindrome is a string that is the same whether written
# backward or forward. Assume that there are no spaces; only lowercase
# letters will be given.
#
# Difficulty: easy.

def palindrome(string):
    p = True
    for i in range(len(string)/2):
        if string[i] == string[len(string)-1-i]:
            p = True
        else:
            return False
    return p


print "Test for palindrome"
print "palindrome('abc')==false:" + str(palindrome("abc"))
print "palindrome('abcba')==true:" + str(palindrome("abcba"))
print "palindrome('a')==true:" + str(palindrome("a"))
print "palindrome('abcd')==false:" + str(palindrome("abcd"))
print "palindrome('abba')==true:" + str(palindrome("abba"))
