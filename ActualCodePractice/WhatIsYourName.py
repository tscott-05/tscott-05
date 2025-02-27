#Create a code that allows you to ask what is your name and allows the user to input the name (Maybe add an age with the year you were born?)

from datetime import datetime

name = input("What is your name? ")
age = int(input("What is your age? "))
current_year = 2025

# Get today's date
today = datetime.today()

# Ask for the user's birthdate (month and day)
birth_month = int(input("What is your birth month (1-12)? "))
birth_day = int(input("What is your birth day (1-31)? "))

# Calculate the year of birth based on age
year_of_birth = current_year - age

# Check if the birthday has occurred yet this year
if today.month < birth_month or (today.month == birth_month and today.day < birth_day):
    year_of_birth -= 1
# Print the user's name and year of birth
print(f"Hello {name}, you were born in {year_of_birth}.")



