# Shijang Lin PSID: 2018904

# Lab 9.10

import csv

new_dict = {}
filename = input()
with open(filename, 'r') as myfile:
    aline = list(csv.reader(myfile, delimiter=','))

    for i in aline[0]:
        if new_dict.get(i, 0) == 0:
            new_dict[i] = 1
        else:
            new_dict[i] += 1

for k in new_dict:
    print(f'{k} {new_dict[k]}')
