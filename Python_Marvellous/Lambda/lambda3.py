def eo(n):
    return (n&1 == 0)
    
ret = eo(11)

if ret == True:
    print("Number is even")
else:
    print("NUmber is Odd")
    