def percentage(M=420,getM=500):
    perc = ((M/getM) * 100)
    return perc

def main():
   
    
    print(percentage(250,500)) #Keyword argument
    print(percentage(250)) #Keyword argument
    print(percentage()) #Keyword argument
    
if __name__ == "__main__":
    main()
    