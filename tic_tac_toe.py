def print_board(board):
    print("    1   2   3")
    print("  +---+---+---+")
    for i, row in enumerate(board):
        print(f"{chr(65+i)} | {' | '.join(row)} |")
        print("  +---+---+---+")

def check_win(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(row[i] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    move_map = {'A': 0, 'B': 1, 'C': 2}

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    current_player = 0
    while True:
        player = players[current_player]
        move = input(f"Player {player}, enter your move (e.g. A1, B2): ").upper()

        if len(move) != 2 or move[0] not in move_map or move[1] not in '123':
            print("Invalid input. Try again.")
            continue

        row = move_map[move[0]]
        col = int(move[1]) - 1

        if board[row][col] != ' ':
            print("That spot is already taken. Try again.")
            continue

        board[row][col] = player
        print_board(board)

        if check_win(board, player):
            print(f"Player {player} wins!")
            break

        if is_full(board):
            print("It's a draw!")
            break

        current_player = 1 - current_player

if __name__ == "__main__":
    main()


          