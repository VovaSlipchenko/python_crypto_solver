import sys
import os
import inspect

import tkinter as tk
from tkinter import S,W,E,N
from PIL import Image


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from elements.my_canvas import MyCanvas
from elements.my_keyboard import MyKeyboard

class TabAlphabetum:
    def __init__(self, root):
        frame_canvas = tk.Frame(root)

        self.letters = []
        
        self.canvas = MyCanvas(frame_canvas, 100,100)
        self.canvas.setGrid(0,0,2,1)

        self.button_clear = tk.Button(frame_canvas, text = "Clear", command=self.clearCanvas)
        self.button_clear.grid(row=1,column=0, sticky=W)

        self.button_add = tk.Button(frame_canvas, text = "Add", command=self.saveLetter)
        self.button_add.grid(row=1,column=1, sticky=E)
        

        frame_canvas.grid()

        self.keyboard = MyKeyboard(root)

        

    def setProject(self, project):
        self.project = project

    def clearCanvas(self):
        self.canvas.clear()

    def saveLetter(self):

        letter_index = 1
        folder = 'projects/'+self.project+'/letters'
        isExist = os.path.exists(folder)
        if not isExist:
            os.makedirs(folder)

        letters = os.listdir(folder)
        #print(letters)

        found = True
        while found:
            found = False
            for letter in letters:
                letter = letter.replace('.png','')
                if letter == str(letter_index):
                    found = True
                    letter_index+=1

        self.canvas.save('temp')
        # use PIL to convert to PNG 
        img = Image.open('temp.eps')
        img.save(folder+'/'+str(letter_index) + '.png', 'png')

        self.clearCanvas()

        self.keyboard.addButton(letter_index, folder+'/'+str(letter_index) + '.png')

    def loadLetters():

        folder = 'projects/'+self.project+'/letters'
        isExist = os.path.exists(folder)
        if not isExist:
            os.makedirs(folder)

        letters = os.listdir(folder)

        
