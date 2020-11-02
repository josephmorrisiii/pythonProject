# Joseph Morris
#1840300


class FoodItem:
    def __init__(self, name='None', fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == '__main__':

    food_number_one = FoodItem()

    food_name = input()
    food_fat = float(input())
    food_carbs = float(input())
    food_protein = float(input())

    food_number_two = FoodItem(food_name, food_fat, food_carbs, food_protein)
    how_many_servings = float(input())
    food_number_one.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(how_many_servings,
                                                                    food_number_one.get_calories(how_many_servings)))
    print()
    food_number_two.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(how_many_servings,
                                                                    food_number_two.get_calories(how_many_servings)))


