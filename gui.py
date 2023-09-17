import tkinter as tk
import customtkinter as ctk

class Gui:
    def createRootCTK(title, geometry, column, row):
        # Create a basic GUI window
        root = ctk.CTk()
        root.title(title)
        root.geometry(geometry)
        root.columnconfigure(column, weight=1)
        root.rowconfigure(row, weight=1)
        return root
