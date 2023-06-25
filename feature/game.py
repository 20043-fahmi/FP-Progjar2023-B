import tkinter as tk
import random
# import fonts


class Game(tk.Frame):

    Color_grid = "#1b1e4d"
    Color_EmptyCell = "#edeef0"
    Color_Score = "#a9aab8"
    Font_ScoreLabel = ("Fredoka One", 20, "bold")
    Font_Score = ("Fredoka One", 36, "bold")
    Font_GameOver = ("Fredoka One", 40, "bold")
    Font_Color_GameOver = "#ffffff"
    Winner_BG = "#001eff"
    Loser_BG = "#898ca3"

    Color_Cells = {
        2: "#cacde3",
        4: "#c6c8f7",
        8: "#8291f5",
        16: "#4660f2",
        32: "#5c6cff",
        64: "#2e40e6",
        128: "#919fed",
        256: "#303efc",
        512: "#4a50ff",
        1024: "#223df0",
        2048: "#504dfa",
        4096: "#0d0b99",
        8192: "#1e1cad",
        16384: "#444394"
    }

    Color_CellNumber = {
        2: "#000000",
        4: "#000000",
        8: "#ffffff",
        16: "#ffffff",
        32: "#ffffff",
        64: "#ffffff",
        128: "#ffffff",
        256: "#ffffff",
        512: "#ffffff",
        2048: "#ffffff",
        8192: "#ffffff",
        16384: "#ffffff"
    }

    Fonts_CellNumebr = {
        2: ("Fredoka One", 45, "bold"),
        4: ("Fredoka One", 45, "bold"),
        8: ("Fredoka One", 45, "bold"),
        16: ("Fredoka One", 40, "bold"),
        32: ("Fredoka One", 40, "bold"),
        64: ("Fredoka One", 40, "bold"),
        128: ("Fredoka One", 35, "bold"),
        256: ("Fredoka One", 35, "bold"),
        512: ("Fredoka One", 35, "bold"),
        1024: ("Fredoka One", 30, "bold"),
        2048: ("Fredoka One", 30, "bold"),
        8192: ("Fredoka One", 30, "bold"),
        16384: ("Fredoka One", 25, "bold")
    }

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.grid()
        self.master.title("2048")

        self.grid_main = tk.Frame(
            self, bg=Game.Color_grid, bd=3, width=600, height=600
        )
        self.grid_main.grid(pady=(110, 0))

        self.GUI_maker()
        self.start_game()

        self.high_score = 0
        self.current_score = 0

        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)

        # self.mainloop()

    def GUI_maker(self):
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                frame_cells = tk.Frame(
                    self.grid_main,
                    bg=Game.Color_EmptyCell,
                    width=100,
                    height=100
                )
                frame_cells.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.grid_main, bg=Game.Color_EmptyCell)
                cell_data = {"frame": frame_cells, "number": cell_number}

                cell_number.grid(row=i, column=j)
                row.append(cell_data)
            self.cells.append(row)

        """
        frame_score = tk.Frame(self)
        frame_score.place(relx=0.5, y=60, anchor="center")
        tk.Label(
            frame_score,
            text="Skor",
            font=Game.Font_ScoreLabel,
            bg=Game.Color_Score
        ).grid(row=0)
        self.label_score = tk.Label(
            frame_score, text="0", font=Game.Font_ScoreLabel)
        self.label_score.grid(row=1)
        """

        frame_high_score = tk.Frame(self)
        frame_high_score.place(relx=0.5, y=10, anchor="center")
        tk.Label(
            frame_high_score,
            text="High Score",
            font=Game.Font_ScoreLabel,
            bg=Game.Color_Score
        ).grid(row=0)
        self.label_high_score = tk.Label(
            frame_high_score, text="0", font=Game.Font_ScoreLabel)
        self.label_high_score.grid(row=1)

        frame_current_score = tk.Frame(self)
        frame_current_score.place(relx=0.5, y=90, anchor="center")
        tk.Label(
            frame_current_score,
            text="Current Score",
            font=Game.Font_ScoreLabel,
            bg=Game.Color_Score
        ).grid(row=0)
        self.label_current_score = tk.Label(
            frame_current_score, text="0", font=Game.Font_ScoreLabel)
        self.label_current_score.grid(row=1)

        frame_buttons = tk.Frame(self)
        frame_buttons.place(relx=0.8, y=40, anchor="center")
        restart_button = tk.Button(
            frame_buttons,
            text="Restart",
            font=Game.Font_ScoreLabel,
            command=self.restart_game
        )
        restart_button.pack()

    def start_game(self):
        self.matrix = [[0] * 4 for _ in range(4)]

        row = random.randint(0, 3)
        col = random.randint(0, 3)
        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg=Game.Color_Cells[2])
        self.cells[row][col]["number"].configure(
            bg=Game.Color_Cells[2],
            fg=Game.Color_CellNumber[2],
            font=Game.Fonts_CellNumebr[2],
            text="2"
        )
        while (self.matrix[row][col] != 0):
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg=Game.Color_Cells[2])
        self.cells[row][col]["number"].configure(
            bg=Game.Color_Cells[2],
            fg=Game.Color_CellNumber[2],
            font=Game.Fonts_CellNumebr[2],
            text="2"
        )

        self.current_score = 0

    def restart_game(self):
        self.start_game()
        self.label_current_score.configure(text="0")
        self.GUI_update()

    def stack(self):
        Matrix_1 = [[0] * 4 for _ in range(4)]
        for i in range(4):
            position_fill = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    Matrix_1[i][position_fill] = self.matrix[i][j]
                    position_fill += 1
        self.matrix = Matrix_1

    def combine(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    self.score += self.matrix[i][j]
                    self.current_score = self.score

    def reverse(self):
        Matrix_1 = []
        for i in range(4):
            Matrix_1.append([])
            for j in range(4):
                Matrix_1[i].append(self.matrix[i][3-j])
        self.matrix = Matrix_1

    def transpose(self):
        Matrix_1 = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                Matrix_1[i][j] = self.matrix[j][i]
        self.matrix = Matrix_1

    def add_tile(self):
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        while (self.matrix[row][col] != 0):
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.matrix[row][col] = random.choice([2, 4])

    def GUI_update(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j]["frame"].configure(
                        bg=Game.Color_EmptyCell)
                    self.cells[i][j]["number"].configure(
                        bg=Game.Color_EmptyCell, text="")
                else:
                    self.cells[i][j]["frame"].configure(
                        bg=Game.Color_Cells[cell_value])
                    self.cells[i][j]["number"].configure(
                        bg=Game.Color_Cells[cell_value],
                        fg=Game.Color_CellNumber[cell_value],
                        font=Game.Fonts_CellNumebr[cell_value],
                        text=str(cell_value)
                    )
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        self.label_high_score.configure(text=str(self.high_score))
        self.label_current_score.configure(text=str(self.current_score))
        self.update_idletasks()

    def left(self, event):
        self.stack()
        self.combine()
        self.stack()
        self.add_tile()
        self.GUI_update()
        self.game_over()

    def right(self, event):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.add_tile()
        self.GUI_update()
        self.game_over()

    def up(self, event):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        self.add_tile()
        self.GUI_update()
        self.game_over()

    def down(self, event):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        self.add_tile()
        self.GUI_update()
        self.game_over()

    def Exists_horizontalMoves(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j + 1]:
                    return True
        return False

    def Exists_verticalMoves(self):
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i + 1][j]:
                    return True
        return False

    def game_over(self):
        if any(16384 in row for row in self.matrix):
            game_over_frame = tk.Frame(self.grid_main, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                game_over_frame,
                text="YOU WIN!!",
                bg=Game.Winner_BG,
                fg=Game.Font_Color_GameOver,
                font=Game.Font_GameOver
            ).pack()
        elif not any(0 in row for row in self. matrix) and not self.Exists_horizontalMoves() and not self.Exists_verticalMoves():
            game_over_frame = tk.Frame(self.grid_main, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                game_over_frame,
                text="GAME OVER!!",
                bg=Game.Loser_BG,
                fg=Game.Font_Color_GameOver,
                font=Game.Font_GameOver
            ).pack()
