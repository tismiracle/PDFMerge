import window
import merger


class Controller:
    def __init__(self):
        
        self.app = window.Window()
        self.mrg = merger.Merger(self.app.root)
        self.btn_commands()
        self.app.mainloop()
        

    def btn_commands(self):
        btns = self.app.buttons_dict
        print(btns)
        btns.get("selected_files").config(command=lambda: [self.app.show_progress_bar(), self.get_from_dialogbox()])
        btns.get("all_files").config(command=lambda: self.merge_all_files())

    def merge_all_files(self):

        self.mrg.merge_all_files(self.app.prgs_bar, self.app.show_progress_bar)

    def get_from_dialogbox(self):
        
        self.paths = self.app.dialogbox()
        self.mrg.merge_files(self.paths, self.app.prgs_bar, self.app.show_progress_bar)
        print(self.paths)



        
application = Controller()
