from  marvellous import filterX,mapX,reduceX
CheckEven= lambda no : (no%2 == 0)
Increase = lambda No: No+1
Sum = lambda A,B : A+B


def main():
    data=[]
    for i in range((int(input("Enter no. of element : ")))):
        no = int(input())
        data.append(no)
        
    
    print("Input data : ",data)


    FData = list(filterX(CheckEven,data))
    print("Filter Data : ", FData)


    MData = list(mapX(Increase,FData))
    print("Map Output : ",MData)


    RData = reduceX(Sum,MData)
    print("Reduce output : ",RData)
    
if __name__ == "__main__":
    main()