from functools import reduce


data=[7,10,15,12,4,6,9,8,12,16]
print("Input data : ",data)


FData = list(filter(lambda no : (no%2 == 0),data))
print("Filter Data : ", FData)


MData = list(map(lambda No: No+1,FData))
print("Map Output : ",MData)


RData = reduce(lambda A,B : A+B,MData)
print("Reduce output : ",RData)