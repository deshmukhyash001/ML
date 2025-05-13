
# Syntax :()
# hetrogenious
# ordered 
# indexed
# data immutable
# tuple immutable
# duplicate allowed

data = (40,90.67,"Hello",40,True)

print("data type is ", type(data))
print("Length is :", len(data))

print(data[0])
print(data[1])

print(data)

# data[0] = 11

print("Data display using loop")

for i in data:
    print(i)
    
    
print("Data display using loop")
print("loop using indexing")


for i in range(len(data)):
    print(data[i])