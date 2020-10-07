#Joseph Morris
#1840300

import csv
if __name__ == '__main__':

    users_file_name = input()

    word_count = {}

    # reading the file
    with open(users_file_name, 'r') as csvfile:
        reading_the_file = csv.reader(csvfile)
    # iterating throught each row
        for row in reading_the_file:
            for word in row:

              if word not in word_count.keys():
                word_count[word] = 1
    # else increase the frequency by 1
              else:
                word_count[word] += 1

    for key in word_count.keys():
        print(key + " " + str(word_count[key]))