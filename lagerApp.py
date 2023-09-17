# Import the Gui and Util classes from respective modules
from gui import Gui
from util import Util

# Define a class named LagerApp
class LagerApp:

    # Class-level variables for data and options
    data = None
    options = None

    # Default window properties
    windowTitle = "Lager"
    windowGeometry = "800x700"
    windowColumn = [0, 1]
    windowRow = [0, 1, 2]

    # Constructor method
    def __init__(self):
        # Load data and options using Util class method
        self.data, self.options = Util.loadDataAndOptions(self, "lager.json")

        # Create the main GUI window and frames
        self.root = Gui.createRootCTK(self.windowTitle, self.windowGeometry, self.windowColumn, self.windowRow)
        self.frameIn = Gui.createFrame(self.root, 0, 0)
        self.frameOut = Gui.createFrame(self.root, 0, 1)
        self.frameButtonsLeft = Gui.createFrame(self.root, 1, 0)
        self.frameButtonsRight = Gui.createFrame(self.root, 1, 1)
        self.frameView = Gui.createScrollabelFrame(self.root, 2, 0, 2)

        # Create labels, option menu, spinbox widgets and buttons within the frames
        Gui.createLabel(self.frameIn, "IN")
        inOptionMenu = Gui.createOptionMenu(self.frameIn, self.options)
        Gui.createLabel(self.frameIn, "QTY")
        inQtySpinbox = Gui.createSpinbox(self.frameIn, 125, 1)
        Gui.createButton(self.frameIn, "ADD", lambda: print(inQtySpinbox.get()))

    # Method to start the main GUI loop
    def run(self):
        # Start the main GUI loop
        self.root.mainloop()
