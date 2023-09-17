# Import the tkinter module and customtkinter module with an alias ctk
import tkinter as tk
import customtkinter as ctk

# Import the IntSpinbox class from intSpinbox module
from intSpinbox import IntSpinbox

# Create a class named Gui
class Gui:

    # Static method to create a custom GUI window with specified title, geometry, column, and row settings
    @staticmethod
    def createRootCTK(title, geometry, column, row):
        # Create a basic GUI window using customtkinter
        root = ctk.CTk()
        root.title(title)
        root.geometry(geometry)

        # Configure column and row weights based on the provided arguments
        if isinstance(column, int):
            root.columnconfigure(column, weight=1)
        elif isinstance(column, list):
            for col in column:
                root.columnconfigure(col, weight=1)

        if isinstance(row, int):
            root.rowconfigure(row, weight=1)
        elif isinstance(row, list):
            for r in row:
                root.rowconfigure(r, weight=1)

        return root

    # Method to create a frame within a given root window, with specified row and column
    def createFrame(root, row, column):
        # Create a frame using customtkinter within the window
        frame = ctk.CTkFrame(root)
        frame.grid(row=row, column=column, padx=10, pady=(10, 0), sticky="nsew")
        return frame

    # Method to create a scrollable frame within a given root window, with specified row, column, and column span
    def createScrollabelFrame(root, row, column, columnspan):
        # Create a scrollable frame using customtkinter within the window
        frame = ctk.CTkScrollableFrame(root)
        frame.grid(row=row, column=column, columnspan=columnspan, padx=10, pady=(10, 0), sticky="nsew")
        return frame

    # Method to create a label widget within a parent frame, with specified text and font
    def createLabel(parentFrame, text, font=("Arial", 20)):
        # Create a label widget using customtkinter
        label = ctk.CTkLabel(parentFrame, text=text, font=font)
        label.pack(pady=10)
        return label

    # Method to create an option menu widget within a parent frame, with provided data
    def createOptionMenu(parentFrame, data):
        # Create an option menu widget using customtkinter
        optionMenu = ctk.CTkOptionMenu(parentFrame, values=data)
        optionMenu.pack(pady=10)
        return optionMenu

    # Method to create an IntSpinbox widget within a parent frame, with specified width and step size
    def createSpinbox(parentFrame, width, step_size):
        # Create an IntSpinbox widget using the imported IntSpinbox class
        intSpinbox = IntSpinbox(parentFrame, width=width, step_size=step_size)
        intSpinbox.pack(pady=10)
        return intSpinbox

    # Method to create a button widget within a parent frame, with specified text and command
    def createButton(parentFrame, text, command):
        # Create a button widget using customtkinter
        button = ctk.CTkButton(parentFrame, text=text, command=command)
        button.pack(pady=10)
        return button