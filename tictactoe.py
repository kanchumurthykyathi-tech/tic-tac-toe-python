print("TIC TAC TOE")

board = ["1","2","3",
         "4","5","6",
         "7","8","9"]

def show():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def check_winner(player):
    wins = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for win in wins:
        if (board[win[0]] == player and
            board[win[1]] == player and
            board[win[2]] == player):
            return True

    return False

player = "X"

for turn in range(9):

    show()

    pos = int(input(f"Player {player}, choose a position (1-9): "))

    if board[pos-1] != "X" and board[pos-1] != "O":

        board[pos-1] = player

        if check_winner(player):
            show()
            print(f"Player {player} Wins!")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"

    else:
        print("Position already taken!")

else:
    show()
    print("Match Draw!")
