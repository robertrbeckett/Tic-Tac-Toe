# Tic-Tac-Toe

This is a Tic-Tac-Toe game I'm doing as a personal project to learn Python programming. 

I want to put in a graphical interface. I could do this with Turtle, but I haven't decided if that's the route I want to go. I also intend to put in a menu so that the computer asks if the user wants to go first and if the user wants to play X's or O's.

I also want to introduce levels of difficulty. Currently, the computer plays randomly. Eventually I'll make it so the computer asks how hard to make the game and can play using different levels of strategy: attempting to get 3 in a row, blocking when the user gets 2 in a row, attempting to fork the user.

For the board, I thought about using a list or a Python array, aka a list of nested lists. If I were working with a more sophistitated program like 4-in-a-row, then this might be worthwhile because I could do strategy or check whether someone has won by starting with moves that have been made and then querying the array relationally. However, in Tic-Tac-Toe there are only 8 possible wins. In order to get the game going, it was easier just to check all of them. Maybe as a warm-up to doing a more sophisticated game, I'll rework my board into an array, but for now, I don't see any compelling reason to do so.

I also feel like what I've done so far can be done with substantially fewer lines of code. I'd like to revise it to make that happen too.

I've developed my program using https://repl.it/languages/python3
