#Joseph Morris
#1840300

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
 #first set of numbers
    x_one = int(input())
    y_one = int(input())
    num_one = int(input())

 #second set of numbers
    x_two = int(input())
    y_two = int(input())
    num_two = int(input())

    solution_found = False

    for x in range(-10, 11):
        for y in range(-10, 11):
            if x_one * x + y_one * y == num_one and x_two * x + y_two * y == num_two:
                print(x, y)
                solution_found = True

    if not solution_found:
        print("No solution")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
