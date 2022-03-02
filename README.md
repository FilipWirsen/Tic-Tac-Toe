# Tic-Tac-Toe

Tic-Tac-Toe is a python terminal game, which runs in the mock terminal on Heroku.

Users can try to beat the computer in a game of Tic-Tac-Toe. The goal of this game is to place three of your own symbols in a row before the computer does or the board gets filled.

[Here is the live link to my game](https://tic-tac-toe-ci.herokuapp.com/)

## How to Play

The following rules apply to the Tic-Tac-Toe game:

1. The game is played on a grid that's 3 squares by 3 squares.
2. The user is X and the computer is O.
3. The user and computer take turns to place their symbol on empty squares. 
4. The first player to get 3 of their symbols in a row (up, down, across or diagonally) is the winner.
5. If all 9 squares are full but no player has 3 symbols in a row the game ends in a tie.


## Features

* The user is greeted to the game and the instructions from "How to play" is displayed.
    * A 3x3 board is created and the user is asked to enter their name.
![Welcome msg](images/welcome-msg-tic-tac-toe.png)

* The user and computer takes turns to place their symbol on empty squares until there is a winner or the game is tied.
![Take turns](images/take-turns-tic-tac-toe.png)

* Once the game is over the user is asked if they want to play again. Entering Y restarts the game and N exits the game.
![Game finished](images/game-finished-tic-tac-toe.png)


## Testing

I manually tested this project by doing the following:
 * Passed the code through a PEP8 validator and there are no errors. 
 * Gave invalid inputs: invalid numbers, same number twice and strings when ints were expected.
 * Tested the game in Gitpod terminal and my Heroku terminal.

 
 ## Bugs

 ### Solved Bugs
 * I got a bug where the computer always tried to place its symbol on the same square as the user did.
    * I fixed this by adding a if statement: (if BOARD[random_index] == '-':). It makes the computer only return their number if the square it correlates with is empty
 * Got a bug witch made the game check all diffrent win conditions even if one of them already had returned true.
    * I fixed this by checking all diffrent win conditions in one if statement. I did this by using the or operator.

 ### Remaining Bugs
 * I have not been able to find any remaining bugs.

## Validating
* PEP8
    * No errors were returned from [PEP8online.com](http://pep8online.com/checkresult)

## Deployment

This project was deployed using Code institue's mock terminal for Heroku.

I did the following to deploy my project: 
* Create a new Heroku app
* Under "Settings" tab
    * Add config var (PORT, 8000)
    * Added two buildpacks in this order: Python, NodeJS
* Under "Deploy" tab
    * Linked the Heroku app to the repository on GitHub
    * Enable automatic deployment from "main" branch
    * Click on "Deploy branch"

## Credits
* Code institute for the deployment terminal.
* My mentor for helping me understand diffrent concepts such as, Short circuiting.
* [Stack overflow](https://stackoverflow.com/) for researching what logic should be used to check for wins.
* [Flake8rules](https://www.flake8rules.com) for helping me understand how and why to tidy up my code.