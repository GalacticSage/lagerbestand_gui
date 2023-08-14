import json
import customtkinter as ctk

class LagerApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Lagerbestand GUI")
        self.window.geometry("800x600")
        self.window.grid_columnconfigure((0, 1), weight=1)
        self.window.grid_rowconfigure((0, 1, 2), weight=1)

        self.load_options()
        self.create_frames()
        self.create_widgets()

    def load_options(self):
        with open("lager.json", "r") as json_file:
            data = json.load(json_file)
            self.options = list(data.keys())

    def create_frames(self):
        self.frame_in = self.create_frame(0, 0)
        self.frame_out = self.create_frame(0, 1)
        self.frame_view = self.create_frame(1, 0)
        self.frame_export = self.create_frame(1, 1)

    def create_frame(self, row, column):
        frame = ctk.CTkFrame(self.window)
        frame.grid(row=row, column=column, padx=10, pady=(10, 0), sticky="nsew")
        return frame

    def create_widgets(self):
        self.create_input_section()
        self.create_output_section()
        self.create_view_section()
        self.create_export_section()

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

    def create_view_section(self):
        view_button = self.create_button(self.frame_view, "View", lambda: print("View Button"))

    def create_export_section(self):
        export_button = self.create_button(self.frame_export, "Export", lambda: print("Export Button"))

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

        error_label = ctk.CTkLabel(error_popup, text=message, font=("Arial", 20))
        error_label.pack(pady=10)

        ok_button = ctk.CTkButton(error_popup, text="OK", command=error_popup.destroy)
        ok_button.pack()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = LagerApp()
    app.run()
