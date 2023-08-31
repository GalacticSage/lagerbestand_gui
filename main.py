import customtkinter as ctk
from lagerbestand_core import core
import func as f

# Read the local JSON file path from "selected_json.txt"
local_json = f.read_selected_directory("selected_json.txt")

# Define the LagerApp class
class LagerApp:
    def __init__(self):
        # Initialize the tkinter window
        self.window = ctk.CTk()
        self.window.title("Lagerbestand GUI")
        self.window.geometry("800x700")
        self.window.grid_columnconfigure((0, 1), weight=1)
        self.window.grid_rowconfigure((0, 1, 2), weight=1)

        # Read JSON data from the local JSON file
        self.data = core.read_json(local_json)

        # Load options from the JSON data
        self.load_options(self.data)

        # Create frames for layout
        self.create_frames()

        # Create widgets within the frames
        self.create_widgets(self.data)

    def load_options(self, data):
        # Load available options from the JSON data
        self.options = list(data.keys())

    def create_frames(self):
        # Create various frames for organizing widgets
        self.frame_in = self.create_frame(0, 0)
        self.frame_out = self.create_frame(0, 1)
        self.frame_view = self.create_frame(1, 0)
        self.frame_export = self.create_frame(1, 1)
        self.frame_view_output = self.create_ScrollableFrame(2, 0, 2)

    def create_frame(self, row, column):
        # Create a frame within the window
        frame = ctk.CTkFrame(self.window)
        frame.grid(row=row, column=column, padx=10, pady=(10, 0), sticky="nsew")
        return frame

    def create_ScrollableFrame(self, row, column, columnspan):
        # Create a scrollable frame within the window
        frame = ctk.CTkScrollableFrame(self.window)
        frame.grid(row=row, column=column, columnspan=columnspan, padx=10, pady=(10, 0), sticky="nsew")
        return frame

    def create_widgets(self, data):
        # Create input, output, view, and export sections
        self.create_input_section()
        self.create_output_section()
        self.create_view_section(data)
        self.create_export_section(data)

    def apply_add_quantity(self):
        # Get the selected item and quantity to add
        selected_item = self.input_optionmenu.get()
        qty_to_add = self.input_quantity.get("1.0", "end-1c")

        # Check if the quantity to add is numeric
        if self.is_numeric(qty_to_add):
            # Increase the quantity in the data dictionary
            core.increase_quantity(local_json, self.data, selected_item, int(qty_to_add))
            # Display a success message
            self.show_success_popup(f"Added {qty_to_add} of '{selected_item}' to the inventory.")
        else:
            self.show_error_popup("Quantity is not a number")

    # Update the create_input_section method to add the "Add Quantity" button
    def create_input_section(self):
        # Create widgets for the input section
        label = self.create_label(self.frame_in, "IN")
        self.input_optionmenu = self.create_option_menu(self.frame_in, self.options)
        qty_label = self.create_label(self.frame_in, "QTY", font=("Arial", 12))
        self.input_quantity = self.create_textbox(self.frame_in, 1, 100, "1-100")
        apply_button = self.create_button(self.frame_in, "Add Quantity", self.apply_add_quantity)

    def apply_decrease_quantity(self):
        # Get the selected item and quantity to decrease
        selected_item = self.output_optionmenu.get()
        qty_to_decrease = self.output_quantity.get("1.0", "end-1c")

        # Check if the quantity to decrease is numeric
        if self.is_numeric(qty_to_decrease):
            # Decrease the quantity in the data dictionary
            core.decrease_quantity(local_json, self.data, selected_item, int(qty_to_decrease))
            # Display a success message
            self.show_success_popup(f"Decreased {qty_to_decrease} of '{selected_item}' from the inventory.")
        else:
            self.show_error_popup("Quantity is not a number")


    # Update the create_output_section method to add the "Decrease Quantity" button
    def create_output_section(self):
        # Create widgets for the output section
        label = self.create_label(self.frame_out, "OUT")
        self.output_optionmenu = self.create_option_menu(self.frame_out, self.options)
        qty_label = self.create_label(self.frame_out, "QTY", font=("Arial", 12))
        self.output_quantity = self.create_textbox(self.frame_out, 1, 100, "1-100")
        apply_button = self.create_button(self.frame_out, "Decrease Quantity", self.apply_decrease_quantity)

    def create_view_section(self, data):
        # Create widgets for the view section
        view_button = self.create_button(self.frame_view, "View", lambda: self.create_view_output(data))

    def create_export_section(self, data):
        # Create widgets for the export section
        export_button = self.create_button(self.frame_export, "Export", lambda: core.export_to_excel(data))

    def create_view_output(self, data):
        # Create a label to display formatted data in the view section
        view_output = self.create_label(self.frame_view_output, core.formatted_data(data), font=("Arial", 20))

    def create_label(self, parent_frame, text, font=("Arial", 20)):
        # Create a label widget
        label = ctk.CTkLabel(parent_frame, text=text, font=font)
        label.pack(pady=10)
        return label

    def create_option_menu(self, parent_frame, values):
        # Create an option menu widget
        optionmenu = ctk.CTkOptionMenu(parent_frame, values=values, command=self.optionmenu_callback)
        optionmenu.pack(pady=10)
        return optionmenu

    def create_textbox(self, parent_frame, height, width, initial_text):
        # Create a textbox widget
        textbox = ctk.CTkTextbox(parent_frame, height=height, width=width)
        textbox.insert(0.0, initial_text)
        textbox.pack(pady=2)
        return textbox

    def create_button(self, parent_frame, text, command):
        # Create a button widget
        button = ctk.CTkButton(parent_frame, text=text, command=command)
        button.pack()
        return button

    def apply_input(self):
        # Handle the input section's Apply button click event
        qty = self.input_quantity.get("1.0", "end-1c")
        if self.is_numeric(qty):
            print("Apply Button clicked:", qty)
        else:
            self.show_error_popup("QTY is not a number")

    def is_numeric(self, value):
        # Check if a value is numeric
        try:
            # Attempt to convert the value to an integer
            int_value = int(value)
            return True
        except ValueError:
            try:
                # Attempt to convert the value to a float
                float_value = float(value)
                return True
            except ValueError:
                return False


    def optionmenu_callback(self, choice):
        # Handle OptionMenu dropdown selection event
        print("OptionMenu dropdown clicked:", choice)

    def show_error_popup(self, message):
        # Create and display an error popup
        error_popup = ctk.CTkToplevel(self.window)
        error_popup.geometry("300x100")
        error_popup.title("ERROR")
        error_popup.attributes("-top", True)  # Set always on top

        error_label = ctk.CTkLabel(error_popup, text=message, font=("Arial", 20))
        error_label.pack(pady=10)

        ok_button = ctk.CTkButton(error_popup, text="OK", command=error_popup.destroy)
        ok_button.pack()

    def show_success_popup(self, message):
        # Create and display a success popup
        success_popup = ctk.CTkToplevel(self.window)
        success_popup.geometry("700x100")
        success_popup.title("SUCCESS")
        success_popup.attributes("-top", True)  # Set always on top

        success_label = ctk.CTkLabel(success_popup, text=message, font=("Arial", 20))
        success_label.pack(pady=10)

        ok_button = ctk.CTkButton(success_popup, text="OK", command=success_popup.destroy)
        ok_button.pack()

        # Schedule the success_popup window to be destroyed after 5000 milliseconds (5 seconds)
        success_popup.after(5000, success_popup.destroy)

    def run(self):
        # Start the main GUI loop
        self.window.mainloop()

# Run the application if this script is the main module
if __name__ == "__main__":
    app = LagerApp()
    app.run()
