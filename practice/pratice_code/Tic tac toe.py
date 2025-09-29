# Tic Tac Toe Game using cell numbers 1–9

def print_board(board):
    print()
    for i in range(3):
        row = board[i]
        print(" " + " | ".join(row))
        if i < 2:
            print("---|---|---")
    print()

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell in ["X", "O"] for row in board for cell in row)

def main():
    # Start with a board showing numbers 1–9
    board = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        try:
            move = int(input("Enter a number (1-9): "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if move < 1 or move > 9:
            print("Number out of range. Try again.")
            continue

        row = (move - 1) // 3
        col = (move - 1) % 3

        if board[row][col] in ["X", "O"]:
            print("Cell already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
