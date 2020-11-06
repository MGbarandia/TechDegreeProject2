import constants
import copy
import random
Name = input("What is your name?  ")
def welcome():
    try:
        enter = input("Would you like to enter? (Yes/No only)  ".format(Name))
        while enter.isnumeric():
            enter = input("Please enter (Yes/No only), {}!  ".format(Name))
    except (ValueError, TypeError):
        print("Please enter (Yes or No only) not {}.".format(play))
    else:
        while enter.lower() != "yes":
            try:
                if enter.lower() == "no":
                    print("Maybe you can play next time! Goodbye, {}!!".format(Name))
                    quit()
                enter = input("Please enter (Yes/No only), {}!  ".format(Name))
            except (ValueError, TypeError):
                print("Please enter (Yes or No only) not {}.".format(play))
            else:
                if enter == "no":
                    print("Maybe you can play next time! Goodbye, {}!!".format(Name))
                    quit()

PlayersList = []
Panthers = []
Bandits = []
Warriors = []

def Balance(team):
    ExpCount = 0
    NoExpCount = 0

    while len(team) != 6:
        choice = random.choice(range(len(PlayersList)))
        if PlayersList[choice]['experience'] == False and NoExpCount <= 2:
            NoExpCount+=1
            team.append(PlayersList.pop(choice))
        elif PlayersList[choice]['experience'] == True and ExpCount <= 2:
            ExpCount+=1
            team.append(PlayersList.pop(choice))


def flat(MyList):
    NewList = []

    for item in MyList:
        if type(item) == str:
            NewList.append(item)
        elif type(item) == list:
            for item2 in item:
                MyList.append(item2)
    return NewList

def Value(MyList, Target):
    temp = []

    for item in MyList:
        temp.append(item[Target])
    return temp

def Calculated(team):
    Total = 0
    NoExp = 0
    Exp = 0

    for player in team:
        Total+=player['height']
        if player['experience'] == True:
            Exp+=1
        elif player['experience'] == False:
            NoExp+=1

    return NoExp, Exp, Total

def HeightAverage(HeightTotal, TotalPlayers):
    Average = HeightTotal / TotalPlayers
    return Average

def CleanStat():
    for player in PlayersList:
        if player['experience'].lower() == 'yes':
            player['experience'] = True
        elif player['experience'].lower() == 'no':
            player['experience'] = False

        height = player['height'].split(' ')
        player['height'] = int(height[0])

        if ' and ' in player['guardians']:
            player['guardians'] = player['guardians'].split(' and ')

def Results(SelectedTeam, Team):
    Guardians1 = flat(Value(SelectedTeam, 'guardians'))
    Names = Value(SelectedTeam, 'name')
    NumInExp, NumOfExp, HeightTotal = Calculated(SelectedTeam)

    print("""------------------------------------------------------------------------------------------
    \n|Team {}|\n""" .format(Team))
    print("\n.Total players: {} players\n".format(len(SelectedTeam)))
    print(".Players: {}\n".format(", ".join(Names)))
    print(".Guardians: {}   \n".format(", ".join(Guardians1)))
    print(".Number of inexperienced players: {}\n".format(NumInExp))
    print(".Number of experienced players: {}\n".format(NumOfExp))
    print(".Average height of the team: {:.2f}\n".format(HeightAverage(HeightTotal, NumOfExp +NumInExp)))
    print("--------------------------------------------------------------------------------------------\n\n\n")


def menu():
    print("""
++++++++++++++++++++++++++++++++++++++++++
--------BASKETBALL TEAM STATS TOOL--------
+++++++++++++++++++++++++++++++++++++++++++
""")

    while True:
        print("""---MAIN MENU---

Here are your choices:
  1) Display Team Stats
  2) Quit
""")
        try:
            user_option = int(input("Enter an option   \n---->"))
            print(("-")*20)
        except ValueError:
            print("\nError {} .Please Try again.\n".format(Name))
            print(("-")*30)
        else:
            if user_option > 2:
                print("\n{}, Only type one of the options listed. Try again.\n".format(Name))
                print(("-")*30)
            elif user_option == 2:
                print("""
    +++++++++++++++++++++++++++++++++++++++++++
    --------See you next time {}!--------
    +++++++++++++++++++++++++++++++++++++++++++""".format(Name))
                quit()
            elif user_option < 1:
                print("\n{}, Only type one of the options listed. Try again.\n".format(Name))
                print(("-")*30)
            elif user_option == 1:
                print("1. Panther\n")
                print("2. Bandits\n")
                print("3. Warriors\n")
                print("4. Quit program\n")
                try:
                    option = int(input("Please Choose one {}:   \n".format(Name)))
                except ValueError:
                    print("""Value Error: {} You Have Made an Error!!!!
                    \nChoose only the numbers at the top.
                    \nThe program will now go back to Main Menu.\n\n""".format(Name))
                    print(("-")*30)
                else:
                    if option == 1:
                        Results(Panthers, "Panther")
                        continue
                    elif option == 2:
                        Results(Bandits, "Bandits")
                        continue
                    elif option == 3:
                        Results(Warriors, "Warriors")
                        continue
                    elif option ==4:
                        print("""++++++++++++++++++++++++++++++++++++++++++
    --------See you next time {}!--------
    +++++++++++++++++++++++++++++++++++++++++++""".format(Name))
                    quit()




if __name__ == '__main__':
    PlayersList = copy.deepcopy(constants.PLAYERS)
    TeamList = copy.deepcopy(constants.TEAMS)

    welcome()
    CleanStat()
    Balance(Panthers)
    Balance(Bandits)
    Balance(Warriors)
    menu()
