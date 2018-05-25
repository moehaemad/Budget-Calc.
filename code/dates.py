from datetime import date
import numpy as np
import pdb

class Dates:
#Create a hashmap with a date and it's respective index in the original X array
#Take as input a string of a date range
    
    #Consider implementing binary tree based for year,month,and day based on
    #frequencies
    
    #Organize a list of dates to date objects. Return -1 if format is not valid
    def organize (strdate):
        #TODO: find way to split the string into a datetime object and send it
        #off to dictionaryDates
        #TODO: Find clever way of finding format of the string returned
        
        if not errorchecking(strdate):
            return 0
        pdb.set_trace()
        year = 0
        month = 0
        day = 0
        #TODO: convert to Date object
        i=0
        if len(strdate)>10:
            while (i != -1):
                print ("Something")
        elif len(strdate) == 10:
            year = int(strdate[0:4])
            month = int(strdate[0:7])
            day = int (strdate[0:10])
        #Assuming format will be in year-month-day "-" year-month-day
        return 0
    def createHashDates(X023):
        #X023 is X[:,[0,2,3]] which contains dates, money spent, payment
        #respectively
        index = np.inf
        strdate = ''
        return strdate, index
#    def update ()#don't really need the update function right now but maybe
        #later
    def errorChecking (dateinput):
        #Example input: 2018-02-22-2019-02-22
        return 0