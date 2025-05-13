def percentage(getM,M):
    perc = ((M/getM) * 100)
    return perc

def main():
    print("Enter a Total marks")
    no1 =int(input())
    
    print("Enter marks get ")
    no2=int(input())
    
    print(percentage(getM=no1,M=no2)) #Keyword argument
        
if __name__ == "__main__":
    main()
    