def main():
    print("Enter your age")
    age  = int(input())
    
    if age < 18:
        print("You cant vote ")
    else:
        print("you can vote")
        
if __name__ == "__main__":
    main()