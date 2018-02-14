import pandas as pd
import numpy as np
from pandas import read_csv
from sklearn import preprocessing



def loadDataset():
    dataset = read_csv('semicon.csv',header=None)
    return dataset


def main():
    ds = loadDataset()
    print(ds.describe())
    print(ds.info())
    return


main()