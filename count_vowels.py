# Write a method that takes a string and returns the number of vowels
# in the string. You may assume that all the letters are lower cased.
# You can treat "y" as a consonant.
#
# Difficulty: easy.

def count_vowels(string):
    count = 0
    for i in range(len(string)):
        if (string[i] == "a")| (string[i] == "e")| (string[i] == "i")| (string[i] == "o")| (string[i] == "u"):
            count += 1
    return count

print "Test for count_vowels"
print "count_vowel('abcd') == 1:" + str(count_vowels("abcd"))
print "count_vowel('color') == 2:" + str(count_vowels("color"))
print "count_vowel('colour') == 3:" + str(count_vowels("colour"))
print "count_vowel('cecilia') == 4:" + str(count_vowels("cecilia"))
print "count_vowel('xyz') == 0:" + str(count_vowels("xyz"))
