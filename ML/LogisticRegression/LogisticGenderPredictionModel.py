import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def marvellouslogistic(datasetpath):
    df = pd.read_csv(datasetpath)
    print("Dimension of dataframe ",df.shape)
    print("Initial data is : ")
    print(df.head())

    df['Gender'] = df['Gender'].map({'Female':0,'Male':1})
    print(df.head())
    
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=df,x = 'Height',y='Weight',hue='Gender',palette="set")
    plt.title("Marvellous Weight Height Predictor")
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.grid(True)
    plt.show()
        
def main():
    marvellouslogistic('weight-height.csv')


if __name__ == '__main__':
    main()
