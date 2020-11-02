#Joseph Morris
#1840300

if __name__ == '__main__':

    result_of_non_negative_integers = []
    list_of_numbers = input().split()

    for user_numbers in list_of_numbers:
        user_numbers = int(user_numbers)
        if user_numbers >= 0:
            result_of_non_negative_integers.append(user_numbers)

    result_of_non_negative_integers.sort()

    for user_numbers in result_of_non_negative_integers:
        print(user_numbers, end=' ')
