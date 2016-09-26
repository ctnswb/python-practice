# Write a method that takes in a string of lowercase letters and
# spaces, producing a new string that capitalizes the first letter of
# each word.
#
# You'll want to use the `split` and `join` methods. Also, the String
# method `upcase`, which converts a string to all upper case will be
# helpful.
#
# Difficulty: medium.

def capitalize_words(string):
    words = string.split()
    capitalized = ""
    for i in range (0, len(words)):
        current = words[i]
        capitalized += current[0].upper()
        for j in range (1, len(current)):
            capitalized += current[j]
        if i < (len(words)-1):
            capitalized += " "
        
    return capitalized

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print capitalize_words("this is a sentence")
print capitalize_words("mike bloomfield")

print 'capitalize_words("this is a sentence") == "This Is A Sentence": ' + str(capitalize_words("this is a sentence") == "This Is A Sentence")
print 'capitalize_words("mike bloomfield") == "Mike Bloomfield": ' + str(capitalize_words("mike bloomfield") == "Mike Bloomfield")
