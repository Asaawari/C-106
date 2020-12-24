import numpy as np
import plotly.express as px
import csv

def getDataSource(dataPath):
    temperature = []
    iceCreamSales = []
    with open(dataPath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            temperature.append(float(row["Temperature"]))
            iceCreamSales.append(float(row["Ice-cream Sales( â‚¹ )"]))
    return {"x":temperature,"y":iceCreamSales}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Temperature vs Ice-cream Sales : \n--->", correlation[0,1])

def setup():
    dataPath = "Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

setup()