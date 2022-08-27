import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


class Prepare():
    def __init__(self) -> None:
        pass

    def load_data(self,data):
        df = pd.read_csv(data)
        return df

    def split_data(self,data,test_size):
        features = data[['Date', 'Precip', 'MaxTemp', 'MeanTemp', 'Snowfall', 'MAX', 'MIN', 'MEA', 'SNF']]
        target = data['MinTemp']
        one_hot = pd.get_dummies(features['Date'])

        features = features.drop('Date',axis = 1)
        features = features.join(one_hot)
        X_train,X_test,y_train,y_test = train_test_split(features,target,test_size = test_size,random_state = 43)

        return X_train,X_test,y_train,y_test

    def normalize_features(self,X_train,X_test):
        scaler = StandardScaler()
        X_train_transformed = scaler.fit_transform(X_train)
        X_test_transformed = scaler.transform(X_test)

        return X_train_transformed,X_test_transformed


