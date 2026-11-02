# Tic-Tac-Toe: Human vs Human or Human vs AI (Minimax)

WINS = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def winner(b):
    """Return 'X' or 'O' if someone has three in a line, else None."""
    for a, c, d in WINS:
        if b[a] == b[c] == b[d] != " ":
            return b[a]

def show(b):
    cells = [c if c != " " else str(i + 1) for i, c in enumerate(b)]
    rows = [" " + " | ".join(cells[i:i+3]) for i in (0, 3, 6)]
    print("\n" + "\n---+---+---\n".join(rows) + "\n")

def minimax(b, ai_turn):
    """Score for AI ('O'): +1 win, -1 loss, 0 draw."""
    w = winner(b)
    if w:
        return 1 if w == "O" else -1
    if " " not in b:
        return 0
    scores = []
    for i in range(9):
        if b[i] == " ":
            b[i] = "O" if ai_turn else "X"
            scores.append(minimax(b, not ai_turn))
            b[i] = " "
    return max(scores) if ai_turn else min(scores)

def ai_move(b):
    def score(i):
        b[i] = "O"
        s = minimax(b, False)
        b[i] = " "
        return s
    return max((i for i in range(9) if b[i] == " "), key=score)

def play():
    scores = {"X": 0, "O": 0, "Draw": 0}
    while True:
        b, turn = [" "] * 9, "X"
        vs_ai = input("1) Human vs Human  2) Human vs AI: ").strip() == "2"

        while not winner(b) and " " in b:
            show(b)
            if vs_ai and turn == "O":
                move = ai_move(b)
            else:
                pos = input(f"Player {turn}, choose (1-9): ")
                if not pos.isdigit() or not 1 <= int(pos) <= 9 or b[int(pos) - 1] != " ":
                    print("Invalid move, try again.")
                    continue
                move = int(pos) - 1
            b[move] = turn
            turn = "O" if turn == "X" else "X"

        show(b)
        result = winner(b) or "Draw"
        scores[result] += 1
        print("It's a draw!" if result == "Draw" else f"Player {result} wins!")
        print(f"Scores -> X: {scores['X']}  O: {scores['O']}  Draws: {scores['Draw']}")

        if input("\nPlay again? (y/n): ").lower().strip() != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play()