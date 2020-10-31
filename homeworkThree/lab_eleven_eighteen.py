#Joseph Morris
#1840300

if __name__ == '__main__':

    numbers_split = input().split()
    result = []

    for numbers in numbers_split:
        numbers = int(numbers)
        if numbers >= 0:
            result.append(numbers)

    result.sort()
    for numbers in result:
        print(numbers, end=' ')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
