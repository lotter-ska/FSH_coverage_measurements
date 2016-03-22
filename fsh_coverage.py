# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 08:38:33 2015

@author: lkock
C:\Users\Public\Documents\Rohde-Schwarz\FSH4View\gsm3
"""
#filename="Sweep 0001 (2015-11-17 11.21.12 AM).csv"

import os
import glob
import csv
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from Tkinter import Tk
from tkFileDialog import askopenfilename


x=0
tresh=-180



dbm=zeros(shape=(len(glob.glob('*.csv')),631))
dbm_max=zeros(shape=(len(glob.glob('*.csv')),1))
f_max=zeros(shape=(len(glob.glob('*.csv')),1))
time=[{}]*len(glob.glob('*.csv'))
geo=[{}]*len(glob.glob('*.csv'))
lati=[{}]*len(glob.glob('*.csv'))
loni=[{}]*len(glob.glob('*.csv'))
time2=np.empty([len(glob.glob('*.csv')),1])


antenna = askopenfilename(title="Select Antenna Cal File",initialdir=(os.path.expanduser("C:\RFI Archive\Equipment_Database\Passive_Antennas"))) # show an "Open" dialog box and return the path to the selected file
antenna_cal = loadtxt(antenna,delimiter=',',usecols=range(0,4),skiprows=1)




for filename in glob.glob('*.csv'):
    data = loadtxt(filename,delimiter=',',usecols=range(0,2),skiprows=46)
    
    lat=np.genfromtxt(filename,delimiter=',',skip_header=3, dtype=None)[0,1].translate(None, '''' S" ''')
    lati[x]=-1*(float(lat[0:2])+float(lat[4:len(lat)])/60)
    lon=np.genfromtxt(filename,delimiter=',',skip_header=3, dtype=None)[1,1].translate(None, '''' S" ''')
    loni[x]=float(lon[0:2])+float(lon[4:len(lat)])/60
    af=interp(data[:,0],antenna_cal[:,1],antenna_cal[:,3])

    time[x]=filename[12:31]
    time2[x]=(datestr2num(filename[23:31].replace('.',':')))
    dbm[x]=data[:,1]+107+af
    dbm_max[x]=max(data[:,1])
    f_max[x]=data[data[:,1]==dbm_max[x],0]
    dbm_max[x]=max(dbm[x])
    geo[x] = " lat %s lon %s " % (lati[x], loni[x])
    x=x+1
    
    

f=data[:,0]

x=10
y=20

subplot(121)
imshow(dbm, aspect='auto')
title("Measured E-field vs position and frequency")

xticks(arange(0,len(f),len(f)/6),arange(920,990,10))
t_ind=arange(0,len(dbm),len(dbm)/10)
yticks(t_ind,geo[1:len(dbm):len(dbm)/10])

colorbar()
xlabel('Frequency MHz')

subplot(122)
hist(f_max,60e6/200e3)
grid()
xlabel('Frequency MHz')
title("Histogram of frequencies of Max E Fields in band")

out=zeros(shape=(len(time),4))
#out[:,0:2]=gps[0:len(time),0:2]
out[:,0]=lati
out[:,1]=loni
out[:,2]=dbm_max[:,0]
out[:,3]=f_max[:,0]


with open("output.csv", "wb") as f:  
    writer = csv.writer(f)
    writer.writerows(out)
