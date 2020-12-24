import numpy as np
import plotly.express as px
import csv

def getDataSource(dataPath):
    size = []
    hours = []
    with open(dataPath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            size.append(float(row["Size of TV"]))
            hours.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    return {"x":size,"y":hours}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Size of TV vs Average Time spent watching TV in a week : \n--->", correlation[0,1])

def setup():
    dataPath = "Size of TV,_Average time spent watching TV in a week (hours).csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

setup()