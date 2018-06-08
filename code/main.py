import pandas as pd
import os
import numpy as np
import monthly
import pdb
from dates import Dates as dt
import tkinter as tk

#------------------------------TODO LIST---------------------------------------
# -Find monthly expenditures
# -Create graphical display of money spent and money deposited
# -create graphical display of total amount

def close (master):
    master.destroy()
    
def createFrames(master):
    statframe = tk.Frame(master)
    return [statframe]
def destroyFrames(frames):
    for frame in frames:
        frame.destroy()
    return 0

def load_dataset(filename):
    with open (os.path.join ('..','data',filename), 'rb') as f:
        return pd.read_csv(f, parse_dates = True)
    
def statistics (statframe,X):
    tk.Label(statframe, text="The latest 5 entries of your statement").pack(side=tk.LEFT)
    fiveFreq = tk.Listbox(statframe)
    for i in range(0,5):
        fiveFreq.insert(i,X[i,1])
    fiveFreq.pack(side=tk.RIGHT)
    mainbtn = tk.Button(statframe, text="main menu", command=main)
    mainbtn.pack(side=tk.TOP)
    statframe.pack(expand=tk.YES)

def main():
    read = load_dataset("visa.csv")
    X = read.values
    root = tk.Tk()
    mainmenu = tk.Menu(root)
    framelist = createFrames(root)
    mainmenu.add_command(label="stop", command = lambda: close(master=root))
    statmenu = tk.Menu(mainmenu,tearoff=0)
    statmenu.add_command(label="5 latest transactions", command = 
                         lambda: statistics(framelist[0],X))
    mainmenu.add_cascade(label="stats", menu=statmenu)
    root.config(menu=mainmenu)
    root.mainloop()
    
if __name__ == '__main__':
    main()
#Create an array where NaN values are replaced with zero

#pdb.set_trace()
#for i in range(X.shape[0]):
#    if np.isnan(X[i,3]):
#        X[i,3]=0
#        #Filter repeating names of transactions
#        places, plcounts = np.unique(X[:,1], return_counts=True)
#        statistics (X)
#        monthly.find_Monthly_Expenditure(places,plcounts)
