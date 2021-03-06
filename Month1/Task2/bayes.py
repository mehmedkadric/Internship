from pandas import read_csv
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import matplotlib
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


def ucitajDS():
    dataset = read_csv('noviDataset.csv')
    dataset.columns = ['Title', 'PClass', 'LifeStage', 'Survived']
    return dataset

def train(dataset):
    number = LabelEncoder()
    dataset["Title"] = number.fit_transform(dataset["Title"].astype('str'))
    dataset["PClass"] = number.fit_transform(dataset["PClass"].astype('str'))
    train, test = train_test_split(dataset, test_size=0.3)
    X_train = list(zip(train["Title"], train["PClass"], train["LifeStage"]))
    y_train = list((train["Survived"]))
    X_test = list(zip(test["Title"], test["PClass"], test["LifeStage"]))
    y_test = list((test["Survived"]))
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    y_pred = gnb.predict(X_test)
    print(classification_report(y_test, y_pred))
    model_accuracy = round(accuracy_score(y_test, y_pred) * 100, 2)
    print('Accuracy', model_accuracy, '%')
    return gnb


def prepareNewDataset():
    number = LabelEncoder()
    datasetTest = read_csv('noviDatasetTest.csv', header=None)
    datasetTest.columns = ['Title', 'PClass', 'LifeStage', 'Survived']
    datasetTest["Title"] = number.fit_transform(datasetTest["Title"].astype('str'))
    datasetTest["PClass"] = number.fit_transform(datasetTest["PClass"].astype('str'))
    return datasetTest


def main():
    dataset = ucitajDS()
    gnb = train(dataset)
    datasetTest = prepareNewDataset()
    X = list(zip(datasetTest["Title"], datasetTest["PClass"], datasetTest["LifeStage"]))
    Y = list((datasetTest["Survived"]))
    #print(classification_report(Y, y_pred))
    y_pred = gnb.predict(X)
    print(y_pred, Y)
    print(gnb.predict_proba(X))
    print(gnb.score(X,Y))
    return


main()
