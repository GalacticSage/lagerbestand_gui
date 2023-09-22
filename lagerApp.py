# Import the Gui and Util classes from respective modules
from gui import Gui
from util import Util


# Define a class named LagerApp
class LagerApp:
    lang = 'en_US'

    translations = Util.load_translations(lang)

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

        self.createRootAndFrames()
        self.populateFrames()

    def createRootAndFrames(self):
        # Create the main GUI window and frames
        self.root = Gui.createRootCTK(self.windowTitle, self.windowGeometry, self.windowColumn, self.windowRow)
        self.frameIn = Gui.createFrame(self.root, 0, 0)
        self.frameOut = Gui.createFrame(self.root, 0, 1)
        self.frameButtonsLeft = Gui.createFrame(self.root, 1, 0)
        self.frameButtonsRight = Gui.createFrame(self.root, 1, 1)
        self.frameView = Gui.createScrollabelFrame(self.root, 2, 0, 2)

    def populateFrames(self):
        # FrameIn
        Gui.createLabel(self.frameIn, Util.translate(self.translations, "IN"))
        inOptionMenu = Gui.createOptionMenu(self.frameIn, self.options)
        Gui.createLabel(self.frameIn, Util.translate(self.translations, "QTY"))
        inQtySpinbox = Gui.createSpinbox(self.frameIn, 125, 1)
        Gui.createButton(self.frameIn, Util.translate(self.translations, "Increase"), lambda: print(inQtySpinbox.get()))

        # FrameOut
        Gui.createLabel(self.frameOut, Util.translate(self.translations, "OUT"))
        outOptionMenu = Gui.createOptionMenu(self.frameOut, self.options)
        Gui.createLabel(self.frameOut, Util.translate(self.translations, "QTY"))
        outQtySpinbox = Gui.createSpinbox(self.frameOut, 125, 1)
        Gui.createButton(self.frameOut, Util.translate(self.translations, "Decrease"),
                         lambda: print(outQtySpinbox.get()))

        # FrameButtonsLeft
        Gui.createButton(self.frameButtonsLeft, Util.translate(self.translations, "View"), lambda: print("View"))
        Gui.createButton(self.frameButtonsLeft, Util.translate(self.translations, "Add"), lambda: print("Add Product"))
        Gui.createButton(self.frameButtonsLeft, Util.translate(self.translations, "Remove"),
                         lambda: print("Remove Product"))

        # FrameButtonsRight
        Gui.createButton(self.frameButtonsRight, Util.translate(self.translations, "Settings"),
                         lambda: self.settingsMenu())
        Gui.createButton(self.frameButtonsRight, Util.translate(self.translations, "Reload"), lambda: print("Reload"))
        Gui.createButton(self.frameButtonsRight, Util.translate(self.translations, "Inventory Check"),
                         lambda: print("Inventory Check"))
    def settingsMenu(self):
        settingsPopup = Gui.createPopup(self.frameButtonsRight, "Settings", "400x400")
        Gui.createLabel(settingsPopup, Util.translate(self.translations, "Language"))

    # Method to start the main GUI loop
    def run(self):
        # Start the main GUI loop
        self.root.mainloop()
