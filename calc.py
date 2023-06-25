import tkinter as tk
from tkinter import ttk, messagebox
import math


def on_shape_selected(event):
    # Clear existing widgets in dimensions_frame
    for widget in dimensions_frame.winfo_children():
        widget.destroy()

    # Based on the selected shape, add appropriate input fields for dimensions
    global dimension_entry
    shape = shape_combobox.get()
    if shape == "Circle":
        # For circle, ask for radius
        radius_label = ttk.Label(dimensions_frame, text="Radius:")
        radius_label.pack()
        dimension_entry = ttk.Entry(dimensions_frame)
        dimension_entry.pack()
    elif shape == "Square" or shape == "Hexagon":
        # For square and hexagon, ask for side length
        side_label = ttk.Label(dimensions_frame, text="Side length:")
        side_label.pack()
        dimension_entry = ttk.Entry(dimensions_frame)
        dimension_entry.pack()
    elif shape == "Triangle":
        # For triangle, ask for side length
        side_label = ttk.Label(dimensions_frame, text="Side length (equilateral):")
        side_label.pack()
        dimension_entry = ttk.Entry(dimensions_frame)
        dimension_entry.pack()


def on_calculate_button_click():
    # This function is called when the calculate button is clicked.
    # Perform the selected calculation for the selected shape.
    shape = shape_combobox.get()
    calculation = calculation_combobox.get()
    try:
        dimension = float(dimension_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for dimension")
        return

    if shape == "Circle":
        if calculation == "Area":
            result = math.pi * dimension ** 2
        else:
            result = 2 * math.pi * dimension
    elif shape == "Square":
        if calculation == "Area":
            result = dimension ** 2
        else:
            result = 4 * dimension
    elif shape == "Hexagon":
        if calculation == "Area":
            result = (3 * math.sqrt(3) * dimension ** 2) / 2
        else:
            result = 6 * dimension
    elif shape == "Triangle":
        if calculation == "Area":
            result = (math.sqrt(3) / 4) * dimension ** 2
        else:
            result = 3 * dimension

    messagebox.showinfo("Result", f"The {calculation} of the {shape} is {result:.2f}")


# Create the main window
root = tk.Tk()
root.title("GeoCalc")

# Create a label for shape selection
shape_label = ttk.Label(root, text="Select a shape:")
shape_label.pack()

# Create a combobox for shape selection
shape_combobox = ttk.Combobox(root, values=["Circle", "Square", "Hexagon", "Triangle"])
shape_combobox.bind("<<ComboboxSelected>>", on_shape_selected)
shape_combobox.pack()

# Create a frame to hold dimension input fields
dimensions_frame = ttk.Frame(root)
dimensions_frame.pack()

# Create a label for calculation selection
calculation_label = ttk.Label(root, text="Select a calculation:")
calculation_label.pack()

# Create a combobox for calculation selection
calculation_combobox = ttk.Combobox(root, values=["Area", "Perimeter"])
calculation_combobox.pack()

# Create a calculate button
calculate_button = ttk.Button(root, text="Calculate", command=on_calculate_button_click)
calculate_button.pack()

# Run the main loop
root.mainloop()
