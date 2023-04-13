# Shijang Lin PSID: 2018904

# zyLab 12.9

from os import system

system('cls')

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    # FIXME: The following line will throw ValueError exception.
    #        Insert try/except blocks to catch the exception.
    try:
        age = int(parts[1]) + 1
    except ValueError:
        age = 0

    print(f'{name} {age}')

    # Get next line
    parts = input().split()
    name = parts[0]
