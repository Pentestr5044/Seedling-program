# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 11:20:57 2021

@author: pente
"""

import sys
import sqlite3
from date import usr_date
import datetime
menu="Welcome to your planting program, your seed babies love you.\n Option 0 will install your database to begin saving plants.\n Option 1 will search through the plant babies for the one you are planting and give you all the yummy info for its lifecycle.\n Option 2 will put new seed babies into the database.\n Option 3 will DELETE babies from the database.\n Option 4 displays the whole database.\n Option 5 quits the program.\n Have fun! I love you!!.\n"
#plantnamesearch=input("Please enter plant baby name to plant: ")
#print(usr_date())
p = 900
string = str(usr_date())
temp = datetime.datetime.strptime(string, '%m/%d/%Y')
new_date_temp = temp + datetime.timedelta(p)
new_date = new_date_temp.strftime('%m/%d/%Y')
print('This is your new date: ', new_date)



















#menu for selection option 0 creates the database seedlings.sql option 1
#calls from the databse by name and sets the planting date by format of mm/dd/yyy
#option 2 creates a new entry with seedling name, pdepth, germrange, transrange, harvest
#option 3 deletes an entry from the database by seedling name.
#option 4 prints out all entries in the database and puts them into a CSV file for review
#option 5 exits program with sys.exit the nice way.
#each option must loop back to the menu unless 5 is pushed. 