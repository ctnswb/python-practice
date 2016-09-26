# Write a method that takes in a number and returns a string, placing
# a single dash before and after each odd digit. There is one
# exception: don't start or end the string with a dash.
#
# You may wish to use the `%` modulo operation; you can see if a number
# is even if it has zero remainder when divided by two.
#
# Difficulty: medium.

def dasherize_number(num):
    number = str(num)
    dasherize = number[0]
    for i in range (0, len(number)-1):
        if int(number[i])%2 == 1:
            dasherize += "-"
        elif int(number[i+1])%2 == 1:
            dasherize += "-"
        dasherize += number[i+1]
    return dasherize 
        

# These are tests to check that your code is working. After writing
# your solution, they should all print true.

print "\nTests for #dasherize_number"
print 'dasherize_number(203) == "20-3": '+dasherize_number(203) + str(dasherize_number(203) == '20-3')
print 'dasherize_number(303) == "3-0-3": '+dasherize_number(303) + str(dasherize_number(303) == '3-0-3')
print 'dasherize_number(333) == "3-3-3": ' +dasherize_number(333)+ str(dasherize_number(333) == '3-3-3')
print 'dasherize_number(3223) == "3-22-3": ' + dasherize_number(3223)+str(dasherize_number(3223) == '3-22-3')
print 'dasherize_number(32234) == "3-22-3-4": ' + dasherize_number(32234)+str(dasherize_number(32234) == '3-22-3-4')
print 'dasherize_number(32234) == "3-22-3-46": ' + dasherize_number(322346)+str(dasherize_number(322346) == '3-22-3-46')
