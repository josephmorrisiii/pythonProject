#Joseph Morris
#1840300


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def password_modifier(user_entered_password):
    print("step")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    password = {"i": "!", "a": "@", "m": "M", "B": "8", "o": "."}

    user_string = str(input())

    for key, value in password.items():
        user_string = user_string.replace(key, value)

print(user_string + "q*s")
