import tkinter
from tkinter.ttk import Progressbar
from tkinter import filedialog

class Window():
    def __init__(self):
        self.root = self.new_window()
        self.buttons_dict = self.buttons()

        self.grid_btns()
        self.progress_bar()
        


    def new_window(self):
        root = tkinter.Tk()
        root.geometry("200x200")
        return root

    def mainloop(self):
        self.root.mainloop()

    def buttons(self):
        selected_btn = tkinter.Button(master=self.root, text="merge selected files")
        all_btn = tkinter.Button(master=self.root, text="merge all files in folder")

        buttons = {"selected_files":selected_btn, "all_files":all_btn}
        return buttons

    def grid_btns(self):
        for key in self.buttons_dict.keys():
            button = self.buttons_dict.get(key)            
            button.pack(expand=True, fill="both")


    def dialogbox(self):
        paths = filedialog.askopenfilenames()
        return paths

    def progress_bar(self):
        self.prgs_bar = Progressbar(self.root, orient="horizontal", mode = 'determinate')
        self.root.update()

    def show_progress_bar(self):
        self.prgs_bar.pack(expand=True, fill=tkinter.BOTH)



         


