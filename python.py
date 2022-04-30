"""
Name:       Richard Ngo
Email:      richard.ngo94@myhunter.cuny.edu
Resources:  https://www1.nyc.gov/assets/doh/downloads/pdf/epi/databrief127.pdf , https://www.who.int/news-room/fact-sheets/detail/suicide, https://www.cdc.gov/nchs/data/databriefs/db398-tables-508.pdf#page=2
Devin Li helped me with Map part
https://data.cityofnewyork.us/City-Government/Borough-Boundaries/tqmj-j8zm
Title:      Suicide In the United States
URL:        https://rn0529.github.io/DatascienceWebsite/
"""

#the numbers for 2019 by age and over 19 years are per 100k people
import plotly.express as px
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

#display total suicide rate
def DisplayTotal():
    df = pd.read_csv("suicideRatesOver19yearscleaned - suicideRatesOver19years.csv")
    dfBoth = df.loc[df['Sex']=="Both sexes"]
    plt.plot(dfBoth['Period'], dfBoth['FactValueNumeric'],)
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Number of suicides per 100k')
    plt.show()
    return

def DisplayBothSex():
    #display both sex suicide rate
    df = pd.read_csv("suicideRatesOver19yearscleaned - suicideRatesOver19years.csv")
    df2 = df.loc[df['Sex']=="Male"]
    df3 = df.loc[df['Sex']=="Female"]
    print(df)
    plt.plot(df2['Period'], df2['FactValueNumeric'],label = "Male")
    plt.plot(df3['Period'], df3['FactValueNumeric'],label = "Female")
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Number of suicides per 100k')
    plt.show()
    
    return

def DisplayByAge():
    df2 = pd.read_csv("2019suicidebyage - 2019suicidebyage.csv")
    df2 = df2.loc[df2['Dim1']=="Both sexes"]
    print(df2)
    xAxis = df2['Dim2']
    yAxis = df2['FactValueNumeric']
    plt.bar(xAxis,yAxis)
    plt.title('Suicide Rates By Age In 2019')
    plt.xlabel('Age Groups')
    plt.ylabel('Number of deaths per 100k')
    plt.show()
    return

def DisplayLinerReg():
    #display linear regression
    df = pd.read_csv("suicideRatesOver19yearscleaned - suicideRatesOver19years.csv")
    print(df)
    df = df.loc[df['Sex']=="Both sexes"]
    print("after")
    print(df)
    x = np.array(df['Period']).reshape((-1, 1))
    y = df['FactValueNumeric']
    linearReg  = LinearRegression()
    linearReg.fit(x,y)
    print(linearReg.intercept_, linearReg.coef_, linearReg)
    ypred = linearReg.predict(x)
    plt.scatter(x, y, color="black")
    plt.plot(x, ypred, color="blue", linewidth=3)
    plt.xlabel('Year')
    plt.ylabel('Number of suicides per 100k')
    plt.xticks(())
    plt.yticks(())
    plt.show()
    return


#Display map

def DisplayMap():
    boroughLocations = json.load(open('Borough_Boundaries.geojson'))
    df =pd.read_csv("boroughsuicide.csv")
    sums = df['Sum'].sum()
    df['Sum'] = df['Sum']/sums
    suicidePlot = px.choropleth_mapbox(
        df, 
        geojson=boroughLocations, 
        locations= 'Borough', 
        featureidkey="properties.boro_name", 
        color= 'Sum',
        color_continuous_scale='Oranges',
        range_color=(0, .30),
        mapbox_style="carto-positron",
        zoom=9.7, center = {"lat": 40.7128, "lon": -74.0060},
        title="Suicide by Borough"
    )
    suicidePlot.show()
    return


DisplayTotal()
DisplayBothSex()
DisplayByAge()
DisplayLinerReg()
DisplayMap()