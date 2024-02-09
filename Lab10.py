import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import DataFrame, Series

# get data from CSV

rawDataset = pd.read_csv("movies.csv", header = None, names = ['Year','Title','Comic','IMDB','RT','','OpeningWeekendBoxOffice','AvgTicketPriceThatYear','EstdOpeningAttendance','USPopThatYear'])

# checks for valid data

dataset = rawDataset[np.isfinite(rawDataset["OpeningWeekendBoxOffice"])]

# normalization of data points
    
normalizedIMDB = dataset["IMDB"] / 10
normalizedRT = dataset["RT"] / 10

# insert into CSV

dataset.insert(10, "IMDBNormalized", normalizedIMDB)
dataset.insert(11, "RTNormalized", normalizedRT)

# creates scatter plot

dataset.plot.scatter(x = "RTNormalized", y = "IMDBNormalized")

# shows data plot

plt.show()

# statistical data

print(dataset[["RTNormalized", "IMDBNormalized"]].corr())
print(dataset[["RTNormalized", "IMDBNormalized"]].describe())

# ACTUAL HOMEWORK ASSIGNMENT

# Q1

dcMovies = dataset[dataset["Comic"] == "DC"]

# Q2

dcMoviesYearTitle = dataset[dataset["Comic"] == "DC"][["Year", "Title"]]

# Q3

marvelMoviesYearTitle = dataset[dataset["Comic"] == "Marvel"][["Year", "Title"]]

# Q4

dataset.plot.scatter(x = "Year", y = "AvgTicketPriceThatYear")
plt.show()

# Q5

correlation = dataset['Year'].corr(dataset['AvgTicketPriceThatYear'])

# Q6

summaryStats = dataset['OpeningWeekendBoxOffice'].describe()
