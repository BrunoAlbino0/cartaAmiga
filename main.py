import tkinter as tk
from tkinter import PhotoImage

# Create the main window
root = tk.Tk()
root.title("Carta Amiga")

# Create and place labels, text, and buttons for your landing page
label = tk.Label(root, text="Carta Amiga", font=("Radley", 41))
label.pack(pady=20)

label = tk.Label(root, text="Uma comunicação segura", font=("Ovo", 35))
label.pack(pady=20)

# Load an image using PhotoImage (change the file path to your image)
#image = PhotoImage(file="path_to_your_image.gif")  # Supported formats: GIF, PGM, PPM, and PNG

# Create a label to display the image
#image_label = tk.Label(root, image=image)
#image_label.pack()

# Run the main loop
root.mainloop()