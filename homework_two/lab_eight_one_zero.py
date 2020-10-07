#Joseph Morris
#1840300

def is_string_a_palindrome(user_string):
    new_string = user_string.replace(" ", "")
    if new_string == new_string[::-1]:
        print(user_string, "is a palindrome")
    else:
        print(user_string, "is not a palindrome")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    user_string = str(input())

is_string_a_palindrome(user_string)