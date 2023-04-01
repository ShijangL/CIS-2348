# Shijang Lin PSID: 2018904

# Final Project Part 1

from os import system
import csv
import datetime

system('cls')

Mlist = []
Plist = []
Slist = []

# Copy the datas from the files into a list that can be scriptable

with open('ManufacturerList.csv', 'r') as ManufacturerList:
    ManuList = csv.reader(ManufacturerList, delimiter=',')

    for m in ManuList:
        Mlist.append(m)

with open('PriceList.csv', 'r') as PriceList:
    PrList = csv.reader(PriceList, delimiter=',')

    for p in PrList:
        Plist.append(p)

with open('ServiceDatesList.csv', 'r') as ServiceList:
    SDateList = csv.reader(ServiceList, delimiter=',')

    for s in SDateList:
        Slist.append(s)
