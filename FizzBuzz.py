for n in range(1,101):
    p = ""
    if n%3==0:
        p+="Fizz"
    if n%5==0:
        p+="Buzz"
    if p=="":
        print n
    else:
        print p
