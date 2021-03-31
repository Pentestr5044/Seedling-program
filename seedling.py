# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 11:20:57 2021

@author: pente
"""

import sys
import sqlite3
from sqlite3 import Error
#from date import usr_date
import datetime
#plantnamesearch=input("Please enter plant baby name to plant: ")
#print(usr_date())
i = 2
#menu = "Welcome to your planting program, your seed babies love you.\n Option 0 will install your database to begin saving plants.\n Option 1 will search through the plant babies for the one you are planting and give you all the yummy info for its lifecycle.\n Option 2 will put new seed babies into the database.\n Option 3 will DELETE babies from the database.\n Option 4 displays the whole database.\n Option 5 quits the program.\n Have fun! I love you!!.\n"
#print(menu)
#usr = int(input("Please enter choice: "))
while i == 2:
        menu = "\n Welcome to your planting program, your seed babies love you.\n Option 0 will install your database to begin saving plants.\n Option 1 will search through the plant babies for the one you are planting and give you all the yummy info for its lifecycle.\n Option 2 will put new seed babies into the database.\n Option 3 will DELETE babies from the database.\n Option 4 displays the whole database.\n Option 5 quits the program.\n Have fun! I love you!!.\n"
        print(menu)
        usr = int(input("Please enter choice: "))
        if usr == 0:
                def sql_connection():
                        try:
                                con = sqlite3.connect('seedlingdatabase2.db')
                                return con
                        except Error:
                                print(Error)
                def sql_table(con):
                        cursorObj = con.cursor()
                        cursorObj.execute("CREATE TABLE seedlings(pname text, pdepth real, pspacing real, psgerm integer, pfgerm integer, pstrans integer, pftrans integer, pharv integer)")
                        con.commit()
                        print("Plowing plots in a table for all of your informations....")
                con = sql_connection()
                sql_table(con)
                con.close()
        if usr == 1:
                pname = str(input("Please enter little seed babys name: "))
                def sql_connection():
                        try:
                                con = sqlite3.connect('seedlingdatabase2.db')
                                return con
                        except Error:
                                print(Error)
                con = sql_connection()
                def sql_table(con):
                        con = sqlite3.connect('seedlingdatabase2.db')
                        sql_query = """SELECT * FROM seedlings WHERE pname = ?"""
                        cursorObj = con.cursor()
                        cursorObj.execute(sql_query, (pname,))
                        row = cursorObj.fetchall()
                        for rows in row:
                                print(rows)
                                gs = rows[3]
                                pdate = str(input("Please enter little seed babys birthday mm/dd/yyy: "))
                                temp = datetime.datetime.strptime(pdate, '%m/%d/%Y')
                                new_date_temp = temp + datetime.timedelta(gs)
                                germ_start = new_date_temp.strftime('%m/%d/%Y')
                                ge = rows[4]
                                temp = datetime.datetime.strptime(pdate, '%m/%d/%Y')
                                new_date_temp = temp + datetime.timedelta(ge)
                                germ_end = new_date_temp.strftime('%m/%d/%Y')
                                ts = rows[5]
                                temp = datetime.datetime.strptime(pdate, '%m/%d/%Y')
                                new_date_temp = temp + datetime.timedelta(ts)
                                trans_start = new_date_temp.strftime('%m/%d/%Y')
                                tf = rows[6]
                                temp = datetime.datetime.strptime(pdate, '%m/%d/%Y')
                                new_date_temp = temp + datetime.timedelta(tf)
                                trans_end = new_date_temp.strftime('%m/%d/%Y')
                                hv = rows[7]
                                temp = datetime.datetime.strptime(pdate, '%m/%d/%Y')
                                new_date_temp = temp + datetime.timedelta(hv)
                                harvest = new_date_temp.strftime('%m/%d/%Y')
                                print("\n This is your germination range is <3 ", "from", germ_start, "To", germ_end, end=('\n'))
                                print("\n Your transplanting range is from <3 ", trans_start, "To ", trans_end)
                                print("\n THIS PLANTS FEED THE FAMILY DAY IS <3 ", harvest, end=('\n'))
                                spc = rows[1]
                                print("\nThis seed baby needs this much arm space: ", spc, "inches", end=("\n"))
                                dep = rows[2]
                                print("\nThis seed baby needs this much covers", dep, "inches\n")
                sql_table(con)
#pdate = int(input("Please enter little seed babys birthday mm/dd/yyy: "))
#temp = datetime.datetime.strptime(pdate, '%m/%d/%Y')
#new_date_temp = temp + datetime.timedelta(p)
        if usr == 2:
                name = str(input("Please enter seedlings name: "))
                depth = float(input("Please enter seedling depth in decimals: "))
                spc = float(input("Please enter spacing for seedling in decimals: "))
                germ_start = int(input("Please enter beginning range for germination in number of days. example: for 45 days from seed to start of germination put 45.\n Please enter number: "))
                germ_end = int(input("Please enter end of range for germination: "))
                transp = int(input("Please enter start of transplant range: "))
                transpf = int(input("Please enter transplant range end: "))
                harvest = int(input("Please enter the total number of days until harvest: "))
                entities=[name, depth, spc, germ_start, germ_end, transp, transpf, harvest]
                con = sqlite3.connect('seedlingdatabase2.db')
                def sql_insert(con, entities):
                        cursorObj = con.cursor()
                        cursorObj.execute('INSERT INTO seedlings(pname, pdepth, pspacing, psgerm, pfgerm, pstrans, pftrans, pharv) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entities)
                        con.commit()
                sql_insert(con,entities)
                print("\nSeedling saved for later use YAY! more food for the family! You are an amazing woman, and I love you\n SO MUCH!!!!!!!!!\n\n\n")
            
            
        if usr == 5:
                print("Goobye! I love you")
                i = 1
#p = 900
#string = str(usr_date())
#temp = datetime.datetime.strptime(string, '%m/%d/%Y')
#new_date_temp = temp + datetime.timedelta(p)
#new_date = new_date_temp.strftime('%m/%d/%Y')
#print('This is your new date: ', new_date)



















#menu for selection option 0 creates the database seedlings.sql option 1
#calls from the databse by name and sets the planting date by format of mm/dd/yyy
#option 2 creates a new entry with seedling name, pdepth, germrange, transrange, harvest
#option 3 deletes an entry from the database by seedling name.
#option 4 prints out all entries in the database and puts them into a CSV file for review
#option 5 exits program with sys.exit the nice way.
#each option must loop back to the menu unless 5 is pushed. 