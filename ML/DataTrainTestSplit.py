import pandas as pd
def main():
    df =pd.read_csv("iris.csv")
    print("Dataset Loaded")
    print("Dimensions",df.shape)

    print(df["variety"])
    # print(df["sepal.length"].head())
    
    df["variety"] = df['variety'].map({"Setosa":0,'Versicolor':1,"Virginica":2})
    print(df["variety"])
    
    X = df.drop('variety',axis='columns')
    Y = df['variety']
    
    print("Independant variable Dimensions",X.shape)
    print("dependant variable Dimensions",Y.shape)
    

if __name__ == '__main__':
    main()
