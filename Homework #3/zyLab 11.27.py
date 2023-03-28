# Shijang Lin PSID: 2018904

# zyLab 11.27

from os import system

system('cls')

new_dict = {}

for num in range(5):
    jnum = input(f"Enter player {num + 1}'s jersey number:\n")
    prate = input(f"Enter player {num + 1}'s rating:\n")

    if jnum not in new_dict:
        new_dict[int(jnum)] = int(prate)

    print()

print("ROSTER")
for k in sorted(new_dict):
    print(f'Jersey number: {k}, Rating: {new_dict[k]}')
