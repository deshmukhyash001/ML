from functools import reduce

CheckEven= lambda no : (no%2 == 0)

Increase = lambda No: No+1

Sum = lambda A,B : A+B

data=[7,10,15,12,4,6,9,8,12,16]
print("Input data : ",data)


FData = list(filter(CheckEven,data))
print("Filter Data : ", FData)


MData = list(map(Increase,FData))
print("Map Output : ",MData)


RData = reduce(Sum,MData)
print("Reduce output : ",RData)