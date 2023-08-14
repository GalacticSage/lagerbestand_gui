import json
import customtkinter as ctk


# Callback function for the option menu
def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

def toplevel_error(message):
    toplevel = ctk.CTkToplevel(window)
    toplevel.geometry("300x100")
    toplevel.title("ERROR")
    error_qty_is_not_num = ctk.CTkLabel(toplevel, text=message, font=("Arial", 20))
    error_qty_is_not_num.pack(pady=10)
    button_error = ctk.CTkButton(toplevel, text="OK", command=toplevel.destroy)
    button_error.pack()

def is_number(value):
    return isinstance(value, (int, float))
def get_qty_in():
    return number_in.get("1.0", "end-1c")

def apply_in():
    qty = get_qty_in()
    if is_number(qty):
        print("Apply Button 1 clicked:", qty)
    else:
        toplevel_error("QTY is not a number")





# Load the JSON file to get the options
with open("lager.json", "r") as json_file:
    data = json.load(json_file)
    options = list(data.keys())  # Extract keys from the JSON as options

# Create the window
window = ctk.CTk()
window.title("Lagerbestand GUI")
window.geometry("800x600")
window.grid_columnconfigure((0, 1), weight=1)
window.grid_rowconfigure((0, 1, 2), weight=1)

# Create frames to organize the layout
frame_in = ctk.CTkFrame(window)
frame_in.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

frame_out = ctk.CTkFrame(window)
frame_out.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsew")

frame_view = ctk.CTkFrame(window)
frame_view.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsew")

frame_export = ctk.CTkFrame(window)
frame_export.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="nsew")

# Create widgets and add them to frames

# Frame for IN section
label = ctk.CTkLabel(frame_in, text="IN", font=("Arial", 20))
label.pack(pady=10)

# Show the options in the OptionMenu
optionmenu_in = ctk.CTkOptionMenu(frame_in, values=options, command=optionmenu_callback)
optionmenu_in.pack(pady=10)

qty_in = ctk.CTkLabel(frame_in, text="QTY", font=("Arial", 12))
qty_in.pack(pady=2)

number_in = ctk.CTkTextbox(frame_in, height=1, width=100)
number_in.insert(0.0, "1-100")
number_in.pack(pady=2)

button = ctk.CTkButton(frame_in, text="Apply", command=apply_in)
button.pack()

# Frame for OUT section
label2 = ctk.CTkLabel(frame_out, text="OUT", font=("Arial", 20))
label2.pack(pady=10)

# Show the options out the OptionMenu
optionmenu_out = ctk.CTkOptionMenu(frame_out, values=options, command=optionmenu_callback)
optionmenu_out.pack(pady=10)

qty_out = ctk.CTkLabel(frame_out, text="QTY", font=("Arial", 12))
qty_out.pack(pady=2)

number_out = ctk.CTkTextbox(frame_out, height=1, width=100)
number_out.insert(0.0, "1-100")
number_out.pack(pady=2)

button2 = ctk.CTkButton(frame_out, text="Apply", command=lambda: print("Hello World 2"))
button2.pack()

# Frame for view section
view = ctk.CTkButton(frame_view, text="View", command=lambda: print("View Button"))
view.pack()

# Frame for export section
export = ctk.CTkButton(frame_export, text="Export", command=lambda: print("Export Button"))
export.pack()

# Start the GUI event loop
window.mainloop()
