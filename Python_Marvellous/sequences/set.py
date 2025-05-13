# set
# Syntax : {}
# Unordered
# hetrogenious
# unindexed
# duplicate not allowed 
# set is mutable 
# data is immutable
data = {10,90.5,True,"Hello"}

print("Data type is : ",type(data))
print("Length is : ", len(data))

print(data)
data.add(71)
print(data)
data.remove(True)
print(data)

# print(data[2])
for i in data:
    print(i)