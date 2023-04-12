# Shijang Lin PSID: 2018904

# zyLab 12.7

from os import system

system('cls')


def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError('Invalid age.')
    return age


# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = .7 * (220 - age)
    return heart_rate


if __name__ == "__main__":
    try:
        age = get_age()
        heart = fat_burning_heart_rate(age)
        print(f'Fat burning heart rate for a {age} year-old: {heart} bpm')
    except ValueError as excpt:
        print(excpt)
        print("Could not calculate heart rate info.\n")
