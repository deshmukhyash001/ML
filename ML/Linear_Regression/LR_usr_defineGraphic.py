import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression 

def MarvellousPredict():
    # Load data
    
    data = pd.read_csv("demo.csv")
    X = data["x"]
    Y = data["y"]

    print(f"Values of independant variables {X}")
    print(f"Values of Dependant variable {Y}")
    
    mean_x = np.mean(X)
    mean_y = np.mean(Y)
    
    print(f"X_mean is : {mean_x}")
    print(f"Y_mean is : {mean_y}")
    
    n = len(X)

    numerator = 0
    denomenator = 0
    
    # Y = mX + C
    for i in range(n):

        # numerator += (X[i]-mean_x*(Y[i]-mean_y))
        numerator += (X[i]-mean_x)*(Y[i]-mean_y)
        denomenator += (X[i] - mean_x)**2       

    m = numerator/denomenator
    
    print("Slope of line is: ",m)
    
    C = mean_y - m*mean_x
    
    print("Y intercept of line is : ",C)
    
    x = np.linspace(1,6,n)    
    y = C+m*x
    
    print("\n\n\n",C+m*600)
    
    plt.plot(x,y,color = "g", label = "Independant variabe")
    plt.scatter(X,Y,color = 'r',label = "Scatter Plot")

    plt.xlabel("X : Independant Variable")
    plt.ylabel("Y : Dependant Variable")
    
    plt.show()
    
def main():
    MarvellousPredict()


if __name__ == '__main__':
    main()