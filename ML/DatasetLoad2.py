from sklearn.datasets import load_iris

def main():
    dataset = load_iris()
    
    print("Independant (Features) variable names are : ")
   
    for i in range(len(dataset.target)):
        print("ID %d, Features %s, Label : %s"%(i,dataset.data[i],dataset.target[i]))
        
if __name__ == '__main__':
    main()
