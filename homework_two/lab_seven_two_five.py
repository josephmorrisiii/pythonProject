#Joseph Morris
#1840300

def exact_change(user_total):
    if user_total <= 0:
        print('no change')
    num_dollars = user_total // 100
    user_total %= 100
    num_quarters = user_total // 25
    user_total %= 25
    num_dimes = user_total // 10
    user_total %= 10
    num_nickels = user_total // 5
    user_total %= 5
    num_pennies = user_total
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__':

    inputval = int(input())
    numdollars, numquarters, numdimes, numnickels, numpennies = exact_change(inputval)


    if numdollars == 1:
        print(numdollars, "dollar")
    elif numdollars > 1:
        print(numdollars, "dollars")

    if numquarters == 1:
        print(numquarters, "quarter")
    elif numquarters > 1:
        print(numquarters, "quarters")

    if numdimes == 1:
        print(numdimes, "dime")
    elif numdimes > 1:
        print(numdimes, "dimes")

    if numnickels == 1:
        print(numnickels, "nickel")
    elif numnickels > 1:
        print(numnickels, "nickels")

    if numpennies == 1:
        print(numpennies, "penny")
    elif numpennies > 1:
        print(numpennies, "pennies")




