board = []
for i in range(0,5):
    board.append(["O"]*5)

def print_board(board):
    for row in range(0,len(board)):
        
        print " ".join(board[row])



### 1 guess battle ships!

from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))

print ship_row
print ship_col

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
elif board[guess_row][guess_col] == "X":
    print "You guessed that one already."
    print_board(board)
else:
    print_board(board)
    if guess_row not in range(len(board)) or guess_col not in range(len(board)):
        print "Oops, that's not even in the ocean."
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
        print_board(board)


##include for loop and break
        from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!


turn = 0
for turn in range(4):
    print "Turn", turn + 1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if turn == 3:
            print "Game Over"
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
            if turn == 3:
                print "Game Over"
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
            if turn == 3:
                print "Game Over"
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            if turn == 3:
                print "Game Over"
        # Print (turn + 1) here!
        print_board(board)
