PI = 3.14
def Area(radi):
    Area = PI * radi * radi
    return Area

def main():
    print("enter radious of circle")
    radi=float(input())
        
    print("Area of circle is ", Area(radi))
    
if(__name__ == "__main__"):
    main()