import tkinter as tk
from LoginForm import LoginForm



class App(tk.Tk):
    def __init__(self, title, size):
        
        #main setup
        self.user_logged_in = False
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0],size[1])
        self.config(background="#071013")
        self.rowconfigure(1)
        self.columnconfigure(1)
        #widgets
        self.form = LoginForm(self)
        #run
        self.mainloop()


App("Online course Platform",(600,600))
