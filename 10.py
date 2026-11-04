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

def minimax(b, ai):
    w = winner(b)
    if w: return 1 if w == "O" else -1
    if " " not in b: return 0
    s = [minimax(b[:i] + ["O" if ai else "X"] + b[i+1:], not ai) for i in range(9) if b[i] == " "]
    return max(s) if ai else min(s)

def ai_move(b):
    return max((i for i in range(9) if b[i] == " "), key=lambda i: minimax(b[:i] + ["O"] + b[i+1:], False))

def play():
    sc = {"X": 0, "O": 0, "Draw": 0}
    while True:
        b, t, ai = [" "] * 9, "X", input("1) Human vs Human  2) Human vs AI: ").strip() == "2"
        while not winner(b) and " " in b:
            show(b)
            if ai and t == "O":
                m = ai_move(b)
            else:
                p = input(f"Player {t}, choose (1-9): ")
                if not (p.isdigit() and 1 <= int(p) <= 9 and b[int(p) - 1] == " "):
                    print("Invalid move."); continue
                m = int(p) - 1
            b[m], t = t, "OX"[t == "O"]
        show(b)
        r = winner(b) or "Draw"
        sc[r] += 1
        print("Draw!" if r == "Draw" else f"Player {r} wins!", sc)
        if input("Play again? (y/n): ").lower().strip() != "y": break

if __name__ == "__main__":
    play()
