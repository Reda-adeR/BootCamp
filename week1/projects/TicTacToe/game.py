
positions = {f"{row}{col}": (i, j)
             for i, row in enumerate("ABC")
             for j, col in enumerate("123")}

class TicTacToe:
    def __init__(self):
        import random
        self.board = [["." for _ in range(3)] for _ in range(3)]
        self.player = random.choice(["x","o"])
        self.moves = 0

    def display_board(self, board):
        print("  --1---2---3--")
        for i,row in enumerate(board):
            rowIdx = "ABC"[i]
            print(f"{rowIdx} | {row[0]} | {row[1]} | {row[2]} |")
            print("- |---|---|---|")

    def switch_turn(self, player):
        self.player = "x" if player == "o" else "o"

    def update_board(self, player):
        while 1:
            pos = self.player_input(player)
            if not pos:
                continue
            if self.board[pos[0]][pos[1]] is not ".":
                continue
            self.board[pos[0]][pos[1]] = player
            return pos


    def player_input(self, player):
        pos = input(f"It's {player}'s Turn : ")
        if pos in positions:
            return positions[pos]

    def checkWin(self, pos):
        r, c = pos
        symbol = self.board[r][c]
        directions = [
            [(0, 1), (0, -1)],   # Horizontal
            [(1, 0), (-1, 0)],   # Vertical
            [(1, 1), (-1, -1)],  # Diagonal \
            [(1, -1), (-1, 1)]   # Diagonal /
        ]

        for direction in directions:
            count = 1
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                while 0 <= nr < 3 and 0 <= nc < 3 and self.board[nr][nc] == symbol:
                    count += 1
                    nr += dr
                    nc += dc
            if count >= 3:
                return True
        return False


    def play(self):
        print("WELCOME TO TIC TAC TOE GAME")
        print("ITS 2 PLAYERS MODE X - O")
        print("To Play just Select your spot A1 A2 . . .")
        self.display_board(self.board)
        while 1:
            pos = self.update_board(self.player)
            self.display_board(self.board)
            if self.moves > 4:
                if self.checkWin(pos):
                    print(f"Winner is {self.player}")
                    break
            elif self.moves == 9:
                print("DRAW MATCH")
                break
            self.switch_turn(self.player)
            self.moves += 1


bo = TicTacToe()
d = [
    ["x","o","x"],
    ["x","o","x"],
    ["x","o","x"]
]
bo.play()
