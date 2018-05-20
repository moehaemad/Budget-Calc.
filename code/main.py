import pandas as pd
import os
import numpy as np
import monthly
import pdb
from dates import Dates
def load_dataset(filename):
    with open (os.path.join ('..','data',filename), 'rb') as f:
        return pd.read_csv(f, parse_dates = True)
    
def statistics (X):
    print ("The latest 5 entries of your statement")
    print (X[0:4,:])
#    frequencies = dict(zip(places,plcounts))
#    pdb.set_trace()
    print("How many times did you spend most frequently " +  
          str(np.max(plcounts)))
    sumrange = input ("find total amount for what dates? (yyyy-mm-dd)-"
                      +"(yyyy-mm-dd)")
    date1,date2 = Dates.organize(sumrange)
    #TODO: Find total amount for the current date inputted

    
    
filename = input("please enter the name of the file in the date folder")
read = load_dataset(filename)
X = read.values
#Create an array where NaN values are replaced with zero
#TODO: get np.nan_to_num to work with float numbers in the array
for i in range(X.shape[0]):
    if np.isnan(X[i,3]):
        X[i,3]=0
#Filter repeating names of transactions
places, plcounts = np.unique(X[:,1], return_counts=True)
statistics (X)
monthly.find_Monthly_Expenditure(places,plcounts)
        
