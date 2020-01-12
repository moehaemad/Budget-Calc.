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

class RepresentExpenditure():
    def __init__(self, X, parent, *args, **kwargs):
        self.X = X
        self.frame = parent
        self.kwargs = kwargs
        self.NUMLATEST = kwargs["NUMLATEST"] #temporary number, will make user 
            #entered
        
    def statistics(self):
        tk.Label(self.frame, text="The latest").pack()
        fiveFreq = tk.Listbox(self.frame)
        for i in range(0, self.NUMLATEST):
            fiveFreq.insert(i, self.X[i,1])
        fiveFreq.pack(side=tk.RIGHT) 
        #NOT SURE IF I SHOULD PACK FRAME TWICE ONCE
            #IN MAINPAGE CLASS AND THE OTHER HERE
        #self.frame.pack(expand=tk.YES)
    
    def line_plot(self, frames, X, master):
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


class MainPage(tk.Frame):
    """Each function in this class requires a Tk object that executes a 
    mainloop """
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        pdb.set_trace()
        self.parent = parent
        self.top_frame = tk.Frame(self.parent)
        self.top_frame.pack()
        
        tk.Label(self.top_frame, text="Load a .csv file to start",
                 font=("Ariel", 30, "bold")).pack()
        tk.Button(self.top_frame, text="Click to open file",
                                      command=self.load_dataset).pack()
        tk.Button(self.top_frame, text="destroy frame", 
                  command = lambda: self.top_frame.pack_forget).pack()
        
        
        
    
    def load_dataset(self):
        f = filedialog.askopenfilename()
        self.csv_file = pd.read_csv(f, parse_dates=True)
        self.X = self.csv_file.as_matrix()
        
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

    
if __name__ == '__main__':
    root = tk.Tk()
#    monthly = Monthly()
#   monthly.find_Monthly_Expenditure(X=X)
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
#    statmenu.add_command(label="linear graph trans.", command = lambda: 
#    line_plot(frames, X, root))
    mainmenu.add_cascade(label="stats", menu=statmenu)
    root.config(menu=mainmenu)
    MainPage(root).pack()
    root.mainloop()

