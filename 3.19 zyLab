import math

# Part 1 of Lab 3.19

print('Enter wall height (feet):')
wall_height = int(input())
print('Enter wall width (feet):')
wall_width = int(input())
wall_area = wall_height * wall_width
print(f'Wall area: {wall_area} square feet')

# Part 2 of Lab 3.19

sq_ft_per_gallon = 350
gallon_needed = wall_area / 350
print(f'Paint needed: {gallon_needed:.2f} gallons')

# Part 3 of Lab 3.19

cans_needed = math.ceil(gallon_needed)
print(f'Cans needed: {cans_needed} can(s)')
print()

# Part 4 of Lab 3.19

color = {'red': 35, 'blue': 25, 'green': 23}
print('Choose a color to paint the wall:')
color_chosen = input()
print(f'Cost of purchasing {color_chosen} paint: ${color[color_chosen] * cans_needed}')
