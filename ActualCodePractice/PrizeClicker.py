import tkinter as tk
from tkinter import Toplevel

# Function to create a new window when the button is clicked
def open_prize_window():
    # Create a new top-level window (a secondary window)
    prize_window = Toplevel(root)
    prize_window.title("Prize Window")
    prize_window.geometry("300x200")  # Size of the prize window

    # Create a label inside the prize window with the prize message
    prize_label = tk.Label(prize_window, text="Congratulations! You won a prize!", font=("Arial", 14))
    prize_label.pack(pady=40)

    # Create a button to close the prize window
    close_button = tk.Button(prize_window, text="Close", command=prize_window.destroy)
    close_button.pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

# Create a label on the main window
label = tk.Label(root, text="Click the button to win a prize!", font=("Arial", 14))
label.pack(pady=40)

# Create a button on the main window to open the prize window
button = tk.Button(root, text="Click Me!", font=("Arial", 14), command=open_prize_window)
button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
