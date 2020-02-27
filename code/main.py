from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import os
import numpy as np
import pdb
from dates import Dates as dt
import tkinter as tk
import time as t
from datetime import datetime
from monthly import Monthly
from controller import Controller
#------------------------------TODO LIST---------------------------------------
# -Find monthly expenditures
# -Create graphical display of money spent and money deposited
# -Find way to delete canvas to make the GUI more dynamic (i.e. either
    #remove frames or canvas and use one)

class RepresentExpenditure(Controller):
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
#        self.clear_screen()
        super.clear_screen([self.parent, self.show_frame])
        self.file_exists()
        tk.Label(self.show_frame, text="The latest").pack()
        fiveFreq = tk.Listbox(self.show_frame)
        for i in range(0, self.NUMLATEST):
            fiveFreq.insert(i, self.X[i,:])
        fiveFreq.pack(fill=tk.BOTH, expand=True)

#TODO:  
    def line_plot(self):
        #Todo: Fix line plot to map only a few not whole years
        self.clear_screen()
        self.file_exists()
        #The following indexes are assuming that the X numpy array contains
            #values in the following order: date (year-month-day), names, 
            #expenditure, and income. I.e. 0,1,2,3
#        fields = self.find_fields()
        pdb.set_trace()
        fields = {'date': 0, 'name':1, 'expend':2, 'income':3}
        fig = Figure (figsize=(5, 5), dpi=100)
        f = fig.add_subplot(111)
        #These two statements get rid of 'NaN' values in the array
        self.X[pd.isnull(self.X[:, fields['income']]),fields['income']]=0
        self.X[pd.isnull(self.X[:, fields['expend']]),fields['expend']]=0
        net = self.X[:, fields['income']] - self.X[:, fields['expend']]
        #Get the year value ex. 2019 as a y-axis marker
        years = [i[0:4] for i in self.X[:, fields['date']]]
        f.plot(years, net, scalex=True)
        f.set_xlabel('Years')
        f.set_ylabel('Net Worth')
        canvas = FigureCanvasTkAgg (fig, self.show_frame)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill = tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill = tk.BOTH, expand=True)
        canvas.delete("all")
    
    def find_fields(self):
        #----------------------------------BAD CODE: FIX-----------------------
        #Getting user to input the values for the fields looking for dates, names,
            #expenditure, income (4 fields)
        fields = {'date', 'name', 'expenditure', 'income'}
        tk.Label(self.show_frame, text="Please index each column in their respective boxes",
                 font=("Ariel", 14)).pack(side=tk.TOP)
        self.statistics()
        tk.Label(self.show_frame, text="Dates").pack()
        date = tk.Entry(self.show_frame).pack()
        tk.Label(self.show_frame, text="Names").pack()
        name = tk.Entry(self.show_frame).pack()
        tk.Label(self.show_frame, text="Expenditure").pack()
        expend = tk.Entry(self.show_frame).pack()
        tk.Label(self.show_frame, text="Income").pack()
        income = tk.Entry(self.show_frame).pack()
        fields['date'] = date.get()
        fields['name'] = name.get()
        fields['expenditure'] = expend.get()
        fields['income'] = income.get()
        self.clear_screen()
        
    def file_exists(self):
        try:
            self.X.any()
        except:
            tk.Label(self.show_frame, text="Please load file first").pack()
        return None
        
    def export(self):
        #TODO: Implement to export an estimation of spending
        tk.messagebox.showinfo(title="Not Available", 
                               message="Function not implemented")
    
    def clear_screen(self):
        self.show_frame.destroy()
        self.show_frame = tk.Frame(self.parent)
        self.show_frame.pack()


class MainPage(tk.Frame):
    """Each function in this class requires a Tk object that executes a 
    mainloop """
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.top_frame = tk.Frame(self.parent)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.stats_obj = RepresentExpenditure(self.top_frame)
        self.create_MenuBar()
        self.monthly = Monthly(self, self.top_frame)
        tk.Label(self.top_frame, text="Load a .csv file to start",
                 font=("Ariel", 30, "bold")).pack()
        tk.Button(self.top_frame, text="Click to open file", 
                  command=lambda: self.stats_obj.load_dataset()).pack()
        tk.Button(self.top_frame, text="Load latest", 
                  command = lambda: self.stats_obj.statistics()).pack()
        tk.Button(self.top_frame, text="Line Plot",
                  command = lambda: self.stats_obj.line_plot()).pack()
        tk.Button(self.top_frame, text="Monthly Payments").pack()
        
        
        
        
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

