# Shijang Lin PSID: 2018904

# Final Project Part 2

from os import system
import csv
import datetime

system('cls')


Mlist = []
Plist = []
Slist = []

# Copy the datas from the files into a list that can be scriptable

with open('D:\School\CIS\CIS 2348 Final Project\ManufacturerList.csv', 'r') as ManufacturerList:
    ManuList = csv.reader(ManufacturerList, delimiter=',')

    for m in ManuList:
        Mlist.append(m)

with open('D:\School\CIS\CIS 2348 Final Project\PriceList.csv', 'r') as PriceList:
    PrList = csv.reader(PriceList, delimiter=',')

    for p in PrList:
        Plist.append(p)

with open('D:\School\CIS\CIS 2348 Final Project\ServiceDatesList.csv', 'r') as ServiceList:
    SDateList = csv.reader(ServiceList, delimiter=',')

    for s in SDateList:
        Slist.append(s)

Manufacturers = []
Tlist = []

# sort the Manufacturers and types

for company in Mlist:
    if company[1].replace(" ", "").capitalize() not in Manufacturers:
        Manufacturers.append(company[1].replace(" ", "").capitalize())
    if company[2].replace(" ", "").capitalize() not in Tlist:
        Tlist.append(company[2].replace(" ", "").capitalize())

Manufacturers.sort()
Tlist.sort()

current_date = datetime.date.today()
search_manu = []
search_type = []
state = ""
types = []
prices = []

search = input("Input the manufacturer and item type:\n")
searchlist = search.split()

for i in searchlist:
    for k in Manufacturers:
        if i.capitalize() == k:
            search_manu.append(k)
    for l in Tlist:
        if i.capitalize() == l:
            search_type.append(l)

if len(search_manu) != 1 or len(search_type) != 1 or (len(search_manu) != 1 and len(search_type) != 1):
    print("No such item in inventory")
    search_manu = []
    search_type = []

for a in range(len(Mlist)):
    if (Mlist[a][2].replace(" ", '').capitalize()) == search_type[0].capitalize():
        types.append(Mlist[a][0])
        if (Mlist[a][1].replace(" ", '').capitalize()) == search_manu[0].capitalize():
            uid = Mlist[a][0]
            for money in Plist:
                if uid in money[0]:
                    prices.append(int(money[-1]))

if len(prices) > 1:
    prices.sort()
    max_price = prices[-1]

    for b in range(len(Mlist)):
        if (Mlist[b][2].replace(" ", '').capitalize()) == search_type[0].capitalize():
            if (Mlist[b][1].replace(" ", '').capitalize()) == search_manu[0].capitalize():
                product = Mlist[b][2]
                manufacturer = Mlist[b][1]
                ids = Mlist[b][0]
                state = Mlist[b][-1]
                for cost in range(len(Plist)):
                    if int(Plist[cost][-1]) == max_price and ids == Plist[cost][0]:
                        price = Plist[cost][-1]
                for service in range(len(Slist)):
                    if ids == Slist[service][0]:
                        date = Slist[service][-1]
                        new_date = date.split('/')
    if (current_date < datetime.date(int(new_date[2]), int(new_date[0]), int(new_date[1]))) and (state != "damaged"):
        print(f"Your item is: {ids}, {manufacturer}, {product}, {price}")
else:
    for b in range(len(Mlist)):
        if (Mlist[b][2].replace(" ", '').capitalize()) == search_type[0].capitalize():
            if (Mlist[b][1].replace(" ", '').capitalize()) == search_manu[0].capitalize():
                product = Mlist[b][2]
                manufacturer = Mlist[b][1]
                ids = Mlist[b][0]
                state = Mlist[b][-1]
                for cost in Plist:
                    if ids in cost[0]:
                        price = cost[-1]
                for service in range(len(Slist)):
                    if ids == Slist[service][0]:
                        date = Slist[service][-1]
                        new_date = date.split('/')
    if (current_date < datetime.date(int(new_date[2]), int(new_date[0]), int(new_date[1]))) and (state != "damaged"):
        print(f"Your item is: {ids}, {manufacturer}, {product}, {price}")

if len(types) > 1:
    for d in types:
        for c in range(len(Mlist)):
            if Mlist[c][0] == d and Mlist[c][1].replace(" ", "").capitalize() != search_manu[0].capitalize():
                for buy in Plist:
                    if Mlist[c][0] == buy[0] and (int(buy[-1]) >= (int(price) - 200) and (int(buy[-1]) <= (int(price) + 200))):
                        price_alt = buy[-1]
                        ids = buy[0]
                        for k in Mlist:
                            if k[0] == ids:
                                product = k[2]
                                manufacturer = k[1]
                                state = k[-1]
                                for service in range(len(Slist)):
                                    if ids == Slist[service][0]:
                                        date = Slist[service][-1]
                                        new_date = date.split('/')
                    else:
                        price_alt = -1

    if ((current_date < datetime.date(int(new_date[2]), int(new_date[0]), int(new_date[1]))) and (state != "damaged")) and (price_alt > 0):
        print(f"You may, also, consider: {ids}, {manufacturer}, {product}, {price_alt}")
