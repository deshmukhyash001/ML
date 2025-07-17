from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier

def calculateAccuracyDecisionTree():
    iris = load_iris()
    data = iris.data
    target = iris.target
    
    X_train,X_test,Y_train,Y_test = train_test_split(data,target,test_size=0.5,random_state=12)
    
    model = DecisionTreeClassifier()
    
    model.fit(X_train,Y_train)
    
    pred = model.predict(X_test)
    
    accuracy = accuracy_score(pred,Y_test)  
    
    return accuracy  

def calculateAccuracyKNN():
    iris = load_iris()
    data = iris.data
    target = iris.target
    
    X_train,X_test,Y_train,Y_test = train_test_split(data,target,test_size=0.5,random_state=12)
    
    model = KNeighborsClassifier()
    
    model.fit(X_train,Y_train)
    
    pred = model.predict(X_test)
    
    accuracy = accuracy_score(pred,Y_test)  
    
    return accuracy  

def main():
    DT = calculateAccuracyDecisionTree()
    KNN = calculateAccuracyKNN()
    print(f"Accuracy of decision tree classifier {DT*100}% ")
    print(f"Accuracy of K nearest neighbors classifier {KNN*100}% ")



if __name__ == '__main__':
    main()
