import sys

def main():
    print("number od comand line args ", len(sys.argv))
    print("list of comand line argumments are : ")
    
    for i in sys.argv:
        print(i)
        
    for i in  range(1,len(sys.argv)):
        print(sys.argv[i])

    i = 1
    while i < len(sys.argv):
        print(sys.argv[i])
        i +=1

if __name__ == "__main__":
    main()