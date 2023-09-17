from gui import Gui
class LagerApp:
    def __init__(self):
        self.root = Gui.createRootCTK("Lager", "800x700", 0, 0)


    def run(self):
        # Start the main GUI loop
        self.root.mainloop()