# Shijang Lin PSID: 2018904

# Final Project Part 1

from os import system
import csv
import datetime

system('cls')


def sortids(idslist):
    return idslist[0]


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

Manufacturers = []
Tlist = []

# sort the Manufacturers and types

for company in Mlist:
    if company[1] not in Manufacturers:
        Manufacturers.append(company[1])
    if company[2] not in Tlist:
        Tlist.append(company[2])

Manufacturers.sort()
Tlist.sort()

# Loop to write Full Inventory file

with open('FullInventory.csv', 'w', newline='') as FullInventory:
    list_writer = csv.writer(FullInventory)
    for name in Manufacturers:
        for run in range(len(Mlist)):
            if name in Mlist[run][1]:
                ids = Mlist[run][0]
                for cost in Plist:
                    if ids in cost[0]:
                        price = cost[-1]
                for service in Slist:
                    if ids in service[0]:
                        date = service[-1]
                for model in Mlist:
                    if ids in model[0]:
                        types = model[2]
                        if model[-1] == 'damaged':
                            list_writer.writerow([ids, name, types, price, date, model[-1]])
                        else:
                            list_writer.writerow([ids, name, types, price, date])

# Loop for item types

for t in Tlist:
    t = t.title()
    with open(f'{t}Inventory.csv', 'w', newline='') as Typelist:
        type_writer = csv.writer(Typelist)
        new_list = []
        for run in range(len(Mlist)):
            if Mlist[run][2].title() == t:
                i = Mlist[run][0]
                for cost in Plist:
                    if i in cost[0]:
                        price = cost[-1]
                for service in Slist:
                    if i in service[0]:
                        date = service[-1]
                for model in Mlist:
                    if i in model[0]:
                        name = model[1]
                        if model[-1] == 'damaged':
                            new_list.append([i, name, price, date, model[-1]])
                        else:
                            new_list.append([i, name, price, date])

        new_list.sort(key=sortids)
        type_writer.writerows(new_list)
