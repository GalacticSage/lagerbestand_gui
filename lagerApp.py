from gui import Gui
from util import Util
class LagerApp:

    data = None
    options = None

    windowTitle = "Lager"
    windowGeometry = "800x700"
    windowColumn = [0, 1]
    windowRow = [0, 1, 2]

    def __init__(self):
        self.data, self.options = Util.loadDataAndOptions(self, "lager.json")

        self.root = Gui.createRootCTK(self.windowTitle, self.windowGeometry, self.windowColumn, self.windowRow)
        self.frameIn = Gui.createFrame(self.root, 0, 0)
        self.frameOut = Gui.createFrame(self.root, 0, 1)
        self.frameButtonsLeft = Gui.createFrame(self.root, 1, 0)
        self.frameButtonsRight = Gui.createFrame(self.root, 1, 1)
        self.frameView = Gui.createScrollabelFrame(self.root, 2, 0, 2)


    def run(self):
        # Start the main GUI loop
        self.root.mainloop()