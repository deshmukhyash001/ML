import arithematic 

def main():
    print("enter first number: ")
    no1 = int(input())

    print("Enter second number : ")
    no2 = int(input())
    
    ans  =  arithematic.prod(no1,no2)
    print(ans)
    
if __name__ == "__main__":
    main()