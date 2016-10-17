# Write a method that takes in a string and an array of indices in the
# string. Produce a new string, which contains letters from the input
# string in the order specified by the indices of the array of indices.
#
# Difficulty: medium.

def scramble_string(string, positions):
      scrambled = ""
      for i in positions:
            scrambled += string[i]

      return scrambled

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print "\nTests for #scramble_string"
print 'scramble_string("abcd", [3, 1, 2, 0]) == "dbca": ' + str(scramble_string("abcd", [3, 1, 2, 0]))
print 'scramble_string("markov", [5, 3, 1, 4, 2, 0]) == "vkaorm"): ' + str(scramble_string("markov", [5, 3, 1, 4, 2, 0]))
