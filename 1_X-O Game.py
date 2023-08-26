def show_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print()
    print("-------------")

def winner(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    players = ["X", "O"] 
    current = players[0]
    i = 0
    while True: 
        try:
            row = int(input("Enter row (0-2) for " + current + ": "))
            col = int(input("Enter column (0-2) for " + current + ": "))
            if row not in range(3) or col not in range(3):
                raise ValueError("Invalid input. Please enter a number between 0 and 2.")
        except ValueError as e:
            print(e)
            continue
        else:
            if board[row][col] != " ":
                print("Invalid. Try again.")
                continue
            board[row][col] = current
            show_board(board)
            if winner(board, current):
                print(current + " wins!")
                return
            i += 1
            current = players[i%2]
tic_tac_toe()