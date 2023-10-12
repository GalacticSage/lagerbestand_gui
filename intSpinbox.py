import customtkinter as ctk

# Create a custom IntSpinbox class that inherits from customtkinter.CTkFrame
class IntSpinbox(ctk.CTkFrame):

    # Initialize the IntSpinbox with default and optional parameters
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: int = 1,
                 command: callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        # Set step size and command function for the spinbox
        self.step_size = step_size
        self.command = command

        # Configure the frame appearance
        self.configure(fg_color=("gray78", "gray28"))  # Set frame color

        # Set grid configuration for layout
        self.grid_columnconfigure((0, 2), weight=0)  # Buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # Entry expands

        # Create and place buttons and entry widget
        self.subtract_button = ctk.CTkButton(self, text="-", width=height-6, height=height-6,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = ctk.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = ctk.CTkButton(self, text="+", width=height-6, height=height-6,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # Set a default value for the entry widget
        self.entry.insert(0, "0")

    # Callback function for the add button
    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    # Callback function for the subtract button
    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = max(0, int(self.entry.get()) - self.step_size)  # Ensure value doesn't go below 0
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    # Get the current value in the entry widget
    def get(self) -> int:
        try:
            return int(self.entry.get())
        except ValueError:
            return 0

    # Set the value of the entry widget
    def set(self, value: int):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(int(value)))
