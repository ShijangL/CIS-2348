# Shijang Lin PSID: 2018904

# zyLab 12.9

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    # FIXME: The following line will throw ValueError exception.
    #        Insert try/except blocks to catch the exception.
    age = int(parts[1]) + 1
    print(f'{name} {age}')

    # Get next line
    parts = input().split()
    name = parts[0]
