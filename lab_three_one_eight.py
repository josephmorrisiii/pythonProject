#Student name - Joseph Morris
#Student ID - 1840300

import math
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Part1
    wall_height = int(input("Enter wall height (feet):\n"))
    wall_width = int(input("Enter wall width (feet):\n"))
    wall_area = wall_width * wall_height
    print('Wall area: ', wall_area, ' square feet')

    #Part2
    wall_area = wall_area / 350
    wall_area = '{:.2f}'.format(wall_area)
    wall_area = float(wall_area)
    print('Paint needed: ', wall_area, ' gallon(s)')

    #Part3
    wall_area = math.ceil(wall_area)
    print('Cans needed: ', wall_area, ' can(s)\n')

    #Part4
    print('Choose a color to paint the wall:')
    print('Options are: Red, Blue, and Green')
    print("Please type exactly as the options are displayed")

    user_input = input()
    if user_input == 'Red':
        print("Cost of purchasing Red paint: $ 35")

    if user_input == "Blue":
        print("Cost of purchasing Blue paint: $ 25")

    if user_input == "Green":
        print("Cost of purchasing Green paint: $ 23")