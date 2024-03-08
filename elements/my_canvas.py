import tkinter as tk

class MyCanvas:

    def __init__(self, root, width, height):

        self.draw = False
        self.width = width
        self.height = height
        self.canvas = tk.Canvas(root,  width= width, height = height, bd=2, bg="white")
        self.canvas.bind("<Button-1>", self.onClick)
        self.canvas.bind("<ButtonRelease-1>", self.onRelease)
        self.canvas.bind("<Motion>", self.onMove)
        self.canvas.grid(row=0,column=0,columnspan=2)

    def setGrid(self,row,column, columnspan, rowspan):
        self.canvas.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan)

    def clear(self):
        self.canvas.delete("all")

    def save(self, file_name):
        self.canvas.postscript(file = file_name + '.eps')

    def onMove(self, event):
        if self.draw:
            self.canvas.create_oval(event.x-1, event.y-1, event.x+1, event.y+1, width = 3 )
        
        #print("Move at ["+ str(event.x)+":"+ str(event.y)+"]")

    def onClick(self, event):
        self.draw = True
        #print("clicked at ["+ str(event.x)+":"+ str(event.y)+"]")

    def onRelease(self, event):
        self.draw = False
        #print("released at ["+ str(event.x)+":"+ str(event.y)+"]")
        