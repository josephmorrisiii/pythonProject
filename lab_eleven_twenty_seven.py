#Joseph Morris
#1840300

if __name__ == '__main__':

    player_dict = {}
    sorted_list_keys = []

    def sortDictKeys():
        sorted_list_keys = sorted(player_dict.keys())
        return sorted_list_keys

    def outputRoster():
        sorted_list_keys = sortDictKeys()

        print("ROSTER")

        # Traverse the list of keys.

        for i in sorted_list_keys:
            print("Jersey number: " + str(i)
                  + ", Rating: " + str(player_dict[i]))

    def addPlayer():
        print("Enter a new player's jersey number:")
        jersey_num = int(input())

        while ((jersey_num < 0) or (jersey_num > 99)):
            print("Invalid Jersey Number! Please " +

                  "enter again!")

            print("Enter a new player's jersey number:")
            jersey_num = int(input())
        print("Enter the player's rating:")
        player_rating = int(input())

        while ((player_rating < 1) or (player_rating > 9)):
            print("Invalid Rating! Please enter again!")
            print("Enter the player's rating:")
            player_rating = int(input())

        player_dict.update({jersey_num: player_rating})

    def removePlayer():
        print("Enter a jersey number:")
        jersey_num = int(input())

        while ((jersey_num < 0) or (jersey_num > 99)):
            print("Invalid Jersey Number! Please " +
                  "enter again!")
            print("Enter a jersey number:")
            jersey_num = int(input())

        if jersey_num in player_dict.keys():
            del player_dict[jersey_num]


    def updatePlayer():
        print("Enter a jersey number:")
        jersey_num = int(input())
        while ((jersey_num < 0) or (jersey_num > 99)):
            print("Invalid Jersey Number! Please " +
                  "enter again!")
            print("Enter a jersey number:")
            jersey_num = int(input())

        # Prompt the user to enter a player's rating.

        print("Enter a new rating for player:")
        player_rating = int(input())
        while ((player_rating < 1) or (player_rating > 9)):
            print("Invalid Rating! Please enter again!")
            print("Enter a new rating for player:")
            player_rating = int(input())

        player_dict[jersey_num] = player_rating

    def outputPlayerAboveRating():
        print("Enter a rating:")
        rating = int(input())

        while ((player_rating < 1) or (player_rating > 9)):
            print("Invalid Rating! Please enter again!")
            print("Enter a rating:")
            rating = int(input())

        print("ABOVE 4")

        sorted_list_keys = sortDictKeys()

        for i in sorted_list_keys:
            if player_dict[i] > rating:
                print("Jersey number: " + str(i)
                      + ", Rating: " + str(player_dict[i]))

    for i in range(1, 6):
        print("Enter player " + str(i) + "'s jersey number:")
        jersey_num = int(input())

        while ((jersey_num < 0) or (jersey_num > 99)):
            print("Invalid Jersey Number! Please " +
                  "enter again!")
            print("Enter player " + str(i)
                  + "'s jersey number:")
            jersey_num = int(input())

        # Prompt the user to enter a player's rating.

        print("Enter player " + str(i) + "'s rating:")

        player_rating = int(input())



        while ((player_rating < 1) or (player_rating > 9)):
            print("Invalid Rating! Please enter again!")
            print("Enter player " + str(i) + "'s rating:")
            player_rating = int(input())

        print()

        player_dict[jersey_num] = player_rating

    outputRoster()

    print()

    while (True):
        print("MENU")

        print("a - Add player")

        print("d - Remove player")

        print("u - Update player rating")

        print("r - Output players above a rating")

        print("o - Output roster")

        print("q - Quit")

        print()

        print("Choose an option:")
        user_choice = input()
        if (user_choice == 'a'):
            addPlayer()
        elif (user_choice == 'd'):
            removePlayer()
        elif (user_choice == 'u'):
            updatePlayer()
        elif (user_choice == 'r'):
            outputPlayerAboveRating()
        elif (user_choice == 'o'):
            outputRoster()
        elif (user_choice == 'q'):
            break
        print()