import json
import customtkinter as ctk
import tkinter
from tkinter import filedialog
from datetime import datetime
import pandas as pd
import openpyxl

local_json = "lager.json"


class LagerApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Lagerbestand GUI")
        self.window.geometry("800x600")
        self.window.grid_columnconfigure((0, 1), weight=1)
        self.window.grid_rowconfigure((0, 1, 2), weight=1)

        data = self.read_json(local_json)
        self.load_options(data)
        self.create_frames()
        self.create_widgets(data)

    def read_json(self, lager_json):
        with open(lager_json, "r") as json_file:
            data = json.load(json_file)
            json_file.close()
        return data

    def load_options(self, data):
        self.options = list(data.keys())

    def view_output_func(self, data):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        formatted_data = dt_string + "\n"
        for key, value in data.items():
            formatted_key = key.replace("_", " ").replace("-", " ").title()
            formatted_data += f"{formatted_key}: {value}\n"
        return formatted_data

    def export_to_excel(self, data):
        # Construct a list of dictionaries with the desired structure
        data_list = [{"Item": key, "Quantity": value} for key, value in data.items()]

        # Create a DataFrame from the list of dictionaries
        df = pd.DataFrame(data_list)

        # Use file dialog to get the output path
        tkinter.Tk().withdraw()  # Prevents an empty tkinter window from appearing
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])

        # If the user didn't cancel the file dialog, save the DataFrame to Excel
        if file_path:
            df.to_excel(file_path, index=False)

    def create_frames(self):
        self.frame_in = self.create_frame(0, 0)
        self.frame_out = self.create_frame(0, 1)
        self.frame_view = self.create_frame(1, 0)
        self.frame_export = self.create_frame(1, 1)
        self.frame_view_output = self.create_ScrollableFrame(2, 0, 2)

    def create_frame(self, row, column, ):
        frame = ctk.CTkFrame(self.window)
        frame.grid(row=row, column=column, padx=10, pady=(10, 0), sticky="nsew")
        return frame

    def create_ScrollableFrame(self, row, column, columnspan):
        frame = ctk.CTkScrollableFrame(self.window)
        frame.grid(row=row, column=column, columnspan=columnspan, padx=10, pady=(10, 0), sticky="nsew")
        return frame

    def create_widgets(self, data):
        self.create_input_section()
        self.create_output_section()
        self.create_view_section(data)
        self.create_export_section(data)

    def create_input_section(self):
        label = self.create_label(self.frame_in, "IN")
        optionmenu = self.create_option_menu(self.frame_in, self.options)
        qty_label = self.create_label(self.frame_in, "QTY", font=("Arial", 12))
        self.input_quantity = self.create_textbox(self.frame_in, 1, 100, "1-100")
        apply_button = self.create_button(self.frame_in, "Apply", self.apply_input)

    def create_output_section(self):
        label = self.create_label(self.frame_out, "OUT")
        optionmenu = self.create_option_menu(self.frame_out, self.options)
        qty_label = self.create_label(self.frame_out, "QTY", font=("Arial", 12))
        self.output_quantity = self.create_textbox(self.frame_out, 1, 100, "1-100")
        apply_button = self.create_button(self.frame_out, "Apply", lambda: print("Hello World 2"))

    def create_view_section(self, data):
        view_button = self.create_button(self.frame_view, "View", lambda: self.create_view_output(data))

    def create_export_section(self, data):
        export_button = self.create_button(self.frame_export, "Export", lambda: self.export_to_excel(data))

    def create_view_output(self, data):
        view_output = self.create_label(self.frame_view_output, self.view_output_func(data), font=("Arial", 20))

    def create_label(self, parent_frame, text, font=("Arial", 20)):
        label = ctk.CTkLabel(parent_frame, text=text, font=font)
        label.pack(pady=10)
        return label

    def create_option_menu(self, parent_frame, values):
        optionmenu = ctk.CTkOptionMenu(parent_frame, values=values, command=self.optionmenu_callback)
        optionmenu.pack(pady=10)
        return optionmenu

    def create_textbox(self, parent_frame, height, width, initial_text):
        textbox = ctk.CTkTextbox(parent_frame, height=height, width=width)
        textbox.insert(0.0, initial_text)
        textbox.pack(pady=2)
        return textbox

    def create_button(self, parent_frame, text, command):
        button = ctk.CTkButton(parent_frame, text=text, command=command)
        button.pack()
        return button

    def apply_input(self):
        qty = self.input_quantity.get("1.0", "end-1c")
        if self.is_numeric(qty):
            print("Apply Button clicked:", qty)
        else:
            self.show_error_popup("QTY is not a number")

    def is_numeric(self, value):
        return isinstance(value, (int, float))

    def optionmenu_callback(self, choice):
        print("OptionMenu dropdown clicked:", choice)

    def show_error_popup(self, message):
        error_popup = ctk.CTkToplevel(self.window)
        error_popup.geometry("300x100")
        error_popup.title("ERROR")
        error_popup.attributes("-top", True)  # Set always on top

        error_label = ctk.CTkLabel(error_popup, text=message, font=("Arial", 20))
        error_label.pack(pady=10)

        ok_button = ctk.CTkButton(error_popup, text="OK", command=error_popup.destroy)
        ok_button.pack()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = LagerApp()
    app.run()
