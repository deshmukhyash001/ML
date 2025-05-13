def Area(rad,PI=3.14):
    Area = PI * rad * rad
    return Area

def main():
    print("enter radious of circle")
    radi=float(input())
        
    print("Area of circle is ", Area(rad=radi))
    
if(__name__ == "__main__"):
    main()