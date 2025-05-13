import sys 
from add import add

def main():
    
    if len(sys.argv) == 2:
        if sys.argv[1] == "--h":
            print("This is use to perform addition of two numbers")
            return

        if sys.argv[1] == "--u":
            print("Execute the code as ")
            print("Fileneme.py first_inp second_int")
            return
    
    if len(sys.argv)>2:
        
        n1 = int(sys.argv[1])
        n2 = int(sys.argv[2])
        res = add(n1,n2)
        print("Addition is : ",res)
    else:
        print("You ca")
        print("Insufficient no. argument")
        

        
if __name__ == "__main__":
    main()