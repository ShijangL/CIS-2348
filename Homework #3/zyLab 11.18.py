# Shijang Lin PSID: 2018904

# zyLab 11.18

string = input()
intlist = string.split()

newlist = []

for i in intlist:
    if int(i) >= 0:
        newlist.append(int(i))

newlist.sort()
for j in newlist:
    print(j, end=' ')
