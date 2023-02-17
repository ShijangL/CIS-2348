# Shijang Lin PSID: 2018904

# Lab 6.22

x1 = int(input())
y1 = int(input())
total1 = int(input())
x2 = int(input())
y2 = int(input())
total2 = int(input())
answer_founded = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if (x1 * x + y1 * y == total1) and (x2 * x + y2 * y == total2):
            answer_founded = True
            print(f'{x} {y}')
    if not answer_founded:
        print('No solution')
