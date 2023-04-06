import json
# import data base file
import open_file as db_player
#global dict what cash a player data
player_map_icon = {}
# This is Start menu, first what see player in game
def start_menu():
    db_player.create_file()
    print("Welcome to your RPG game!\n")
    print("1. New Game")
    print("2. Load Game")
    print("3. Quit\n")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        new_game()
    elif choice == "2":
        load_game()
    elif choice == "3":
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid choice, please try again.\n")
        start_menu()
# this function take a data from db and convert for game function
def load_player():
    global player_map_icon
    with open(db_player.filename, 'r') as data:
        player_map_icon = json.load(data)
    player_name = player_map_icon['items'][0]['player_name']
    role = player_map_icon['items'][0]['role']
    health_point = player_map_icon['items'][0]['health_point']
    mana_point = player_map_icon['items'][0]['mana_point']
    player_str = player_map_icon['items'][0]['player_str']
    player_int = player_map_icon['items'][0]['player_int']
    player_icon = player_map_icon['items'][0]['player_icon']
    position_x = player_map_icon['items'][0]['position_x']
    position_y = player_map_icon['items'][0]['position_y']
    #player_dict = {"player_name": player_name, "role": role, "health_point": health_point, "mana_point": mana_point,
     #"player_str": player_str, "player_int": player_int, "player_icon": player_icon, "position_x": position_x, "position_y": position_y}
# function control game, maps, movement etc.
def load_game():
    load_player()
    move()
# function create new player and save data in DB
def new_game():
    db_player.read_file()
    print("Starting a new game...\n")
    role = choose_role()
    player_name = input("Enter your name: ")
    health_point = 50
    mana_point = 20
    player_str = 10
    player_int = 10
    player_icon = "P"
    position_x = 6
    position_y = 6
    player_dict = {"player_name": player_name, "role": role, "health_point": health_point, "mana_point": mana_point,
     "player_str": player_str, "player_int": player_int, "player_icon": player_icon, "position_x": position_x, "position_y": position_y}
    db_player.append_to_file(player_dict)
    print(f"Hi {player_name}, you are awesome!!")
    load_game()
# function for creating new character in the game
def choose_role():
    print("Choose your role:\n")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue\n")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        return "Warrior"
    elif choice == "2":
        return "Mage"
    elif choice == "3":
        return "Rogue"
    else:
        print("Invalid choice, please try again.\n")
        return choose_role()
# map generator
def map():
    for x in range(11):
        line = ''
        num_x = x + 1
        for y in range(11):
            num_y = y + 1
            if player_map_icon['items'][0]['position_x'] == num_x and player_map_icon['items'][0]['position_y'] == num_y:
                line += " " + player_map_icon['items'][0]['player_icon'] + " "
            else:
                line += " " + '0' + " "
        print(line)
# control movement function, work with map and save every step in DB
def move():
    while True:
        try:
            map()
            choise = input("Nord - Up, South - Down, West - Left, East - Rigth: ").lower()
            if choise == 'n':
                if player_map_icon['items'][0]['position_x'] == 1:
                    print("You can`t go this way!")
                else:
                    player_map_icon['items'][0]['position_x'] -= 1
            elif choise == 's':
                if player_map_icon['items'][0]['position_x'] == 11:
                    print("You can`t go this way!")
                else:
                    player_map_icon['items'][0]['position_x'] += 1
            elif choise == 'w':
                if player_map_icon['items'][0]['position_y'] == 1:
                    print("You can`t go this way!")
                else:
                    player_map_icon['items'][0]['position_y'] -= 1
            elif choise == 'e':
                if player_map_icon['items'][0]['position_y'] == 11:
                    print("You can`t go this way!")
                else:
                    player_map_icon['items'][0]['position_y'] += 1
            else:
                print('Invalid input!!')
        except:
            pass
        finally:
            db_player.save_file(player_map_icon)
# function, what start a game
if __name__ == '__main__':
    start_menu()