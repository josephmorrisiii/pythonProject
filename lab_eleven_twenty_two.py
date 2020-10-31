#Joseph Morris
#1840300

from collections import Counter

if __name__ == '__main__':
    sentence = str(input())
    for the_words in sentence.split():
        print(f"{the_words} {Counter(sentence.split())[the_words]}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
