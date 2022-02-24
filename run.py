# Create board

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
    print(board[6] + "|" + board[7] + "|" + board[8])

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
                break
            else:
                print(f"{inp} is not a valid number, try again.")
        except ValueError as e:
            print(f"{e} is not valid, try again.")


#Check for win or tie 
def win_horizontally(board, player):
    """
    Check for win horizontally
    """
    if board[0] == board[1] == board[2] and board[0] != "-":
        print(f"Congratz {player}, You won the game!")
    elif board[3] == board[4] == board[5] and board[3] != "-":
        print(f"Congratz {player}, You won the game!")
    elif board[6] == board[7] == board[8] and board[6] != "-":
        print(f"Congratz {player}, You won the game!")
    
def win_vertically(board, player):
    """
    Check fo win vertically
    """
    if board[0] == board[3] == board[6] and board[0] != "-":
        print(f"Congratz {player}, You won the game!")
    elif board[1] == board[4] == board[7] and board[1] != "-":
        print(f"Congratz {player}, You won the game!")
    elif board[2] == board[5] == board[8] and board[3] != "-":
        print(f"Congratz {player}, You won the game!")

def win_diagonally(board, player):
    """
    Check for win diagonally
    """
    if board[0] == board[4] == board[8] and board[0] != "-":
        print(f"Congratz {player}, You won the game!")
    elif board[2] == board[4] == board[6] and board[2] != "-":
        print(f"Congratz {player}, You won the game!")

def check_for_win(board, player):
    win_horizontally(board,player)
    win_vertically(board, player)
    win_diagonally(board, player)
            
#Switch player

#Run game
player_one = input("Player one, please enter your name: \n")
player_two = input("Player two, please enter your name: \n")

def main():
    while run_game:
        player_input(BOARD, player_one)
        print_board(BOARD)
        check_for_win(BOARD, player_one)
        player_input(BOARD, player_two)
        print_board(BOARD)
        check_for_win(BOARD, player_two)
main()
print("XD")