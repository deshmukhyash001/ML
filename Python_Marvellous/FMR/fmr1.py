from functools import reduce

def CheckEven(no):
    return(no%2 == 0)

def Increase(No):
    return No+1

def Sum(A,B):
    return A+B

data=[7,10,15,12,4,6,9,8,12,16]
print("Input data : ",data)


FData = list(filter(CheckEven,data))
print("Filter Data : ", FData)


MData = list(map(Increase,FData))
print("Map Output : ",MData)


RData = reduce(Sum,MData)
print("Reduce output : ",RData)