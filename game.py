class Weapon:
    def __str__(self):
        return self.name


class Screwdriver(Weapon):
    def _init_(self):
        self.name = "Screwdriver"
        self.description = "A cross type screwdriver"
        self.damage = 5


class BrokenBottle(Weapon):
    def _init_(self):
        self.name = "Broken Bottle"
        self.description = "A piece of bottle with pointy edges"
        self.damage = 7


class Photo(Weapon):
    def _init_(self):
        self.name = "Photo"
        self.description = "A polaroid of me and other people I don't know"
        self.damage = 0


def play():
<<<<<<< HEAD
    inventory = ['screwdriver', 'photo', 'broken bottle']
    print("Escape from Room 237")
    while True:
        action_input = get_player_command()
        if action_input == 'n' or action_input == 'N':
            print("Go North!")
        elif action_input == 's' or action_input == 'S':
            print("Go South!")
        elif action_input == 'e' or action_input == 'E':
            print("Go East!")
        elif action_input == 'w' or action_input == 'W':
            print("Go West!")
        elif action_input == ['i', 'I']:
            print("Inventory:")
        for item in inventory:
            print('*' + str(item))
        else:
            print("Invalid action!")

=======
    inventory = ['screwdriver', 'brokenbottle']
    print("Escape from Room 237")
    action_input = get_player_command()
    if action_input in ['n', 'N']:
        print("Go North!")
    elif action_input in ['s', 'S']:
        print("Go South!")
    elif action_input in ['e', 'E']:
        print("Go East!")
    elif action_input in ['w', 'W']:
        print("Go West!")
    elif action_input in ['i', 'I']:
        print("Inventory:")
        print(inventory)
    else:
        print("Invalid action!")
    
>>>>>>> 115e41dd931994a36e3c6e4c6aaeafee9cab0732

def get_player_command():
    return input('Action: ')


play()
