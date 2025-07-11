from sklearn.datasets import load_iris

def main():
    dataset = load_iris()
    
    print("Independant (Features) variable names are : ")
    print(dataset.feature_names)

    print("dependant (Labels) variable names are : ")
    print(dataset.target_names)
if __name__ == '__main__':
    main()
