import numpy
import math

def EucDistance(P1,P2):
    Ans = math.sqrt((P1["x"]-P2["x"])**2+(P1["y"]-P2["y"])**2)
    return Ans

def MarvellousKNN():
    line = "-"*40
    data = [{
        "point":"A",
        "x":1,
        "y":2,
        "label":"Red"
    },
    {
        "point":"B",
        "x":2,
        "y":3,
        "label":"Red"
    },
    {
        "point":"C",
        "x":3,
        "y":1,
        "label":"Blue"
    },
    {
        "point":"D",
        "x":6,
        "y":5,
        "label":"Blue"
    }]
    
    print(line)
    print("training data : ")
    print(line)
    
    for i in data:
        print(i)
    
    print(line)
    
    print(f"training dataset")
    
    new_point = {'x':3,"y":3}
    
    for d in data:
        d["distance"] = EucDistance(d,new_point)
        
    print(line)
    print("Calculated Distances are : ")

    print(line)
    
    for d in data:
        print(d)
        
    print(line)
    
    
    # Sort by distance
    sorted_data = sorted(data,key= lambda item:item['distance'])
    
    for d in sorted_data:
        print(d)
        
    print(line)
    
    K = 3
    nearest = sorted_data[:K]
    
    print(line)
    print("Soeted 3 elements are : ")
    
    for d in nearest:
        print(d)
        
    print(line)
    
    votes = {}
    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label,0)+1
        
    print(line)
    print("result of voting is : ")
    for d in votes:
        print("Name : ",d," Value : ",votes[d])
    
    print(line)
    
    predicted_class = max(votes,key=votes.get)
    print(f"predicted class for point {new_point} is : {predicted_class}")
    
def main():
    
    print("Demonstraton of KNN algorithem")
    MarvellousKNN()
if __name__ == '__main__':
    main()
