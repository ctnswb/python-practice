# Write a method that takes a string in and returns true if the letter
# "z" appears within three letters **after** an "a". You may assume
# that the string contains only lowercase letters.
#
# Difficulty: medium.

def nearby_az(string):
    current = string[0]
    nearby = False
    for i in range (0, len(string)): # while theres still letters to check
        current = string[i]
        if current == "a": # check if current letter is "a"
            for j in range (i+1,i+4):
                if j < len(string): # if its an a, check if z is within next 3 letters
                    if string[j] == "z":
                        nearby = True
    return nearby

print "Tests for nearby_az"

print "nearby_az('baz')==true:" + str(nearby_az("baz"))
print "nearby_az('abz')==true:" + str(nearby_az("abz"))
print "nearby_az('abcz')==true:" + str(nearby_az("abcz"))
print "nearby_az('a')==false:" + str(nearby_az("a"))
print "nearby_az('z')==false:" + str(nearby_az("z"))
print "nearby_az('za')==false:" + str(nearby_az("za"))
print "nearby_az('oeueeeaeui')==false:" + str(nearby_az("oeueeeaeui"))
print "nearby_az('eoeaoez')==true:" + str(nearby_az("eoeaoez"))
print "nearby_az('eaeaoee')==false:" + str(nearby_az("eaeaoee"))
