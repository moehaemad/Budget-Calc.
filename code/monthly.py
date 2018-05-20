import numpy as np
def find_Monthly_Expenditure (names, counts):
#    frequencies = dict(zip(names,counts))
    monthlies = np.array (np.shape(names))
    
    for i in range(len(names)):
        answer = input ("Is " + names[i] + " a monthly ependiture")
        if (answer == "y"):
            monthlies[i] = names[i]
        

        