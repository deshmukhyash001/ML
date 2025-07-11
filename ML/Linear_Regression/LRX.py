def y_predict(bias,slope,X):
    Y = bias - slope*X
    return Y

def main():

    Xy_train = {512:2000000,402:1700000,720:2500000}
    xi,yi,xi2,xiyi = 0,0,0,0
    n = len(Xy_train)

    for i in Xy_train:
        xi += i
        yi += Xy_train[i]
        xi2 += i**2
        xiyi += i*Xy_train[i]

    bias_numerator = (n * xiyi) - xi*yi
    bias_denominator = n * xi2 - xi**2  
    bias = bias_numerator/bias_denominator

    slope_numerator = yi - bias*xi
    slope = slope_numerator/n

    print(bias)
    print(slope)

    Xy_test = {500:1920000,750:2700000}
    mean = sum(Xy_test.values())/len(Xy_test)

    y_actual,error,variation = 0,0,0
    for X in Xy_test:
        X_pred = y_predict(bias,slope,X)
        print(X_pred)
        y_actual += Xy_test[X]
        error += (Xy_test[X]-X_pred)**2
        variation += (Xy_test[X] - mean)**2

    accuracy = (1-(error/variation))
    print(accuracy)

if __name__ == '__main__':
    main()