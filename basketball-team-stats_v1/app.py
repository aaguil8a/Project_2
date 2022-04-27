import constants
import copy
import sys


teams_data = copy.deepcopy(constants.TEAMS)
players_data = copy.deepcopy(constants.PLAYERS)
panters = []
bandits = []
warriors = []


def enter():
    name = input('PRESS ENTER to continue')
    if not name:
        menu()
    
    else:
        print('Have a nice day!')


def menu():
    
    print('BASKETBALL TEAM STATS TOOL')
    print('\n ---- MENU----') 
    print('\n   Here are your choices:')
    print('\n   A) Display Team Stats')
    print('\n   B) Quit')

    while True:
        print(' ')
        option = str(input('Enter an option: '))
        if option.upper() == 'B':
            sys.exit('See you next time!')
            

        elif option.upper() == 'A':
            print("""
            A) Panthers
            B) Bandits
            C) Warriors
            """)
           
            option1 = str(input('Enter an option: '))
            
            if option1.upper() == 'A':
                  print('')
                  print('Team: Panthers Stats')
                  print('---------------------')
                  print(f'Total players: {len(panters)}')
                  print()
                  print('Players on team:')
                  print(', '.join(panters))
                  print()
                  enter()
                  break

            elif option1.upper() == 'B':
                print(' ')
                print('Team: Bandits Stats')
                print('---------------------')
                print(f'Total players: {len(panters)}')
                print()
                print('Players on team:')
                print(', '.join(bandits))
                print()
                enter()
                break

            elif option1.upper() == 'C':
                print(' ')
                print('Team: Warriors Stats')
                print('---------------------')
                print(f'Total players: {len(panters)}')
                print()
                print('Players on team:')
                print(', '.join(warriors))
                print()
                enter()
                break

            else:
                print('Not a valid input!')
                break
    
        else:
            print('Not a valid input!')
            break


def clean_data(data):

    clean = []
    for player in data:

        fixed = {}
        fixed['name'] = player['name']
        fixed['guardians'] = player['guardians']
        if player['experience'] == 'YES':
            fixed['experience'] = True
        else:
            fixed['experience'] = False

        fixed['height'] = int(player['height'].split()[0])
        clean.append(fixed)

    return clean


def balance_teams():
    og_list = len(players_data) // 3
    for _ in range(og_list):
        panters.append(players_data.pop()['name'])
        bandits.append(players_data.pop()['name'])
        warriors.append(players_data.pop()['name'])


def main():
    clean_data(players_data)
    balance_teams()
    menu()


if __name__ == "__main__":
    main()
