from datetime import datetime

# Get the current date and time
now = datetime.now()

# Print the current date and time
print("Current date and time:", now)

# Accessing individual components (e.g., year, month, day)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)

# Formatting date and time
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_date)
