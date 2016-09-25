# Write a method that will take in a number of minutes, and returns a
# string that formats the number into `hours:minutes`.
#
# Difficulty: easy.

def time_conversion(minutes):
    h = minutes/60
    m = minutes%60
    ms = str(m)
    if m < 10:
        ms = "0"+str(m)
    return str(h)+ ":" + ms

print "Tests for time_conversion"
print "time_conversion(15) == '0:15':" + time_conversion(15)
print "time_conversion(150) == '2:30':" + time_conversion(150)
print "time_conversion(360) == '6:00':" + time_conversion(360)
