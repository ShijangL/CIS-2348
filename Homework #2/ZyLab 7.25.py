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


if __name__ == "__main__":
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if input_val == 0:
        print('no change')
    if num_dollars > 1:
        print(f'{num_dollars} dollars')
    elif num_dollars > 0:
        print(f'{num_dollars} dollar')

    if num_quarters > 1:
        print(f'{num_quarters} quarters')
    elif num_quarters > 0:
        print(f'{num_quarters} quarter')

    if num_dimes > 1:
        print(f'{num_dimes} dimes')
    elif num_dimes > 0:
        print(f'{num_dimes} dime')

    if num_nickels > 1:
        print(f'{num_nickels} nickels')
    elif num_nickels > 0:
        print(f'{num_nickels} nickel')

    if num_pennies > 1:
        print(f'{num_pennies} pennies')
    elif num_pennies > 0:
        print(f'{num_pennies} penny')
