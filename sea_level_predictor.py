import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    plt.scatter(df['Year'], 
                df['CSIRO Adjusted Sea Level'],
                c='blue', 
                s=10)

    # Create first line of best fit
    fit1880 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    xVal = pd.Series([i for i in range(1880, 2051)])
    plt.plot(xVal, 
             fit1880.intercept + fit1880.slope*xVal,
             label='fit with 1880-2013 data',
             c='green')

    # Create second line of best fit
    mask = df['Year']>=2000
    fit2000 = linregress(df['Year'][mask], df['CSIRO Adjusted Sea Level'][mask])
    xVal = pd.Series([i for i in range(2000, 2051)])
    plt.plot(xVal, 
             fit2000.intercept + fit2000.slope*xVal,
             label='fit with 2000-2013 data',
             c='red')

    # Add labels and title
    plt.xlabel('Year') 
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
