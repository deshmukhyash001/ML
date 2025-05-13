# Hetrogenious
# indexed
# ordered
# list 



data = [40,90.67,"Hello",40,50,True]

print("data type is ", type(data))
print("Length is :", len(data))

print(data[0])
print(data[1])
print(data[2])
print(data[3])

data[0] = 11

data.append(50)

print(data[6])
print(data)
print("Data display using loop")

for i in data:
    print(i)