from functools import partial
from tkinter import *

class PuzzleGUI(Tk):
    def __init__(self, puzzle, solution):
        self.root = Tk()
        self.root.geometry("600x600")
        self.root.config(bg = "#FFA07A")

        # The frame containing the puzzle
        frame = Frame(self.root, bg = "#F5FFFA", borderwidth = "5", relief = "solid")
        frame.place(relx = 0.2, rely = 0.2, relheight = 0.59, relwidth = 0.59)
        # The solve button
        solve = Button(self.root, text = "Solve", bg="#FF4500", fg="white", font=("Helvetica", 14), command = self.solve)
        solve.place(relx = 0.4, rely = 0.85, relheight = 0.1, relwidth = 0.2)

        self.labels = dict()    # dictionary mapping each number to the GUI label contining it
        self.puzzle = puzzle
        self.solution = solution

        c = 0.21
        d = 0.21
        for i in self.puzzle:
            if i != '0': # add a label to that number
                b = Label(self.root, text = i, bg="#1c9cd4", fg="white", font=("Helvetica", 24), 
                    borderwidth = "1", relief = 'sunken')
                self.labels[i] = [b, c, d]
                b.place(relx = c, rely = d, relheight = 0.19, relwidth = 0.19)
            c += 0.19
            if round(c, 2) == 0.78:
                c = 0.21
                d += 0.19

        self.root.mainloop()

    def solve(self):
        zero = self.puzzle.index('0')
        swapped = self.puzzle.index('0') # The index of the number swapped. Initially set to position of 0.

        def f(i):
            nonlocal zero, swapped
            self.puzzle[zero], self.puzzle[swapped] = self.puzzle[swapped], self.puzzle[zero]
            self.moveLabel(self.solution[i])
            zero = self.puzzle.index('0')
            swapped = self.puzzle.index(self.solution[i])
            if i < len(self.solution) - 1:
                # CHANGE the number 500 below to control the speed of the blocks.
                self.root.after(500, partial(f, i+1))
            else:
                Label(self.root, text = f"Cost: {len(self.solution)}", bg="#FFA07A", fg="#2E8B05",
                    font=("Helvetica", 30)).place(relx = 0.36, rely = 0.1)
        f(0)

    def moveLabel(self, num: str):
        num_value = self.labels[num]
        c = num_value[1]
        d = num_value[2]
        x = 0

        def move():
            nonlocal c, x, d
            if self.puzzle.index(num) == self.puzzle.index('0') - 1: c += 0.01
            elif self.puzzle.index(num) == self.puzzle.index('0') + 1: c -= 0.01
            elif self.puzzle.index(num) == self.puzzle.index('0') - 3: d += 0.01
            elif self.puzzle.index(num) == self.puzzle.index('0') + 3: d -= 0.01
            x += 0.01
            num_value[0].place(relx = c, rely = d, relheight = 0.19, relwidth = 0.19)
            if round(x, 2) != 0.19:
                self.root.after(3, move)
            else:
                self.labels[num][1] = c
                self.labels[num][2] = d
        
        move()