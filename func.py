import tkinter as tk
from tkinter import filedialog

def read_selected_directory(filename):
    try:
        with open(filename, 'r') as txt_file:
            directory = txt_file.read()
            return directory  # Remove leading/trailing whitespace, if any
    except FileNotFoundError:
        select_json_and_save()  # Handle the case where the file doesn't exist
        return read_selected_directory(filename)  # Try again after the user has selected a file
def select_json_and_save():
    def select_json_file():
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])

        if file_path:
            with open('selected_json.txt', 'w') as txt_file:
                txt_file.write(file_path)
            status_label.config(text=f"Selected JSON file: {file_path}")

    def save_and_close():
        root.destroy()  # Close the GUI window

    # Create a basic GUI window
    root = tk.Tk()
    root.title("JSON File Selector")

    # Set an appropriate window size
    window_width = 400
    window_height = 150
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create and configure a label to display the status
    status_label = tk.Label(root, text="Select a JSON file:")
    status_label.pack(pady=10, padx=10)

    # Create a button to open the file dialog
    select_button = tk.Button(root, text="Select JSON File", command=select_json_file)
    select_button.pack(pady=5, padx=10)

    # Create a button to save and close the window
    save_button = tk.Button(root, text="Save", command=save_and_close)
    save_button.pack(pady=5, padx=10)

    # Start the main GUI loop
    root.mainloop()

