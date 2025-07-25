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
    # game_state = [player_location, player_health, player_score, player_inventory, game_quit]
   
    # To be implemented
    pass


# Morning task
def take_item(item_name, game_state):
    # game_state = [player_location, player_health, player_score, player_inventory, game_quit]


    # To be implemented
    pass


# Morning task
def check_win_condition(game_state):
    # Check if player has collected the treasure
    # To be implemented
    pass


def display_stats(game_state):
    # To be implemented
    pass


def show_inventory(game_state):
    # To be implemented
    pass


def random_event(game_state):
    # To be implemented
    pass


def use_item(item_name, game_state):
    # To be implemented
    pass


def check_lose_condition(game_state):
    # To be implemented
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
        print("To be implemented")
    elif action == 'inventory':
        print("To be implemented")
    elif action == 'look':
        display_location(game_state[0])
    elif action == 'stats':
        print("To be implemented")
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
   
    print(f"\nFinal Score: {player_score}")
    print(f"Items Collected: {len(player_inventory)}")
    print("="*50)


# Run the game
if __name__ == "__main__":
    main()