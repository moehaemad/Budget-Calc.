from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import os
import numpy as np
import pdb
from monthly import Monthly
from dates import Dates as dt
import tkinter as tk
from tkinter import filedialog
import time as t

#------------------------------TODO LIST---------------------------------------
# -Find monthly expenditures
# -Create graphical display of money spent and money deposited
# -Find way to delete canvas to make the GUI more dynamic (i.e. either
    #remove frames or canvas and use one)
NUMLATEST = 10
#-----------------------------Tkinter functions-------------------------------#
def close(master):
    master.destroy()
    
def create_frames(master):
    statframe = tk.Frame(master)
    frames = list()
    frames.append(statframe)
    return frames

def destroy_frames(frames): #put this into a class to avoid supplying each and
    #every single frame so the frames can be indexed with "self."
    if (len(frames) == 0):
        return 0
    for frame in frames:
        frame.destroy()
        

#-----------------------------Statistics--------------------------------------#
def load_dataset(filename):
    f = filedialog.askopenfilename()
    return pd.read_csv(f, parse_dates = True)
    
def statistics(frames, X):
    statframe = frames.pop(0)
    if (len(frames) >= 1):
        destroy_frames(frames)
    tk.Label(statframe, text="The latest").pack()
    fiveFreq = tk.Listbox(statframe)
    for i in range(0, NUMLATEST):
        fiveFreq.insert(i, X[i,1])
    fiveFreq.pack(side=tk.RIGHT)
    statframe.pack(expand=tk.YES)
    
def line_plot(frames, X, master):
    destroy_frames(frames)
    fig = Figure (figsize=(5, 5), dpi=100)
    f = fig.add_subplot(111)
    X[pd.isnull(X[:, 3]),3]=0
    X[pd.isnull(X[:, 2]),2]=0
    spending = X[:, 2]*-1 + X[:, 3]
    years = [i[0:4] for i in X[:, 0]]
    f.plot(years, spending, scalex=True)
    canvas = FigureCanvasTkAgg (fig, master)
    canvas.show()
    canvas.get_tk_widget().pack(side=tk.TOP, fill = tk.BOTH, expand=True)
    canvas._tkcanvas.pack(side=tk.TOP, fill = tk.BOTH, expand=True)
    canvas.delete("all")

if __name__ == '__main__':
    read = load_dataset("visa.csv")
    X = read.as_matrix()
    monthly = Monthly()
    monthly.find_Monthly_Expenditure(X=X)
    root = tk.Tk()
    root.geometry("500x500")
    t.localtime.__getattribute__
    tk.Label(root, text="Current time: " + str(t.localtime().tm_mon) + ", " +
             str(t.localtime().tm_year)).pack()
    mainmenu = tk.Menu(root)
    frames = create_frames(root)
    mainmenu.add_command(label="stop", command = lambda: close(master=root))
    statmenu = tk.Menu(mainmenu, tearoff=0)
    statmenu.add_command(label= str(NUMLATEST)+" latest transactions", 
                         command = lambda: statistics(frames,X))
    statmenu.add_command(label="linear graph trans.", command = lambda: 
        line_plot(frames, X, root))
    mainmenu.add_cascade(label="stats", menu=statmenu)
    root.config(menu=mainmenu)
    root.mainloop()

