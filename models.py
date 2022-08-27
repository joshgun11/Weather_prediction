from statistics import linear_regression
import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression


class Models():

    def __init__(self) -> None:
        pass

    def linear_regression(self,X_train,X_test,y_train,y_test):
        reg = LinearRegression()
        reg.fit(X_train, y_train)
        score = reg.score(X_test, y_test)
        print(score)



    


