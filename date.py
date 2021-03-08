# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 14:19:35 2021

@author: pente
"""

from datetime import datetime
def usr_date():
    usrDate = str(input('please enter planting date m/d/y: '))
    date1 = datetime.strptime(usrDate, '%m/%d/%Y')
    date = date1.strftime('%m/%d/%Y')
    return date #check input for date needs to be the output of month/day/year no time necissary
#right now
