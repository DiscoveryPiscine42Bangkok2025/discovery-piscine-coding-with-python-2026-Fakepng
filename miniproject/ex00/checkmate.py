import sys

def checkmate(board_str):
    board = format_board(board_str)

    check_valid_board(board)

    is_checkmate(board)

def format_board(board_str):
    # Check board is string
    if not board_str or not isinstance(board_str, str):
        print("Invalid board format")
        sys.exit(1)

    return [list(line) for line in board_str.splitlines()]

def check_valid_board(board):
    # Check if board is n x n
    row_count = len(board)
    for row in board:
        if len(row) != row_count:
            print("Invalid board shape")
            sys.exit(1)

    # Check if there is exactly one king
    king_count = sum(row.count('K') for row in board)
    if king_count != 1:
        print("Invalid number of kings")
        sys.exit(1)

    # Check for valid pieces
    valid_pieces = {'K', 'Q', 'B', 'R', 'P', '.'}
    for row in board:
        for piece in row:
            if piece not in valid_pieces:
                print(f"Invalid piece found: {piece}")
                sys.exit(1)

def is_checkmate(board):
    # Find king position
    king_pos = None
    for i, row in enumerate(board):
        for j, piece in enumerate(row):
            if piece == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    print(f"King position: {king_pos}")

    check_pawns(board, king_pos)
    check_bishops(board, king_pos)
    check_rooks(board, king_pos)
    check_queens(board, king_pos)

    print("Fail")

def check_pawns(board, king_pos):
    for i, row in enumerate(board):
        for j, piece in enumerate(row):
            if piece == 'P':
                # Pawns attack diagonally forward
                if (i - 1, j - 1) == king_pos or (i - 1, j + 1) == king_pos:
                    print("Success")
                    sys.exit(0)

def check_bishops(board, king_pos):
    for i, row in enumerate(board):
        for j, piece in enumerate(row):
            if piece == 'B':
                # Check diagonals for bishop attack
                # Check top-left diagonal
                for x, y in zip(range(i-1, -1, -1), range(j-1, -1, -1)):
                    # print(f"Checking bishop at {(i,j)} to {(x,y)}")
                    if (x, y) == king_pos:
                        print("Success")
                        sys.exit(0)
                    if board[x][y] != '.':
                        break

                # Check top-right diagonal
                for x, y in zip(range(i-1, -1, -1), range(j+1, len(board))):
                    # print(f"Checking bishop at {(i,j)} to {(x,y)}")
                    if (x, y) == king_pos:
                        print("Success")
                        sys.exit(0)
                    if board[x][y] != '.':
                        break

                # Check bottom-left diagonal
                for x, y in zip(range(i+1, len(board)), range(j-1, -1, -1)):
                    # print(f"Checking bishop at {(i,j)} to {(x,y)}")
                    if (x, y) == king_pos:
                        print("Success")
                        sys.exit(0)
                    if board[x][y] != '.':
                        break

                # Check bottom-right diagonal
                for x, y in zip(range(i+1, len(board)), range(j+1, len(board))):
                    # print(f"Checking bishop at {(i,j)} to {(x,y)}")
                    if (x, y) == king_pos:
                        print("Success")
                        sys.exit(0)
                    if board[x][y] != '.':
                        break

def check_rooks(board, king_pos):
    for i, row in enumerate(board):
        for j, piece in enumerate(row):
            if piece == 'R':
                # Check vertical and horizontal for rook attack
                # Check upwards
                for x in range(i-1, -1, -1):
                    # print(f"Checking rook at {(i,j)} to {(x,j)}")
                    if (x, j) == king_pos:
                        print("Success")
                        sys.exit(0)
                    if board[x][j] != '.':
                        break

                # Check downwards
                for x in range(i+1, len(board)):
                    # print(f"Checking rook at {(i,j)} to {(x,j)}")
                    if (x, j) == king_pos:
                        print("Success")
                        sys.exit(0)
                    if board[x][j] != '.':
                        break

                # Check left
                for y in range(j-1, -1, -1):
                    # print(f"Checking rook at {(i,j)} to {(i,y)}")
                    if (i, y) == king_pos:
                        print("Success")
                        sys.exit(0)
                    if board[i][y] != '.':
                        break

                # Check right
                for y in range(j+1, len(board)):
                    # print(f"Checking rook at {(i,j)} to {(i,y)}")
                    if (i, y) == king_pos:
                        print("Success")
                        sys.exit(0)
                    if board[i][y] != '.':
                        break

def check_queens(board, king_pos):
    for i, row in enumerate(board):
        for j, piece in enumerate(row):
            if piece == 'Q':
                # Check diagonals for queen attack (like bishop)
                # Check top-left diagonal
                for x, y in zip(range(i-1, -1, -1), range(j-1, -1, -1)):
                    # print(f"Checking queen at {(i,j)} to {(x,y)}")
                    if (x, y) == king_pos:
                        print("Success")
                        sys.exit(0)
                    if board[x][y] != '.':
                        break

                # Check top-right diagonal
                for x, y in zip(range(i-1, -1, -1), range(j+1, len(board))):
                    # print(f"Checking queen at {(i,j)} to {(x,y)}")
                    if (x, y) == king_pos:
                        print("Success")
                        sys.exit(0)
                    if board[x][y] != '.':
                        break

                # Check bottom-left diagonal
                for x, y in zip(range(i+1, len(board)), range(j-1, -1, -1)):
                    # print(f"Checking queen at {(i,j)} to {(x,y)}")
                    if (x, y) == king_pos:
                        print("Success")
                        sys.exit(0)
                    if board[x][y] != '.':
                        break

                # Check bottom-right diagonal
                for x, y in zip(range(i+1, len(board)), range(j+1, len(board))):
                    # print(f"Checking queen at {(i,j)} to {(x,y)}")
                    if (x, y) == king_pos:
                        print("Success")
                        sys.exit(0)
                    if board[x][y] != '.':
                        break

                # Check vertical and horizontal for queen attack (like rook)
                # Check upwards
                for x in range(i-1, -1, -1):
                    # print(f"Checking queen at {(i,j)} to {(x,j)}")
                    if (x, j) == king_pos:
                        print("Success")
                        sys.exit(0)
                    if board[x][j] != '.':
                        break

                # Check downwards
                for x in range(i+1, len(board)):
                    # print(f"Checking queen at {(i,j)} to {(x,j)}")
                    if (x, j) == king_pos:
                        print("Success")
                        sys.exit(0)
                    if board[x][j] != '.':
                        break

                # Check left
                for y in range(j-1, -1, -1):
                    # print(f"Checking queen at {(i,j)} to {(i,y)}")
                    if (i, y) == king_pos:
                        print("Success")
                        sys.exit(0)
                    if board[i][y] != '.':
                        break

                # Check right
                for y in range(j+1, len(board)):
                    # print(f"Checking queen at {(i,j)} to {(i,y)}")
                    if (i, y) == king_pos:
                        print("Success")
                        sys.exit(0)
                    if board[i][y] != '.':
                        break