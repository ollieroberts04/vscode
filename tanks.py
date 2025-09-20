import random
tank_locations = []
already_guessed = []


def place_tanks():
    global tank_locations
    while len(tank_locations) < 5:
        coordinate = f"{random.randint(0,7)},{random.randint(0,7)}"
        if coordinate not in tank_locations:
            tank_locations.append(coordinate)


def display_game_state():
    global already_guessed, tank_locations
    print('''   0  1  2  3  4  5  6  7''')
    for y in range(0,8):
        line = f"{y}  "
        for x in range(0,8):
            coordinate = f"{x},{y}"
            if coordinate in already_guessed:
                if coordinate in tank_locations:
                    line += "\033[91mX\033[0m  "
                else:
                    line += "X  "
            else:
                line += "   "
        print(line)


def player_guess():
    global already_guessed
    guess = input("Where do you want to guess 0-7 (x,y)?: ")
    while len(guess) != 3 or int(guess[0]) not in range(0,8) or guess[1] != ',' or int(guess[2]) not in range(0,8) or guess in already_guessed:
        if guess in already_guessed:
            print(f"You've already guessed {guess}. Try another one.")
        else:
            print("Guess must be entered in the format 'x,y' and coordinates cannot be larger than 7.")
        guess = input("Where do you want to guess (x,y)?: ")
    already_guessed.append(guess)
    return guess


def check_guess(guess):
    global tank_locations, tanks_found
    if guess in tank_locations:
        print(f"Well done you took down a tank at {guess}")
        tanks_found += 1
    else:
        print(f"Oh no there wasn't a tank at {guess}")
        

def display_tanks():
    global tank_locations, already_guessed
    print('''   0  1  2  3  4  5  6  7''')
    for y in range(0,8):
        line = f"{y}  "
        for x in range(0,8):
            coordinate = f"{x},{y}"
            if coordinate in tank_locations:
                if coordinate not in already_guessed:
                    line += "\033[91mX\033[0m  "
                else: 
                    line += "\033[92mX\033[0m  " 
            else:
                line += "   "
        print(line)

place_tanks()
attempt = 0
tanks_found = 0
display_game_state()
while attempt != 20 and tanks_found < 5:
    check_guess(player_guess())
    display_game_state()
    attempt += 1
print()
print()
if tanks_found == 5:
    print("Well done you took down all the tanks!")
else:
    print(f"Oh no! You lost, there are still {5 - tanks_found} left!")
print("Tanks:")
display_tanks()

