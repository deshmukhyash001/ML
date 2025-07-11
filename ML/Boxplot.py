import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df = pd.read_csv("iris.csv")
    sns.boxenplot(x='variety',y='petal.length',data =df)    
    plt.title("Marvellous box plot for petal.length variety")
    plt.show()
    
if __name__ == '__main__':
    main()
