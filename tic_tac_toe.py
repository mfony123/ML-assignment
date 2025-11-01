def play(board):
    # Determine whose turn it is
    x_count = board.count('x')
    o_count = board.count('o')
    player = 'x' if x_count == o_count else 'o'
    opponent = 'o' if player == 'x' else 'x'

    # All possible winning combinations (rows, columns, diagonals)
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]

    # 1️⃣ Rule 1: Try to win if possible
    for a, b, c in wins:
        line = [board[a], board[b], board[c]]
        if line.count(player) == 2 and line.count('') == 1:
            return [a, b, c][line.index('')]

    # 2️⃣ Rule 2: Block opponent's winning move
    for a, b, c in wins:
        line = [board[a], board[b], board[c]]
        if line.count(opponent) == 2 and line.count('') == 1:
            return [a, b, c][line.index('')]

    # 3️⃣ Rule 3: Take the center if available
    if board[4] == '':
        return 4

    # 4️⃣ Rule 4: Take a corner if available
    for i in [0, 2, 6, 8]:
        if board[i] == '':
            return i

    # 5️⃣ Rule 5: Take any available side
    for i in [1, 3, 5, 7]:
        if board[i] == '':
            return i

    # 6️⃣ If all filled (shouldn’t happen), return -1
    return -1
    