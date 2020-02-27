import numpy as np
import pdb;
class Monthly:
    
    def find_Monthly_Expenditure (self, X,*args):
    #    frequencies = dict(zip(names,counts))
    #    print (frames) #don't think I need frames but not sure right now
    
    #algorithm for finding monthly payments:
    #-for list of places starting from most frequent find (%) of the consistency
    #of payments where 1 is 100% and all payments have been the same previously
    #O(n)
    #iterate through X_O(n) and get percentage
        _sorted_places = X[np.argsort(X[:,1], kind='mergesort', axis=0), 0:2]
        places, counts = np.unique(_sorted_places[:,1], return_counts = True)
        _up_counts= dict(zip(places, counts))
        payments = X[:,2]
        most_freq = np.bincount(counts)
#        for i in range(0, len(places)-1):
#            #placing dummy statement because not sure whether to include for-loop
#            print("testing function")
        #create dictionary of the sums of payments made for each place
        #sample solution: create array of true values for which you can find
        #payments were made and for what amount
        truth_array = X[:,1] == places[1]
        np.unique (truth_array*X[:,1])
        
#        _up_payments = dict(zip())
        
        std_dev = np.ones(len(payments))
        #find percentages of the current price with respect to others
#        for i, price in range(0,len(payments)), payments:
#            std_dev[i] = stdev(price)
#        pdb.set_trace()
    
    def manual_entry(self, names):
        for i in range(len(names)):
            answer = input ("Is " + names[i] + " a monthly ependiture")
            if (answer == "y"):
                self.monthlies[i] = names[i]
    def __init__ (self, main, frame):
        #require the main object in which the monthly class was instantiated in
            #and the frame it's using to draw representations in.
        self.frame = frame
        self.main = main
#        pdb.set_trace()
#        self.main.RepresentExpenditure(self.frame).clear_screen()

            