from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import os
import numpy as np
import pdb
from monthly import Monthly
from dates import Dates as dt
import tkinter as tk
import time as t

#------------------------------TODO LIST---------------------------------------
# -Find monthly expenditures
# -Create graphical display of money spent and money deposited
# -Find way to delete canvas to make the GUI more dynamic (i.e. either
    #remove frames or canvas and use one)

class RepresentExpenditure():
    def __init__(self, parent, X=None, *args, **kwargs):
        self.X = X
        self.parent = parent
        self.show_frame = tk.Frame(self.parent)
        self.show_frame.pack()
        self.kwargs = kwargs
        self.NUMLATEST = 10
            
    def load_dataset(self):
        f = tk.filedialog.askopenfilename()
        self.csv_file = pd.read_csv(f, parse_dates=True)
        self.X = self.csv_file.as_matrix()
        
#TODO: Create popup/widget to get NUMLATEST Value
        
    def statistics(self):
        try:
            self.X.any()
        except:
            tk.Label(self.show_frame, text="Please load file first").pack()
            return None
        self.show_frame.destroy()
        self.show_frame = tk.Frame(self.parent)
        self.show_frame.pack()
        tk.Label(self.show_frame, text="The latest").pack()
        fiveFreq = tk.Listbox(self.show_frame)
        for i in range(0, self.NUMLATEST):
            fiveFreq.insert(i, self.X[i,1])
        fiveFreq.pack(side=tk.RIGHT)

#TODO:  ONCE STATISTICS IS FUNCTIONAL, FIX THIS FUNCTION TO BE OBJECT ORIENTED
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
        
    def export(self):
        #TODO: Implement to export an estimation of spending
        tk.messagebox.showinfo(title="Not Available", 
                               message="Function not implemented")


class MainPage(tk.Frame):
    """Each function in this class requires a Tk object that executes a 
    mainloop """
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.top_frame = tk.Frame(self.parent)
        self.top_frame.pack()
        self.stats_obj = RepresentExpenditure(self.top_frame)
        self.create_MenuBar()
        tk.Label(self.top_frame, text="Load a .csv file to start",
                 font=("Ariel", 30, "bold")).pack()
        tk.Button(self.top_frame, text="Click to open file", 
                  command=lambda: self.stats_obj.load_dataset()).pack()
        tk.Button(self.top_frame, text="destroy frame", 
                  command = lambda: self.top_frame.destroy()).pack()
        tk.Button(self.top_frame, text="Load latest", 
                  command = lambda: self.stats_obj.statistics()).pack()
        
        
        
        
    def create_MenuBar(self):
        tk.Label(self.top_frame, text="Current time: " + str(t.localtime().tm_mon) + 
                 ", " + str(t.localtime().tm_year)).pack()
        mainmenu = tk.Menu(self.parent)
        #for now let NUMLATEST = 10
#        stats = RepresentExpenditure(self.top_frame, self.X, NUMLATEST=10)
        mainmenu.add_command(label="Stop", command = lambda: self.parent.destroy())
        mainmenu.add_command(label="Home", command = lambda: self.__init__(self.parent))
        filemenu = tk.Menu(mainmenu, tearoff=0)
        mainmenu.add_cascade(label="File", menu=filemenu)
#        filemenu.add_command(label="Open", command = lambda: self.load_dataset())
        filemenu.add_command(label="Export", command = lambda:
                self.stats_obj.export())
        root.config(menu=mainmenu)
#        statmenu = tk.Menu(mainmenu, tearoff=0)
#        statmenu.add_command(label= str(stats.NUMLATEST)+" latest transactions", 
#                             command = lambda: stats.statistics())
#        mainmenu.add_cascade(label="stats", menu=statmenu)
#        statmenu.add_command(label="linear graph trans.", command = lambda: 
#            line_plot(self.parent, self.X, self.parent))

if __name__ == '__main__':
    root = tk.Tk()
#    monthly = Monthly()
#   monthly.find_Monthly_Expenditure(X=X)
    root.geometry("500x500")

    MainPage(root).pack()
    root.mainloop()

