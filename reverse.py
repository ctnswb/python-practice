# Write a method that will take a string as input, and return a new
# string with the same letters in reverse order.
#
# Don't use String's reverse method; that would be too simple.
#
# Difficulty: easy.


def reverse(s):
    rString = ''
    for i in range(len(s)-1,-1,-1):
        rString += s[i]
    return rString


print "Tests for reverse"
print "reverse('abcdef') == " + reverse("abcdef")
print "reverse('a') == " + reverse("a")
print "reverse('') == " + reverse("")

