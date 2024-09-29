import tkinter as tk
from calc_UI import calcUI

class CALCULATOR:

  def __init__(self):
    
    self.root = tk.Tk()

    self.root.geometry("400x500")
    self.root.title("Calculator")

    self.textbox = tk.Text(self.root, font=('Arial', 16), height=1)
    self.textbox.pack(padx=10, pady=10)

    self.btnframe = calcUI(self.root)

    self.root.mainloop()

CALCULATOR()
