#imports the Image and ImageDraw modules from the PIL library
from PIL import Image, ImageDraw, ImageFont

# Create a new image with RGB mode and white background
image = Image.new("RGB", (800, 700), "lightblue")

# Initialize ImageDraw to draw on the image
draw = ImageDraw.Draw(image)

# Optionally, load a font (You can use a default font)
try:
    font = ImageFont.truetype("arial.ttf", 40)  # Change the font if needed
except IOError:
    font = ImageFont.load_default()

# Add text to the image
draw.text((100, 100), "ILY kels!", fill="darkblue", font=font)

# Save the image to a file
image.save("output_image.png")

# Show the image (optional)
image.show()
