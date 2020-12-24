import plotly.express as px
import csv

with open('Size of TV,_Average time spent watching TV in a week (hours).csv') as csvFile:
    df = csv.DictReader(csvFile)
    fig = px.scatter(df,x='Size of TV',y='\tAverage time spent watching TV in a week (hours)')
    fig.show()