import tkinter as tk
import math
from tkinter import LEFT
from PIL import Image
from PIL import ImageTk

class MyKeyboard:
    MODE_SELECT = 1
    MODE_CLICK = 2
    def __init__(self, root, mode):
        self.mode = mode
        self.buttons_in_row = 10
        self.total_buttons = 0
        self.buttons_array = []
        self.images_array = []
        self.frame = tk.Frame(root)
        self.frame.pack()


    def addButton(self, letter_index, file):
        
        width = 40
        height = 40

        #print('total_buttons = '+str(self.total_buttons))
        row = math.floor(self.total_buttons / self.buttons_in_row)
        #print(row)
        column = self.total_buttons - row*self.buttons_in_row

        print(file)

        img = Image.open(file)
        img = img.resize((width,height))
        photoImg =  ImageTk.PhotoImage(img)
        self.images_array.append(photoImg)

        button = tk.Button(self.frame, image=photoImg, width=width, height=height)
        button.bind("<Button-1>", self.leftClick)
        button.grid(row=row, column=column)

        self.orig_color = button.cget("background")
        #button.pack(side=LEFT)

        self.total_buttons += 1
        
        self.buttons_array.append(button)

    def leftClick(self, event):        
        if self.mode == self.MODE_SELECT:
            for b in self.buttons_array:
                b.configure(bg=self.orig_color)
        event.widget.configure(bg="green")

    def deleteSelectedButton(self):
        temp = []
        for b in self.buttons_array:
            if b.cget("background") != self.orig_color:
                b.destroy()
            else:
                temp.append(b)

        self.total_buttons = 0
        for button in temp:
            row = math.floor(self.total_buttons / self.buttons_in_row)        
            column = self.total_buttons - row*self.buttons_in_row
            self.total_buttons += 1
            button.grid(row=row, column=column)

        self.buttons_array = temp



    def clear(self):
        for b in self.buttons_array:
            b.destroy()
        self.total_buttons = 0
        self.buttons_array = []