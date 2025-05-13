import sys 
from add import add

def main():
    
    if len(sys.argv)>1:
        n1 = int(sys.argv[1])
        n2 = int(sys.argv[2])
        res = add(n1,n2)
        print("Addition is : ",res)
    else:
        print("Insufficient no. argument")
        

        
    
        
        
if __name__ == "__main__":
    main()