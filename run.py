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
    inp = int(input(f"{player} please chose a number between 1-9 to place your symbol: \n"))
    board[inp-1] = current_player

#Check for win or tie 

#Switch player

#Run game
player_one = input("Player one, please enter your name: \n")
player_two = input("Player two, please enter your name: \n")
while run_game:
    player_input(BOARD, player_one)
    print_board(BOARD)
    player_input(BOARD, player_two)
    print_board(BOARD)