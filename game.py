import random


# Game world - rooms and their properties
rooms = {
    'forest': {
        'description': 'You are in a dark, mysterious forest. Tall trees surround you.',
        'exits': {'north': 'cave', 'east': 'village', 'south': 'lake'},
        'items': ['stick', 'berries']
    },
    'cave': {
        'description': 'A damp cave with glowing crystals on the walls. You hear water dripping.',
        'exits': {'south': 'forest', 'east': 'mountain'},
        'items': ['torch', 'gold_coin']
    },
    'village': {
        'description': 'A small, peaceful village with cozy houses and friendly people.',
        'exits': {'west': 'forest', 'north': 'mountain'},
        'items': ['bread', 'map']
    },
    'mountain': {
        'description': 'You stand atop a high mountain. The view is breathtaking!',
        'exits': {'west': 'cave', 'south': 'village'},
        'items': ['treasure_chest']
    },
    'lake': {
        'description': 'A serene lake with crystal-clear water. Fish swim peacefully below.',
        'exits': {'north': 'forest'},
        'items': ['fishing_rod', 'fish']
    }
}


def display_location(player_location):
    """Show current location info"""
    current_room = rooms[player_location]
    print("\n" + "="*50)
    print(f"LOCATION: {player_location.upper()}")
    print("="*50)
    print(current_room['description'])
   
    # Show available exits
    exits = list(current_room['exits'].keys())
    print(f"\nExits: {', '.join(exits)}")
   
    # Show items in room
    if current_room['items']:
        print(f"You can see: {', '.join(current_room['items'])}")
   
# Morning task
def move_player(direction, game_state):
    current_location = game_state[0]
    current_location_props = rooms[current_location]
    
    # print(dict(current_location_props["exits"].items()))
    
    if direction in current_location_props["exits"]:
        # game_state[0] = rooms[current_location]
        # print(current_location_props["exits"].items())
        # print(current_location_props["exits"][direction])
        game_state[0] = current_location_props["exits"][direction]
        game_state[1]-=10
        game_state[2]+=10
        random_event(game_state)
    else:
        print("Cannot go the that direction !")
   
    pass


# Morning task
def take_item(item_name, game_state):
    # game_state = [player_location, player_health, player_score, player_inventory, game_quit]
    
    if item_name in rooms[game_state[0]]["items"]:
        game_state[3].append(rooms[game_state[0]]["items"][rooms[game_state[0]]["items"].index(item_name)])
        rooms[game_state[0]]["items"].remove(rooms[game_state[0]]["items"][rooms[game_state[0]]["items"].index(item_name)])
        game_state[2]+=15
        random_event(game_state)
        # print(game_state[3])
    else:
        print("Item not found !")

    pass


# Morning task
def check_win_condition(game_state):
    if len(rooms["mountain"]["items"]) == 0:
        return True
    pass


def display_stats(game_state):
    print("Player Status\n" + "------------------------")
    print("Health :", game_state[1])
    print("Score :", game_state[2])
    show_inventory(game_state)
    pass


def show_inventory(game_state):
    print("You currently have...")
    print("------------------------\n")
    if len(game_state[3]) == 0:
        print("No Items")
    else:
        for i in range(len(game_state[3])):
            print("*", game_state[3][i])
    print("\n------------------------")
    pass


def random_event(game_state):
    events = [["Sunglasses", "Umbrella", "Car", "10Kg Bomb", "Notebook", "Apple", "Banana", "Trash", "Snake", "Sand", "Mask", "Drug", "Flower", "Gun", "Medicine"],
              [5, 10, 20, 30, 35, 40, 45, 50], 
              [-5, -10, -15]]
    random_case = random.randrange(0, 3)
    
    if random_case == 0:
        random1 = random.choice(events[0])
        game_state[3].append(random1)
        print("You got", random1)
    elif random_case == 1:
        random2 = random.choice(events[1])
        game_state[1] = game_state[1] + random2
        print("Your health got increased by", random2)
    elif random_case == 2:
        random3 = random.choice(events[2])
        game_state[1] = game_state[1] - random3
        print("Your health got decreased by", random3)
    pass


def use_item(item_name, game_state):
    if item_name in game_state[3]:
        print("Use", item_name)
        game_state[3].remove(item_name)
    else:
        print("Item not found !")
    pass


def check_lose_condition(game_state):
    if game_state[1] == 0:
        return True
    pass


def show_help():
    """Display available commands"""
    print("\n=== AVAILABLE COMMANDS ===")
    print("go <direction>     - Move in a direction (north, south, east, west)")
    print("take <item>        - Pick up an item")
    print("use <item>         - Use an item from your inventory")
    print("inventory          - Show your items")
    print("look               - Look around current location")
    print("stats              - Check your stats")
    print("help               - Show this help message")
    print("quit               - Exit the game")


def process_command(command, game_state):
    # game_state = [player_location, player_health, player_score, player_inventory, game_quit]
    parts = command.lower().split()
    if not parts:
        return
   
    action = parts[0]
   
    if action == 'go' and len(parts) > 1:
        move_player(parts[1], game_state)
    elif action == 'take' and len(parts) > 1:
        take_item(parts[1], game_state)
    elif action == 'use' and len(parts) > 1:
        use_item(parts[1], game_state)
    elif action == 'inventory':
        show_inventory(game_state)
    elif action == 'look':
        display_location(game_state[0])
    elif action == 'stats':
        display_stats(game_state)
    elif action == 'help':
        show_help()
    elif action == 'quit':
        print("\nThanks for playing!")
        game_state[4] = True
    else:
        print("\nI don't understand that command. Type 'help' for available commands.")


def main():
   
    # Player state
    
    player_location = 'forest'
    player_inventory = []
    player_health = 100
    player_score = 0
    game_win = False
    game_lose = False
    game_quit = False
    current_game_state = [player_location, player_health, player_score, player_inventory, game_quit]
   
    print("="*60)
    print("         WELCOME TO THE ADVENTURE GAME!")
    print("="*60)
    print("\nYour goal is to explore the world and find the treasure!")
    print("Type 'help' at any time to see available commands.")
   
    display_location(player_location)
   
    while not (game_win or game_lose):
        command = input("\n> What do you want to do? ")
        process_command(command, current_game_state)
       
        # Check win conditions
        game_win = check_win_condition(current_game_state)
        game_lose = check_lose_condition(current_game_state)
       
        game_quit = current_game_state[4]
        if game_quit:
            break
   
    # Game end messages
    print("\n" + "="*50)
    if game_win:
        print("🎉 CONGRATULATIONS! YOU WON! 🎉")
        print("You found the treasure and completed your adventure!")
    elif game_lose:
        print("💀 GAME OVER 💀")
        print("Your health reached zero. Better luck next time!")
   
    print(f"\nFinal Score: " + str(current_game_state[2]))
    print(f"Items Collected: {len(player_inventory)}")
    print("="*50)


# Run the game
if __name__ == "__main__":
    main()
