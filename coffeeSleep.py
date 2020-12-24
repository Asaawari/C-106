import plotly.express as px
import csv

with open('cups of coffee vs hours of sleep.csv') as csvFile:
    df = csv.DictReader(csvFile)
    fig = px.scatter(df,x='Coffee in ml',y='sleep in hours', color='week')
    fig.show()