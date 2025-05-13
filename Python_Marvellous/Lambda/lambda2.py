def eo(n):
    if n&1 == 0:
        return True
        
    else:
        return False
    
ret = eo(11)

if ret == True:
    print("Number is even")
else:
    print("NUmber is Odd")
    