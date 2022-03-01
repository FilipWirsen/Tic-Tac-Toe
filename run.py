# Create board

REFERENCE_BOARD = ["1", "2", "3",
                    "4", "5", "6",
                    "7", "8", "9"]


BOARD = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

run_game = True
current_player = "X"

#print board
def print_board(board):
    """
    Prints the board 
    """
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8] +"\n")

#Player input 
def player_input(board, player):
    """
    Take player input and add their symbol to the board
    """
    while True:
        try:
            inp = int(input(f"{player} please chose a number between 1-9 to place your symbol: \n"))
            if inp >= 1 and inp <= 9 and board[inp-1] == "-":
                board[inp-1] = current_player
                print_board(BOARD)
                check_for_win_or_tie(board, player)
                switch_player()
                break
            else:
                print(f"Slot number:{inp} is already taken, try again. \n")
        except ValueError as e:
            print(f"You need to enter a number, {e} is not a number \n")


#Check for win or tie 
def win_horizontally(board, player):
    """
    Check for win horizontally
    """
    global run_game
    if board[0] == board[1] == board[2] and board[0] != "-":
        print(f"Congratz {player}, You won the game! \n")
        run_game = False
    elif board[3] == board[4] == board[5] and board[3] != "-":
        print(f"Congratz {player}, You won the game! \n")
        run_game = False
    elif board[6] == board[7] == board[8] and board[6] != "-":
        print(f"Congratz {player}, You won the game! \n")
        run_game = False
    
def win_vertically(board, player):
    """
    Check fo win vertically
    """
    global run_game
    if board[0] == board[3] == board[6] and board[0] != "-":
        print(f"Congratz {player}, You won the game! \n")
        run_game = False
    elif board[1] == board[4] == board[7] and board[1] != "-":
        print(f"Congratz {player}, You won the game! \n")
        run_game = False
    elif board[2] == board[5] == board[8] and board[2] != "-":
        print(f"Congratz {player}, You won the game! \n")
        run_game = False

def win_diagonally(board, player):
    """
    Check for win diagonally
    """
    global run_game
    if board[0] == board[4] == board[8] and board[0] != "-":
        print(f"Congratz {player}, You won the game! \n")
        run_game = False
    elif board[2] == board[4] == board[6] and board[2] != "-":
        print(f"Congratz {player}, You won the game! \n ")
        run_game = False

def check_tie(board):
    """
    Checks if game is tied
    """
    global run_game
    if "-" not in board:
        print("It is a tie!\n")
        run_game = False


def check_for_win_or_tie(board, player):
    """
    Runs functions to check if a player has won or tied the game
    """
    win_horizontally(board,player)
    win_vertically(board, player)
    win_diagonally(board, player)
    check_tie(BOARD)
            
#Switch player
def switch_player():
    """
    Switches  player 
    """
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    



def main():
    """
    Function that gets player names and runs the game
    """
    player_one = input("Player one, please enter your name: \n")
    player_two = input("Player two, please enter your name: \n")
    while run_game:
        player_input(BOARD, player_one)
        if run_game:
            player_input(BOARD, player_two)


#Play again
def play_again():
    """
    Asks player if they want to restart the game once a player has won or tied the previous round.
    """
    global run_game
    print("Would you like to play again? \n")
    answer = input("Enter Y or N: \n")
    if answer == "Y":
        run_game = True
        main()
    
main()
play_again()
