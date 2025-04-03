import tkinter as tk
from tkinter import ttk
from elements.my_canvas import MyCanvas
from elements.my_keyboard import MyKeyboard

from tabs.tab_alphabet import TabAlphabetum

PROJECT = 'default'

root = tk.Tk()
root.geometry("1024x768")

tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)


#TAB1
tab_alphabet = TabAlphabetum(tab1)
tab_alphabet.setProject(PROJECT)

#TAB2




#TABS

tabControl.add(tab1, text ='Alpabet')
tabControl.add(tab2, text ='Source text')
tabControl.add(tab3, text ='Frequency')
tabControl.pack(expand = 1, fill ="both")

root.mainloop()


