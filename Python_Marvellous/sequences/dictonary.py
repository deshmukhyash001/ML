# disctonary 
# Syntax = {key : value}
# Hetrogeneous
# ordered
# indexed (Non numeric)
# key duplicate allowed but old gets over written 
# value duplicate allowed 
# data mutable(value)


data = {"Name": "Let us C", "Author": "Y kanetkar", "Price": 340,"Publications": "BPB"}

print("Type of data : ", type(data))
print("Length is : ",len(data))

print(data)

data["Price"]= 500
print(data["Price"])

