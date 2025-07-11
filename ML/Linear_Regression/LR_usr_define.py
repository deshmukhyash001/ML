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
    
    mean_x = 0
    mean_y = 0
    
    XSum = 0
    YSum = 0
    
    for i in range(len(X)):
        XSum += X[i]
        YSum += Y[i]
        
    mean_x = XSum/len(X)     
    mean_y = YSum/len(Y)
    
    print(f"X_mean is : {mean_x}")
    print(f"Y_mean is : {mean_y}")
    
def main():
    MarvellousPredict()


if __name__ == '__main__':
    main()
