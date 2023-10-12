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
    labelView = None

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
        Gui.createButton(self.frameOut, Util.translate(self.translations, "Decrease"), lambda: core.decrease_quantity(self.lagerJsonPath, self.productData, outOptionMenu.get(), int(outQtySpinbox.get())))

        # FrameButtonsLeft
        Gui.createButton(self.frameButtonsLeft, Util.translate(self.translations, "View"), lambda: self.showItemsInView())
        Gui.createButton(self.frameButtonsLeft, Util.translate(self.translations, "Add"), lambda: self.showAddItem())
        Gui.createButton(self.frameButtonsLeft, Util.translate(self.translations, "Remove"),
                         lambda: self.showRemoveItem())

        # FrameButtonsRight
        Gui.createButton(self.frameButtonsRight, Util.translate(self.translations, "Settings"),
                         lambda: self.settingsMenu())
        Gui.createButton(self.frameButtonsRight, Util.translate(self.translations, "Reload"), lambda: self.reloadGUI())
        Gui.createButton(self.frameButtonsRight, Util.translate(self.translations, "Inventory Check"),
                         lambda: self.showInventoryCheck())
        
        # FrameView
        self.labelView = Gui.createLabel(self.frameView, "")

    def settingsMenu(self):
        self.langData, self.langOptions = Util.loadDataAndOptions(self, self.availableLanguagesJsonPath, True)
        settingsPopup = Gui.createPopup(self.frameButtonsRight, "Settings", "400x400")
        Gui.createLabel(settingsPopup, Util.translate(self.translations, "Language"))
        langOptionMenu = Gui.createOptionMenu(settingsPopup, self.langOptions)
        Gui.createButton(settingsPopup, Util.translate(self.translations, "Apply"),
                         lambda: [Util.setLanguage(self, langOptionMenu.get()), settingsPopup.destroy()])
        Gui.createLabel(settingsPopup, Util.translate(self.translations, "Reset Settings"))
        Gui.createButton(settingsPopup, Util.translate(self.translations, "Reset"),
                         lambda: self.resetSettings())
        Gui.createLabel(settingsPopup, Util.translate(self.translations, "Export"))
        Gui.createButton(settingsPopup, Util.translate(self.translations, "Export as Excel"), lambda: [core.export_to_excel(self.productData, filePath=Gui.selectExcelSavePath(self)), settingsPopup.destroy()])

    def showItemsInView(self):
        self.labelView.configure(text=core.formatted_data(self.productData))
    
    def showAddItem(self):
        popup = Gui.createPopup(self.root, Util.translate(self.translations, "Add Item"), "400x400")
        Gui.createLabel(popup, Util.translate(self.translations, "Item Name"))
        itemNameEntry = Gui.createEntry(self, popup)
        Gui.createLabel(popup, Util.translate(self.translations, "QTY"))
        addItemQtySpinbox = Gui.createSpinbox(popup, 125, 1)
        Gui.createButton(popup, Util.translate(self.translations, "Add"), lambda: [core.add_item(self.lagerJsonPath, self.productData, itemNameEntry.get(), int(addItemQtySpinbox.get())), popup.destroy()])
        
    def showRemoveItem(self):
        popup = Gui.createPopup(self.root, Util.translate(self.translations, "Remove Item"), "400x400")
        Gui.createLabel(popup, Util.translate(self.translations, "Item Name"))
        removeItemOptionMenu = Gui.createOptionMenu(popup, self.productOptions)
        Gui.createButton(popup, Util.translate(self.translations, "Remove"), lambda: [core.remove_item(self.lagerJsonPath, self.productData, removeItemOptionMenu.get()), popup.destroy()])
    
    def showInventoryCheck(self):
        self.labelView.configure(text=core.formatted_data(Util.filter_values_under_five(self, self.productData)))
        
    
    def reloadGUI(self):
        # Close the current GUI
        self.root.destroy()

        # Create a new instance of LagerApp and run it
        app = LagerApp()
        app.run()
        
    
    # Method to start the main GUI loop
    def run(self):
        # Start the main GUI loop
        self.root.mainloop()
