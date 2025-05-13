def main():
    n = int(input("Enter number of elm: "))
    data = list()
    for i in range(n):
        itm = input()
        data.append(itm)
        
    print("Entered elements are :")
    for i in data:
        print(i)
    
    
    
if __name__ == "__main__":
    main()