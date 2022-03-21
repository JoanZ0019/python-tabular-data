#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def species(n):
    x = n.petal_length_cm
    y = n.sepal_length_cm
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'Data')
    plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig("petal_v_sepal_length_regress.png")

"""
Generate the regression plot

Parameter
------
n: species
------
"""

dataframe = pd.read_csv("iris.csv")
#versicolor = dataframe[dataframe.species == 'Iris_versicolor']
#species(versicolor)

#setosa = dataframe[dataframe.species == 'Iris_setosa']
#species(setosa)
 
virginica = dataframe[dataframe.species == 'Iris_virginica']
species(virginica)

