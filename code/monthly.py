import numpy as np

class Monthly:
    def create_dictionary (X):
        return 0
    
    
    #TODO: sort the array of X[:,[0,1]] s.t. name and date are sorted together
        #respectively. Sort on X[:,1](names) alphabetically
    def find_Monthly_Expenditure (self, X,*args):
    #    frequencies = dict(zip(names,counts))
    #    print (frames) #don't think I need frames but not sure right now
        _sortedplaces = X[np.argsort(X[:,1]), :]
        import pdb; pdb.set_trace()
        create_dictionary (X[:,[0,1]])
    
    def manual_entry(self, names):
        for i in range(len(names)):
            answer = input ("Is " + names[i] + " a monthly ependiture")
            if (answer == "y"):
                self.monthlies[i] = names[i]
    
            