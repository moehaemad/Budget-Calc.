from datetime import date
import numpy as np
import pdb

class Dates:
#Create a hashmap with a date and it's respective index in the original X array
#Take as input a string of a date range
    
    #Consider implementing binary tree based for year,month,and day based on
    #frequencies
    
    def organize (strdate):
        #TODO: find way to split the string into a datetime object and send it
        #off to dictionaryDates
        #TODO: Find clever way of finding format of the string returned
        pdb.set_trace()
        first = strdate[0:10]
        second = strdate[11:21]
        #Assuming format will be in year-month-day "-" year-month-day
        return first, second
    def createHashDates(a):
        #a is a matrix of dates
        index = np.inf
        strdate = ''
        return strdate, index
#    def update ()#don't really need the update function right now but maybe
        #later
    def errorChecking (dateinput):
        #Example input: 2018-02-22-2019-02-22
        return 0