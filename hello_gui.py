#example_gui.py
import tkinter as tk # Tk interface
class FirstGUI:
    def __init__(self):
        # display the main window
        self.main_window = tk.Tk() # creates a dialogue box # root
        self.main_window.configure(bg = 'white') # background
        self.main_window.title('My First GUI')
        self.main_window.geometry('300x200') # size of the window
        self.set_label()
        # continuously display the main window
        tk.mainloop()
    def set_label(self):
        # create label widgets
        self.__hello_label = tk.Label(self.main_window, text = 'Hello class!', fg = 'green') # fg - foreground
        self.__my_label = tk.Label(self.main_window, text = 'This is my first GUI ', bg = 'yellow', fg = 'red') # fore-ground
        #self.new_label = tk.Label(self.main_window, text = 'aaa')
        # pack the labels 
        self.__hello_label.pack(side = 'left')
        self.__my_label.pack(side = 'right')
        #self.new_label.pack()       
# create an instance
my_gui = FirstGUI()
