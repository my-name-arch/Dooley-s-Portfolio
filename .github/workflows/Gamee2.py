class gameGUI:


   def __init__(self):
       self.main = tk.Tk()


       self.canvas = tk.Canvas(self.main, width=400, height=400, bg="light blue")
       self.canvas.grid(row=0, column=0)


       self.squares = []


       # Generate mine locations
       self.mine_locs = [self.mine_generator() for _ in range(8)]


       for i in range(8):
           for j in range(8):
               x1, y1 = i * 50, j * 50
               x2, y2 = x1 + 50, y1 + 50
               square = self.canvas.create_rectangle(x1, y1, x2, y2, fill="light blue")
               self.squares.append(square)


               # Binding click event to the square
               self.canvas.tag_bind(square, "<Button-1>", lambda event, s=square: self.on_square_click(s))


       quitButton = tk.Button(self.main, text="Quit", command=self.quitCallBack)
       quitButton.grid(row=1, column=0, columnspan=8)


   def mine_generator(self):
       return random.randint(1, 64)


   def on_square_click(self, square_id):
       if square_id in [self.squares[loc - 1] for loc in self.mine_locs]:
           self.display_end_window()
       else:
           adjacent_mines = self.count_adjacent_mines(square_id)
           if adjacent_mines:
               self.canvas.create_text(self.canvas.coords(square_id)[0] + 25, self.canvas.coords(square_id)[1] + 25, text=str(adjacent_mines), fill="black")
           self.canvas.itemconfig(square_id, fill="white")


   def count_adjacent_mines(self, square_id):
       adjacent_mines = 0
       square_index = self.squares.index(square_id)
       x, y = square_index // 8, square_index % 8
       for dx in [-1, 0, 1]:
           for dy in [-1, 0, 1]:
               if (0 <= x + dx < 8) and (0 <= y + dy < 8):
                   neighbor_index = (x + dx) * 8 + (y + dy)
                   neighbor_id = self.squares[neighbor_index]
                   if neighbor_id in self.mine_locs:
                       adjacent_mines += 1
       return adjacent_mines


   def quitCallBack(self):
       self.main.destroy()
       sys.exit()


   def run(self):
       self.main.mainloop()


   def display_end_window(self):
       end_window = tk.Toplevel(self.main)
       end_window.title("Game Over")
       end_message = tk.Label(end_window, text="You hit a mine! Try Again?")
       end_message.pack()
       try_again_button = tk.Button(end_window, text="Try Again", command=self.try_again)
       try_again_button.pack()
       quit_button = tk.Button(end_window, text="Quit", command=self.quitCallBack)
       quit_button.pack()


   def try_again(self):
       self.main.destroy()
       new_game = gameGUI()
       new_game.run()


startScreenGUI = startScreen()
startScreenGUI.run()


