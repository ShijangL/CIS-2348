# Shijang Lin PSID: 2018904

# Coding Problem 2

import datetime
from os import system

system('cls')
current_date = datetime.date.today()
found = False
month = {
            'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
            'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11,
            'December': 12
        }
with open('inputDates.txt', 'r') as datefile:
    date = datefile.readline()
    output = open('parsedDates.txt', 'w')
    while date:
        for i in month:
            if date.find(i) != -1:
                found = True
            else:
                continue
            if found:
                newlist = date.split()
                newlist[0] = month[newlist[0]]
                num_date = datetime.date(int(newlist[2]), int(newlist[0]), int(newlist[1].replace(',', '')))
                if num_date < current_date and ',' in newlist[1]:
                    output.write(f"{newlist[0]}/{newlist[1].replace(',', '')}/{newlist[2]}\n")
            date = datefile.readline()
            output.close()
