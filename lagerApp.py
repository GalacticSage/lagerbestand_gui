# Import the Gui and Util classes from respective modules
from gui import Gui
from util import Util
from lagerbestand_core import lagerbestand_core as core

# Define a class named LagerApp
class LagerApp:
    # Class-level variables
    settingsJsonPath = "settings.json"
    lagerJsonPath = None
    availableLanguagesJsonPath = "locales/available_languages.json"
    productData = None
    productOptions = None
    settingsData = None
    langData = None
    langOptions = None
    translations = None
    lang = None

    # Default window properties
    windowTitle = "Lager"
    windowGeometry = "800x700"
    windowColumn = [0, 1]
    windowRow = [0, 1, 2]

    # Constructor method
    def __init__(self):
        self.loadSettings()
        self.loadTranslations()
        self.createRootAndFrames()
        self.populateFrames()


    def loadSettings(self):
        self.settingsData = Util.loadData(self, self.settingsJsonPath)
        self.lang = self.settingsData['Language']
        self.lagerJsonPath = self.settingsData['LagerJsonPath']
        if self.lagerJsonPath == "" or self.lagerJsonPath is None:
            self.selectJsonAndSave()

    def resetSettings(self):
        self.settingsData['Language'] = "en_US"
        self.settingsData['LagerJsonPath'] = ""
        core.write_json(self.settingsData, self.settingsJsonPath)
        restetPopup = Gui.createPopup(self.frameButtonsRight, Util.translate(self.translations, "Close the app"), "600x100")
        Gui.createLabel(restetPopup, Util.translate(self.translations, "Close the app and restart it to apply the changes."))
        Gui.createButton(restetPopup, Util.translate(self.translations, "Close"), lambda: self.root.destroy())
        
    def selectJsonAndSave(self):
        self.lagerJsonPath = Gui.selectJsonPath(self)
        self.settingsData['LagerJsonPath'] = self.lagerJsonPath
        core.write_json(self.settingsData, self.settingsJsonPath)

    def loadTranslations(self):
        self.translations = Util.loadTranslations(self.lang)

    def createRootAndFrames(self):
        # Create the main GUI window and frames
        self.root = Gui.createRootCTK(self.windowTitle, self.windowGeometry, self.windowColumn, self.windowRow)
        self.frameIn = Gui.createFrame(self.root, 0, 0)
        self.frameOut = Gui.createFrame(self.root, 0, 1)
        self.frameButtonsLeft = Gui.createFrame(self.root, 1, 0)
        self.frameButtonsRight = Gui.createFrame(self.root, 1, 1)
        self.frameView = Gui.createScrollabelFrame(self.root, 2, 0, 2)

    def populateFrames(self):
        self.productData, self.productOptions = Util.loadDataAndOptions(self, self.lagerJsonPath, True)

        # FrameIn
        Gui.createLabel(self.frameIn, Util.translate(self.translations, "IN"))
        inOptionMenu = Gui.createOptionMenu(self.frameIn, self.productOptions)
        Gui.createLabel(self.frameIn, Util.translate(self.translations, "QTY"))
        inQtySpinbox = Gui.createSpinbox(self.frameIn, 125, 1)
        Gui.createButton(self.frameIn, Util.translate(self.translations, "Increase"), lambda: core.increase_quantity(self.lagerJsonPath, self.productData, inOptionMenu.get(), int(inQtySpinbox.get())))

        # FrameOut
        Gui.createLabel(self.frameOut, Util.translate(self.translations, "OUT"))
        outOptionMenu = Gui.createOptionMenu(self.frameOut, self.productOptions)
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
        self.langData, self.langOptions = Util.loadDataAndOptions(self, self.availableLanguagesJsonPath, True)
        settingsPopup = Gui.createPopup(self.frameButtonsRight, "Settings", "400x400")
        Gui.createLabel(settingsPopup, Util.translate(self.translations, "Language"))
        langOptionMenu = Gui.createOptionMenu(settingsPopup, self.langOptions)
        Gui.createButton(settingsPopup, Util.translate(self.translations, "Apply"),
                         lambda: print(langOptionMenu.get()))
        Gui.createLabel(settingsPopup, Util.translate(self.translations, "Reset Settings"))
        Gui.createButton(settingsPopup, Util.translate(self.translations, "Reset"),
                         lambda: self.resetSettings())

    # Method to start the main GUI loop
    def run(self):
        # Start the main GUI loop
        self.root.mainloop()
