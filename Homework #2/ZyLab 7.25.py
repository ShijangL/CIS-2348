# Shijang Lin PSID: 2018904

# Lab 7.25

def exact_change(user_total):
    dollars = user_total // 100
    remainder = user_total % 100
    quarter = remainder // 25
    remainder = user_total % 25
    dime = remainder // 10
    remainder = remainder % 10
    nickel = remainder // 5
    penny = remainder % 5

    return dollars, quarter, dime, nickel, penny
