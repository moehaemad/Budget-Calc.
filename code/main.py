import pandas as pd
import os
import numpy as np
import monthly
import pdb
from dates import Dates as dt
import tkinter as tk
def load_dataset(filename):
    with open (os.path.join ('..','data',filename), 'rb') as f:
        return pd.read_csv(f, parse_dates = True)
    
def statistics (X, master=None):
    frame = tk.Frame (master)
    frame.pack(expand="YES")
    tk.Label(frame, text="The latest 5 entries of your statement").pack(side=tk.LEFT)
    fiveFreq = tk.Listbox(frame)
    for i in range(0,5):
        fiveFreq.insert(i,X[i,1])
    fiveFreq.pack(side=tk.RIGHT)
#    print("How many times did you spend most frequently " +  
#          str(np.max(plcounts)))
#    sumrange = input ("find total amount for what dates? (yyyy-mm-dd)-"
#                      +"(yyyy-mm-dd)")
#    datelist = dt.Dates.organize(sumrange)
    #TODO: Find total amount for the current date inputted


filename = input("please enter the name of the file in the date folder \n")
read = load_dataset(filename)
X = read.values
root = tk.Tk()
statistics (X, master=root)
root.mainloop()
#Create an array where NaN values are replaced with zero
#TODO: get np.nan_to_num to work with float numbers in the array
for i in range(X.shape[0]):
    if np.isnan(X[i,3]):
        X[i,3]=0
        #Filter repeating names of transactions
        places, plcounts = np.unique(X[:,1], return_counts=True)
        statistics (X)
        monthly.find_Monthly_Expenditure(places,plcounts)
