from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def MarvellousPredict():
    # Load data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

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
        numerator += (X[i]-mean_x*(Y[i]-mean_y))
        denomenator += (X[i] - mean_x)**2       

    m = numerator/denomenator
    
    print("Slope of line is: ",m)
    
    C = mean_y - m*mean_x
    
    print("Y intercept of line is : ",C)
    

def main():
    MarvellousPredict()


if __name__ == '__main__':
    main()
