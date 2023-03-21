# Shijang Lin PSID: 2018904

# zyLab 10.11

class FoodItem:
    def __init__(self, name="None", fat=0, carbs=0, protein=0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":
    food_name = input()
    fats_grams = int(input())
    carbs_grams = int(input())
    protein_grams = int(input())
    servings = int(input())

    food1 = FoodItem()
    food1.print_info()
    print(f'Number of calories for {servings:.2f} serving(s): {food1.get_calories(servings):.2f}')
    print()

    food = FoodItem(food_name, fats_grams, carbs_grams, protein_grams)
    food.print_info()
    print(f'Number of calories for {servings:.2f} serving(s): {food.get_calories(servings):.2f}')
