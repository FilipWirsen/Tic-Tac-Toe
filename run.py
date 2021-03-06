from random import randrange

BOARD = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def print_board():
    """
    Prints the board
    """
    global BOARD
    print(BOARD[0] + "|" + BOARD[1] + "|" + BOARD[2])
    print(BOARD[3] + "|" + BOARD[4] + "|" + BOARD[5])
    print(BOARD[6] + "|" + BOARD[7] + "|" + BOARD[8] + "\n")
    return


def get_random_position():
    """
    Make computer choose random number between 0-9
    """
    global BOARD
    while True:
        random_index = randrange(9)
        if BOARD[random_index] == '-':
            return random_index


def player_input(player_name):
    """
    Take player input and add their symbol to the board
    """
    global BOARD
    while True:
        try:
            inp = int(input(f"{player_name} please chose a number"
                      " between 1-9 to place your symbol: \n"))
            if inp >= 1 and inp <= 9 and BOARD[inp-1] == "-":
                BOARD[inp-1] = 'X'
                print_board()
                did_win_or_tie = check_for_win_or_tie(player_name)
                if did_win_or_tie:
                    return ask_to_play_again()
                else:
                    play_computer_chance(player_name)
                break
            else:
                print(f"Slot number:{inp} is already taken, try again. \n")
        except ValueError as e:
            print(f"You need to enter a number, {e} is not a number \n")
    return


def did_win_horizontally(player):
    """
    Check for win horizontally
    """
    global BOARD
    did_win = False
    if ((BOARD[0] != "-" and BOARD[0] == BOARD[1] == BOARD[2]) or
            (BOARD[3] != "-" and BOARD[3] == BOARD[4] == BOARD[5]) or
            (BOARD[6] != "-" and BOARD[6] == BOARD[7] == BOARD[8])):
        print(f"Congratz {player}, You won the game! \n")
        did_win = True
    return did_win


def did_win_vertically(player):
    """
    Check fo win vertically
    """
    global BOARD
    did_win = False
    if ((BOARD[0] != "-" and BOARD[0] == BOARD[3] == BOARD[6]) or
        (BOARD[1] != "-" and BOARD[1] == BOARD[4] == BOARD[7]) or
            (BOARD[2] != "-" and BOARD[2] == BOARD[5] == BOARD[8])):
        print(f"Congratz {player}, You won the game! \n")
        did_win = True
    return did_win


def did_win_diagonally(player):
    """
    Check for win diagonally
    """
    global BOARD
    did_win = False
    if ((BOARD[0] != "-" and BOARD[0] == BOARD[4] == BOARD[8]) or
            (BOARD[2] != "-" and BOARD[2] == BOARD[4] == BOARD[6])):
        print(f"Congratz {player}, You won the game! \n ")
        did_win = True
    return did_win


def check_tie():
    """
    Checks if game is tied
    """
    global BOARD
    is_tie = False
    if "-" not in BOARD:
        print("It is a tie!\n")
        is_tie = True
    return is_tie


def check_for_win_or_tie(player):
    """
    Runs functions to check if a player has won or tied the game
    """
    if (did_win_horizontally(player) or
            did_win_vertically(player) or
            did_win_diagonally(player) or
            check_tie()):
        return True
    return False


def play_computer_chance(player_name):
    """
    The computer places their symbol
    """
    global BOARD
    random_position = get_random_position()

    BOARD[random_position] = 'O'
    print("The computer has placed their symbol\n")
    print_board()
    did_win_or_tie = check_for_win_or_tie('Computer')
    if did_win_or_tie:
        return ask_to_play_again()
    else:
        reference_board()
        print_board()
        player_input(player_name)

    return


def ask_to_play_again():
    """
    Ask user if they want to play again,
    if Yes, then call start_game() or else exit
    """
    print("Would you like to play again?")
    answer = input("Y/N: \n").lower()
    if answer == "y":
        return start_game()
    elif answer == "n":
        print("Thanks for playing, hope to see you soon again!")
    else:
        print("Please enter Y or N \n")
        ask_to_play_again()


def start_game():
    """
    Starts the game!
    """
    global BOARD
    player_name = input("Please enter your name to start the game: \n")
    BOARD = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    player_input(player_name)


def welcome_msg():
    """
    Prints welcome message
    """
    print(" ??????????????????   ??????????????????     ??????????????????")
    print(" ??????????????????   ??????????????????     ??????????????????")
    print(" ?????????????????????????????????????????????????????????????????????????????????????????????")
    print("   ???????????????????????????????????????????????????????????????????????????????????????")
    print("   ???????????????????????????????????????????????????????????????????????????????????????")
    print("   ?????????????????????  ???????????????????????????  ??????????????????????????? \n")


def display_rules():
    """
    Prints the game rules
    """
    print("This game is played on a grid that's 3 squares by 3 squares.\n")
    print("You are X and the computers symbol is O. You and the computer"
          " will take turns putting your symbol in empty squares.\n")
    print("The first player to get 3 of their symbol in a row"
          " (up, down, across or diagonally) is the winner.\n")
    print("If all 9 squares are full, the game is tied.\n")
    print("This is how the board looks and"
          " what number correlates with wich square.\n")


def reference_board():
    """
    Prints reference board
    """
    print("Reference board: \n")
    print("|1|2|3|")
    print("|4|5|6|")
    print("|7|8|9| \n")


def main():
    """
    Main function that shows welcome message, game instructions and
    calls the start_game function
    """
    welcome_msg()
    display_rules()
    reference_board()
    start_game()


main()
