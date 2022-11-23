#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Le script sera schedulé a la place du script Bash actuel sur le NAS.
Le script corrige les Features ajoutée par la derniere mise à jours de Okofen
Okovision est donc perturbé par les colonne "Electrique" en plus
"""

import pandas as pd
import os
import sys
import datetime
from wget import download
import shutil

# init variables
today = datetime.datetime.now()
oneday=datetime.timedelta(days=1) 
yday= today-oneday
dateFormat=yday.strftime('%Y%m%d')
# Repertoire & fichier
currentDir=os.path.dirname(os.path.abspath(__file__))
yearCurrentDir="{path}\\{dir}\\".format(path=currentDir,dir=yday.strftime('%Y'))
rawDir="{path}\\RAW\\".format(path=currentDir)
fileYDay="touch_{dateFormat}.csv".format(dateFormat=dateFormat)
okovisionDir="/volume1/web/okovision/tmp"
# Informations Chaudiere
_ipMyPelletronic="127.0.0.1"
urlPelletronic="https://{ip}/ogfiles/pelletronic/".format(ip=_ipMyPelletronic)
# Manipulation CSV
separator = ";"
listColumnToKeep=["Datum ","Zeit ","AT [°C]"," ATakt [°C]","PE1_BR1","HK1 VL Ist[°C]","HK1 VL Sol[°C]","HK1 RT Ist[°C]","HK1 RT Soll[°C]","HK1 Pumpe","HK1 Mischer","HK1 Fernb[°C]","HK1 Status","WW1 EinT Ist[°C]","WW1 AusT Ist[°C]","WW1 Soll[°C]","WW1 Pumpe","WW1 Status","PE1 KT[°C]","PE1 KT_SOLL[°C]","PE1 UW Freigabe[°C]","PE1 Modulation[%]","PE1 FRT Ist[°C]","PE1 FRT Soll[°C]","PE1 FRT End[°C]","PE1 Einschublaufzeit[°C]","PE1 Pausezeit[zs]","PE1 Luefterdrezahl[%]","PE1 Saugzugdrehzahl[%]","PE1 Unterdruck Ist[EH]","PE1 Undruck Soll[EH]","PE1 Fuellstand[kg]","PE1 Fuellstand ZWB[kg]","PE1 Status","PE Motor ES","PE1 Motor RA","PE1 Motor RES1","PE1 Motor TURBINE","PE1 Motor ZUEND","PE1 Motor UW[%]","PE1 Motor AV","PE1 Motor RES2","PE1 Motor MA","PE1 Motor RM","PE1 Motor SM","PE1 Res1 Temp.[°C]","PE1 Res2 Temp.[°C]","PE1 CAP RA","PE1 CAP ZB","PE1 AK","PE1 Saug-Int[min]","PE1 DigIn1","PE1 DigIn2","Fehler1","Fehler2","Fehler3"]


# Get fichiers sur la chaudiere
wget.download(urlPelletronic+fileYDay)

# Manipulation du CSV
f=pd.read_csv(currentDir+"\\"+fileYDay, sep=separator)
new_f = f[listColumnToKeep]
new_f.to_csv(yearCurrentDir+fileYDay , index=False, sep=separator)

# Copy aux differents endroits
shutil.copy(currentDir+"\\"+fileYDay,okovisionDir)
shutil.copy(currentDir+"\\"+fileYDay,rawDir )


