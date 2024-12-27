import random
import tkinter as tk
from imageTools import *
import sys


class startScreen:
  def __init__(self):
      self.rootWin=tk.Tk()
      self.rootWin.title("minesweeper")
      self.canvas = tk.Canvas(self.rootWin, bg="lightgreen", width=400, height=400)
      self.canvas.grid(column=10,row=10,rowspan=800,columnspan=800)
      quitButton = tk.Button(self.rootWin)
      quitButton["text"] = ("Quit")
      quitButton.grid(column=400, row=400)
      quitButton["command"] = self.quitCallBack




      startButton = tk.Button(self.rootWin)
      startButton["text"] = ("Start")
      startButton.grid(column=400, row=350)
      startButton["command"] = self.startCallBack




      self.welcomeLabel = tk.Label(self.rootWin)
      self.welcomeLabel["text"] = ("Minesweeper")
      self.welcomeLabel.grid(row=200, column=400)




      self.nameLabel=tk.Label(self.rootWin)
      self.nameLabel["text"]=("Made by Dooley Kim and Luke Blankinship")
      self.nameLabel.grid(row=205,column=400)
  def startCallBack(self):
      self.rootWin.destroy()
      gamegui = gameGUI()
      gamegui.run()
  def quitCallBack(self):
      self.rootWin.destroy()
      sys.exit()
  def run(self):
      self.rootWin.mainloop()


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
       end_window.transient(self.main)  # Set end_window as a transient window of the main window
       end_message = tk.Label(end_window, text="You hit a mine! Try Again?")
       end_message.pack()
       try_again_button = tk.Button(end_window, text="Try Again", command=self.try_again)
       try_again_button.pack()
       quit_button = tk.Button(end_window, text="Quit", command=self.quitCallBack)
       quit_button.pack()

   def check_win(self):
       for square_id in self.squares:
           if square_id not in [self.squares[loc - 1] for loc in self.mine_locs]:
               square_index = self.squares.index(square_id)
               x, y = square_index // 8, square_index % 8
               if self.canvas.itemcget(square_id, "fill") != "white":
                   return False
       return True

   def on_square_click(self, square_id):
       if square_id in [self.squares[loc - 1] for loc in self.mine_locs]:
           self.display_end_window()
       else:
           adjacent_mines = self.count_adjacent_mines(square_id)
           if adjacent_mines:
               self.canvas.create_text(self.canvas.coords(square_id)[0] + 25, self.canvas.coords(square_id)[1] + 25, text=str(adjacent_mines), fill="black")
           self.canvas.itemconfig(square_id, fill="white")
           if self.check_win():
            self.display_win_window()

   def display_win_window(self):
       win_window = tk.Toplevel(self.main)
       win_window.title("Congratulations!")
       win_window.transient(self.main)  # Set win_window as a transient window of the main window
       win_message = tk.Label(win_window, text="Congratulations! You've cleared the minefield! Play again?")
       win_message.pack()
       play_again_button = tk.Button(win_window, text="Play Again", command=self.try_again)
       play_again_button.pack()
       quit_button = tk.Button(win_window, text="Quit", command=self.quitCallBack)
       quit_button.pack()

   def try_again(self):
       self.main.destroy()
       new_game = gameGUI()
       new_game.run()


startScreenGUI = startScreen()
startScreenGUI.run()
