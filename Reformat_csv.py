#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pandas as pd
import os
import sys
import datetime
import wget

# init variables
today = datetime.datetime.now()
oneday=datetime.timedelta(days=1) 
yday= today-oneday
dateFormat=yday.strftime('%Y%m%d')
# pour test
dateFormat="20221121"

currentDir=os.path.dirname(os.path.abspath(__file__))
yearCurrentDir="{path}\\{dir}\\".format(path=currentDir,dir=yday.strftime('%Y'))
rawDir="{path}\\RAW\\".format(path=currentDir)
fileToDay="touch_{dateFormat}.csv".format(dateFormat=dateFormat)
_ipMyPelletronic="127.0.0.1"


# Get fichiers
# pathSource="C:\\Users\\wilfrid.arthemise\\Documents\\200 - okovision\\"
wget.download()

print(os.path.exists(yearCurrentDir))
print(os.path.exists(rawDir))
print(os.path.exists(currentDir+"\\"+fileToDay))
