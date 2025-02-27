import tkinter as tk
from tkinter import messagebox
import json
import os
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# File to store user credentials
accounts_file = "accounts.json"

# Game variables
WIDTH, HEIGHT = 800, 600
player_width = 50
player_height = 50
player_velocity = 5
obstacle_width = 50
obstacle_height = 50
obstacle_velocity = 5
obstacle_frequency = 30

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
    clear_window()

    # Registration screen content
    tk.Label(main_window, text="Choose a Username", font=("Arial", 12, "bold")).pack(pady=10)
    reg_username_entry = tk.Entry(main_window, font=("Arial", 12), bd=2, relief="solid")
    reg_username_entry.pack(pady=5)

    tk.Label(main_window, text="Choose a Password", font=("Arial", 12, "bold")).pack(pady=10)
    reg_password_entry = tk.Entry(main_window, show="*", font=("Arial", 12), bd=2, relief="solid")
    reg_password_entry.pack(pady=5)

    def on_register_click():
        username = reg_username_entry.get()
        password = reg_password_entry.get()
        register_account(username, password)

    register_button = tk.Button(main_window, text="Register", command=on_register_click, font=("Arial", 12, "bold"),
                                bg="#4CAF50", fg="white", relief="flat", bd=0, padx=20, pady=10)
    register_button.pack(pady=20)

    # Back button to go back to the main menu
    back_button = tk.Button(main_window, text="Back", command=show_main_screen, font=("Arial", 12, "bold"),
                            bg="#f44336", fg="white", relief="flat", bd=0, padx=20, pady=10)
    back_button.pack(pady=10)

# Function to switch to the login screen
def show_login_screen():
    clear_window()

    # Login screen content
    tk.Label(main_window, text="Username", font=("Arial", 12, "bold")).pack(pady=10)
    username_entry = tk.Entry(main_window, font=("Arial", 12), bd=2, relief="solid")
    username_entry.pack(pady=5)

    tk.Label(main_window, text="Password", font=("Arial", 12, "bold")).pack(pady=10)
    password_entry = tk.Entry(main_window, show="*", font=("Arial", 12), bd=2, relief="solid")
    password_entry.pack(pady=5)

    def on_login_click():
        username = username_entry.get()
        password = password_entry.get()
        validate_login(username, password)

    login_button = tk.Button(main_window, text="Login", command=on_login_click, font=("Arial", 12, "bold"),
                             bg="#4CAF50", fg="white", relief="flat", bd=0, padx=20, pady=10)
    login_button.pack(pady=20)

    # Back button to go back to the main menu
    back_button = tk.Button(main_window, text="Back", command=show_main_screen, font=("Arial", 12, "bold"),
                            bg="#f44336", fg="white", relief="flat", bd=0, padx=20, pady=10)
    back_button.pack(pady=10)

# Function to switch back to the main screen
def show_main_screen():
    clear_window()

    label = tk.Label(main_window, text="Choose an option:", font=("Arial", 14, "bold"))
    label.pack(pady=20)

    login_button = tk.Button(main_window, text="Login", command=show_login_screen, font=("Arial", 12, "bold"),
                             bg="#4CAF50", fg="white", relief="flat", bd=0, padx=20, pady=10)
    login_button.pack(pady=10)

    create_account_button = tk.Button(main_window, text="Create Account", command=show_registration_screen,
                                      font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="flat", bd=0,
                                      padx=20, pady=10)
    create_account_button.pack(pady=10)

# Function to show the game start screen
def show_game_start_screen():
    clear_window()

    start_label = tk.Label(main_window, text="Press SPACE to start the game!", font=("Arial", 14, "bold"))
    start_label.pack(pady=40)

    # Bind space bar to start the game
    main_window.bind("<KeyPress-space>", start_game)

# Function to start the game
def start_game(event=None):
    # Close the Tkinter window and start the game in Pygame
    root.destroy()  # Close the Tkinter window

    # Setup Pygame window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2D Obstacle Game")

    # Colors
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)

    player_x = WIDTH // 4
    player_y = HEIGHT - player_height - 10
    player_velocity = 5

    obstacle_list = []
    score = 0
    game_over = False

    clock = pygame.time.Clock()

    while not game_over:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Moving player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_velocity
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_velocity
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_velocity
        if keys[pygame.K_DOWN] and player_y < HEIGHT - player_height:
            player_y += player_velocity

        # Generate obstacles
        if random.randint(1, obstacle_frequency) == 1:
            obstacle_x = random.randint(WIDTH, WIDTH + 100)
            obstacle_y = random.randint(0, HEIGHT - obstacle_height)
            obstacle_list.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))

        # Move obstacles
        for obstacle in obstacle_list:
            obstacle.x -= obstacle_velocity
            if obstacle.x < 0:
                obstacle_list.remove(obstacle)
                score += 1

        # Draw player and obstacles
        pygame.draw.rect(screen, GREEN, pygame.Rect(player_x, player_y, player_width, player_height))

        for obstacle in obstacle_list:
            pygame.draw.rect(screen, RED, obstacle)

        # Check for collisions
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        for obstacle in obstacle_list:
            if player_rect.colliderect(obstacle):
                game_over = True

        # Update score
        score_text = pygame.font.SysFont("Arial", 24).render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    # End game message
    game_over_text = pygame.font.SysFont("Arial", 48).render("Game Over", True, (255, 0, 0))
    screen.blit(game_over_text, (WIDTH // 3, HEIGHT // 3))
    pygame.display.flip()
    pygame.time.wait(2000)  # Wait for 2 seconds
    pygame.quit()

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
   