# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 16:42:21 2021

@author: pente
"""
import datetime
from date import usr_date
p = 9
string = str(usr_date())
temp = datetime.datetime.strptime(string, '%m/%d/%Y')
new_date_temp = temp + datetime.timedelta(p)
new_date = new_date_temp.strftime('%m/%d/%Y')
print('This is your new date: ', new_date)