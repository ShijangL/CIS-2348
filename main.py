# Shijang Lin PSID: 2018904

# Lab 5.22 Part 1
print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
print()

service_dict = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 0}

# Lab 5.22 Part 2
print('Select first service:')
first_service = input()
print('Select second service:')
second_service = input()
print()

# Lab 5.22 Part 3
print("Davy's auto shop invoice")
print()
if first_service == '-':
    print(f'Service 1: No service')
else:
    print(f'Service 1: {first_service}, ${service_dict[first_service]}')
if second_service == '-':
    print(f'Service 2: No service')
else:
    print(f'Service 2: {second_service}, ${service_dict[second_service]}')
print()
print(f'Total: ${service_dict[first_service] + service_dict[second_service]}')
