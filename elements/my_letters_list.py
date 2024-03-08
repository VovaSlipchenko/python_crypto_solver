import tkinter as tk
import math
from tkinter import LEFT

class MyLetterList:
    def __init__(self, root):
        self.buttons_in_row = 10
        self.total_buttons = 0
        self.buttons_array = []
        self.frame = tk.Frame(root)
        self.frame.grid()    

    def addLetter(self):
        
        #print('total_buttons = '+str(self.total_buttons))
        row = math.floor(self.total_buttons / self.buttons_in_row)
        #print(row)
        column = self.total_buttons - row*self.buttons_in_row

        button = tk.Button(self.frame, width=4, height=2)
        button.grid(row=row, column=column)
        #button.pack(side=LEFT)

        self.total_buttons += 1
        
        self.buttons_array.append(button)