# Shijang Lin PSID: 2018904

# zyLab 11.27

from os import system

system('cls')


def print_menu():
    letter = "aduroq"
    command = ' '
    menu = ("\nMENU\n"
            "a - Add player\n"
            "d - Remove player\n"
            "u - Update player rating\n"
            "r - Output players above a rating\n"
            "o - Output roster\n"
            "q - Quit\n")

    while command != 'q':
        print(menu, end='\n')
        command = input("Choose an option:\n")
        while command not in letter:
            command = input("Choose an option:\n")
        if command == 'a':
            new_jersey = int(input("Enter a new player jersey number:\n"))
            rating = int(input("Enter player's rating:\n"))

            if new_jersey not in new_dict:
                new_dict[new_jersey] = rating
        if command == 'd':
            new_jersey = int(input("\nEnter a player jersey number:\n"))
            if new_jersey in new_dict:
                del new_dict[new_jersey]
        if command == 'u':
            new_jersey = int(input("\nEnter a player jersey number:\n"))
            rating = int(input("\nEnter player's new rating:\n"))
            if new_jersey in new_dict:
                new_dict[new_jersey] = rating
        if command == 'r':
            rating = int(input("Enter a rating:\n"))
            print(f"ABOVE {rating}")
            for kl in sorted(new_dict):
                if new_dict[kl] > rating:
                    print(f"Jersey number: {kl}, Rating: {new_dict[kl]}")
        if command == 'o':
            print("ROSTER")
            for kl in sorted(new_dict):
                print(f"Jersey number: {kl}, Rating: {new_dict[kl]}")


new_dict = {}

for num in range(5):
    jnum = input(f"Enter player {num + 1}'s jersey number:\n")
    prate = input(f"Enter player {num + 1}'s rating:\n")

    if jnum not in new_dict:
        new_dict[int(jnum)] = int(prate)
    print()

print("ROSTER")

for k in sorted(new_dict):
    print(f"Jersey number: {k}, Rating: {new_dict[k]}")

print_menu()

