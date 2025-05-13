import sys

def main():
    print("number od comand line args ", len(sys.argv))
    print("first cmf line arg is", sys.argv[0])
    print("DT of sys.argv is ", type(sys.argv))
    print("first cmf line arg1 is", sys.argv[1])
    print("first cmf line arg2 is", sys.argv[2])
    print("first cmf line arg3 is", sys.argv[3])


if __name__ == "__main__":
    main()