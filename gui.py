import tkinter as tk
import customtkinter as ctk


class Gui:
    @staticmethod
    def createRootCTK(title, geometry, column, row):
        # Create a basic GUI window
        root = ctk.CTk()
        root.title(title)
        root.geometry(geometry)

        # Assuming column and row are integers or lists of integers
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

    def createFrame(root, row, column):
        # Create a frame within the window
        frame = ctk.CTkFrame(root)
        frame.grid(row=row, column=column, padx=10, pady=(10, 0), sticky="nsew")
        return frame

    def createScrollabelFrame(root, row, column, columnspan):
        # Create a frame within the window
        frame = ctk.CTkScrollableFrame(root)
        frame.grid(row=row, column=column, columnspan=columnspan, padx=10, pady=(10, 0), sticky="nsew")
        return frame