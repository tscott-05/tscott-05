import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store user credentials
accounts_file = "accounts.json"

# Load accounts from the file
def load_accounts():
    if os.path.exists(accounts_file):
        with open(accounts_file, "r") as f:
            return json.load(f)
    else:
        return {}

# Save accounts to the file
def save_accounts(accounts):
    with open(accounts_file, "w") as f:
        json.dump(accounts, f)

# Dictionary to store username and password pairs (loaded from file)
accounts = load_accounts()

# Function to handle account registration
def register_account(username, password):
    if username in accounts:
        messagebox.showerror("Registration Failed", "Username already exists. Please choose a different username.")
    else:
        accounts[username] = password
        save_accounts(accounts)  # Save new account to file
        messagebox.showinfo("Registration Successful", "Account created successfully! You can now log in.")
        show_login_screen()  # After registration, show the login screen

# Function to handle login validation
def validate_login(username, password):
    if username in accounts and accounts[username] == password:
        show_game_start_screen()  # After login, show the game start screen
    else:
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

# Function to switch to the registration screen
def show_registration_screen():
    # Clear the main window
    clear_window()

    # Registration screen content
    tk.Label(main_window, text="Choose a Username", font=("Arial", 12, "bold")).pack(pady=10)
    reg_username_entry = tk.Entry(main_window, font=("Arial", 12), bd=2, relief="solid")
    reg_username_entry.pack(pady=5)

    tk.Label(main_window, text="Choose a Password", font=("Arial", 12, "bold")).pack(pady=10)
    reg_password_entry = tk.Entry(main_window, show="*", font=("Arial", 12), bd=2, relief="solid")
    reg_password_entry.pack(pady=5)

    # Registration button
    def on_register_click():
        username = reg_username_entry.get()
        password = reg_password_entry.get()
        register_account(username, password)

    register_button = tk.Button(main_window, text="Register", command=on_register_click, font=("Arial", 12, "bold"),
                                bg="#4CAF50", fg="white", relief="flat", bd=0, padx=20, pady=10)
    register_button.pack(pady=20)

    # Add a back button to go back to the main menu
    back_button = tk.Button(main_window, text="Back", command=show_main_screen, font=("Arial", 12, "bold"),
                            bg="#f44336", fg="white", relief="flat", bd=0, padx=20, pady=10)
    back_button.pack(pady=10)

# Function to switch to the login screen
def show_login_screen():
    # Clear the main window
    clear_window()

    # Login screen content
    tk.Label(main_window, text="Username", font=("Arial", 12, "bold")).pack(pady=10)
    username_entry = tk.Entry(main_window, font=("Arial", 12), bd=2, relief="solid")
    username_entry.pack(pady=5)

    tk.Label(main_window, text="Password", font=("Arial", 12, "bold")).pack(pady=10)
    password_entry = tk.Entry(main_window, show="*", font=("Arial", 12), bd=2, relief="solid")
    password_entry.pack(pady=5)

    # Login button
    def on_login_click():
        username = username_entry.get()
        password = password_entry.get()
        validate_login(username, password)

    login_button = tk.Button(main_window, text="Login", command=on_login_click, font=("Arial", 12, "bold"),
                             bg="#4CAF50", fg="white", relief="flat", bd=0, padx=20, pady=10)
    login_button.pack(pady=20)

    # Add a back button to go back to the main menu
    back_button = tk.Button(main_window, text="Back", command=show_main_screen, font=("Arial", 12, "bold"),
                            bg="#f44336", fg="white", relief="flat", bd=0, padx=20, pady=10)
    back_button.pack(pady=10)

# Function to show the prize screen after successful login
def show_prize_screen():
    # Clear the main window
    clear_window()

    # Prize screen content
    prize_label = tk.Label(main_window, text="Congratulations! You won a prize!", font=("Arial", 14, "bold"),
                           fg="#4CAF50")
    prize_label.pack(pady=40)

    # Add a back button to go back to the main menu
    back_button = tk.Button(main_window, text="Back", command=show_main_screen, font=("Arial", 12, "bold"),
                            bg="#f44336", fg="white", relief="flat", bd=0, padx=20, pady=10)
    back_button.pack(pady=10)

# Function to switch back to the main screen
def show_main_screen():
    # Clear the main window
    clear_window()

    # Main screen content (login or create account options)
    label = tk.Label(main_window, text="Choose an option:", font=("Arial", 14, "bold"))
    label.pack(pady=20)

    # Login button
    login_button = tk.Button(main_window, text="Login", command=show_login_screen, font=("Arial", 12, "bold"),
                             bg="#4CAF50", fg="white", relief="flat", bd=0, padx=20, pady=10)
    login_button.pack(pady=10)

    # Create Account button
    create_account_button = tk.Button(main_window, text="Create Account", command=show_registration_screen,
                                      font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="flat", bd=0,
                                      padx=20, pady=10)
    create_account_button.pack(pady=10)

# Function to show the game start screen
def show_game_start_screen():
    # Clear the main window
    clear_window()

    # Game start screen content
    start_label = tk.Label(main_window, text="Press any key to start the game!", font=("Arial", 14, "bold"))
    start_label.pack(pady=40)

    # Bind any key press to start the game
    main_window.bind("<KeyPress>", start_game)

# Function to start the game
def start_game(event):
    # Clear the window and show the game screen
    clear_window()

    # Add game content here - for now, just a placeholder
    game_label = tk.Label(main_window, text="Welcome to the game! Let's play!", font=("Arial", 16, "bold"))
    game_label.pack(pady=40)

    # Game logic will be added here

# Function to clear all widgets in the main window
def clear_window():
    for widget in main_window.winfo_children():
        widget.destroy()

# Create the root window (main application window)
root = tk.Tk()
root.title("Main Application Window")
root.geometry("400x300")
root.configure(bg="#f0f0f0")  # Background color

# Create the main window (login or create account options)
main_window = tk.Frame(root, bg="#f0f0f0")
main_window.pack(fill="both", expand=True)

# Show the main screen with the options
show_main_screen()

# Start the Tkinter main loop
root.mainloop()
