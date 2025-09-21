import random
import time


def display_board(current_board):
    for rows in current_board:
        print(''.join(rows))


def get_choice():
    global computer
    choice = input("Do you want to be X or O: ").upper()
    while choice not in computer:
        print("Must enter 'X' or 'O'.")
        choice = input("Do you want to be X or O: ").upper()
    computer.remove(choice)
    return choice


def get_starter():
    return random.randint(0,1)


def get_square(user):
    global squares, player_squares, computer_squares
    if user == 'You':
        next_square = input('Enter the square you want to play (1-9): ')
        while not next_square.isdigit() or int(next_square) not in range(1, 10) or int(next_square) not in squares:
            print("Must enter a square not taken and on the board (1 to 9).")
            next_square = input('Enter the square you want to play (1-9): ')
        player_squares.append(int(next_square))
    else:
        next_square = random.choice(squares)
        computer_squares.append(next_square)
    squares.remove(int(next_square))
    return int(next_square)


def place_square():
    global board
    number = 0
    for row in range(0, len(board), 2):
        for char in range(0, len(board[row]), 2):
            number += 1
            if number == square:
                if users[starter] == 'You':
                    board[row][char] = f' {player} '
                else: 
                    board[row][char] = f' {computer[0]} '


def check_winner(winners):
    win = False
    for winner in winners:
        play, comp = 0, 0
        for num in winner:
            if num in player_squares:
                play += 1
            elif num in computer_squares:
                comp += 1
        if play == 3:
            win = 'Player'
            break
        elif comp == 3:
            win = 'Computer'
            break
    return win


def display_winner():
    scores = open("tic tac toe scores.txt", 'r')
    scores_list = eval(scores.read())
    print()
    if not winner:
        print("Draw")
        scores_list[1] += 1
    else:
        print(f"{winner} wins!")
        if winner == 'Player':
            scores_list[0] += 1
        else:
            scores_list[2] += 1
    scores = open("tic tac toe scores.txt", 'w')
    scores.write(str(scores_list))



def update_scores():
    scores = open("tic tac toe scores.txt", 'r')
    scores_list = eval(scores.read())
    print(f"""Scores:
Player: {scores_list[0]}
Draws: {scores_list[1]}
Computer: {scores_list[2]}""")


#====================================================================

example_board = [[' 1 ', ' | ', ' 2 ', ' | ', ' 3 '], ['---', '---', '---', '---', '---'], [' 4 ', ' | ', ' 5 ', ' | ', ' 6 '], ['---', '---', '---', '---', '---'], [' 7 ', ' | ', ' 8 ', ' | ', ' 9 ']]
board = [['   ', ' | ', '   ', ' | ', '   '], ['---', '---', '---', '---', '---'], ['   ', ' | ', '   ', ' | ', '   '], ['---', '---', '---', '---', '---'], ['   ', ' | ', '   ', ' | ', '   ']]
computer, users = ['X', 'O'], ['You', 'Computer']
squares, player_squares, computer_squares = [1,2,3,4,5,6,7,8,9], [], []
attempts, winner = 0, False
winning_combinations = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]


print("Squares on the board are as shown: ")
print()
display_board(example_board)
print()
player = get_choice()
starter = get_starter()
print(f'{users[starter]} start.')
while not winner and attempts != 9:
    print(f"{users[starter]} go.")
    print()
    attempts += 1
    square = get_square(users[starter])
    place_square()
    if starter == 0:
        starter = 1
    else:
        starter = 0
    print()
    display_board(board)
    print()
    time.sleep(1)
    winner = check_winner(winning_combinations)

display_winner()
update_scores()