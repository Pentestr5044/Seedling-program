# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 18:36:18 2021

@author: pente
"""

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print('connected to SQL database')
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
if __name__ == '__main__':
    create_connection(r'C:/Users/pente/Desktop/SeedlingProgram/seedlingdatabase1.db')
    print ('Your seed baby nursary database has been tilled, seeded, and grown.')
print ('Adding plots to the field for your plant babies......this might take a second.')


    
    
    