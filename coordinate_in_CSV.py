# -*- coding: utf-8 -*-

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox as ms
from subprocess import call

# Function for login
def Login():
    try:
        call(["python", "login1.py"])
    except Exception as e:
        ms.showerror("Error", f"An error occurred while trying to open the login page: {e}")

# Function for registration
def Register():
    try:
        call(["python", "registration.py"])
    except Exception as e:
        ms.showerror("Error", f"An error occurred while trying to open the registration page: {e}")

# Main function
def main():
    # Initialize the main Tkinter window
    root = tk.Tk()

    # Set the window title
    root.title("Yoga Pose Detection Using Machine Learning")

    # Set the window size to full screen
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f"{w}x{h}+0+0")
    root.configure(background="skyblue")

    # Set the background image (make sure the path is correct)
    try:
        image2 = Image.open('y1.jpg')  # Ensure 'y1.jpg' exists in your project directory
        image2 = image2.resize((w, h), Image.LANCZOS)
        background_image = ImageTk.PhotoImage(image2)
    except FileNotFoundError:
        ms.showerror("File Not Found", "Background image 'y1.jpg' not found. Please check the file path.")
        return

    # Create a label to display the background image
    background_label = tk.Label(root, image=background_image)
    background_label.image = background_image  # Keep a reference to avoid garbage collection
    background_label.place(x=0, y=93)  # Adjust the y-coordinate if needed

    # Create the title label
    title_label = tk.Label(root, text="Yoga Pose Detection Using Machine Learning", 
                           width=50, background="skyblue", height=2, 
                           font=("Times New Roman", 19, "bold"))
    title_label.place(x=0, y=15)

    # Create the welcome label
    welcome_label = tk.Label(root, text="......Welcome to Yoga Pose Detection System ......", 
                             width=85, height=3, background="skyblue", 
                             foreground="black", font=("Times New Roman", 22, "bold"))
    welcome_label.place(x=0, y=620)  # You can adjust 'y' based on how it looks on your screen

    # Create the Login and Register buttons
    login_button = tk.Button(root, text="Login", command=Login, width=9, height=2, bd=0, 
                             background="skyblue", foreground="black", 
                             font=("Times New Roman", 14, "bold"))
    login_button.place(x=1100, y=18)

    register_button = tk.Button(root, text="Register", command=Register, width=9, height=2, bd=0, 
                                background="skyblue", foreground="black", 
                                font=("Times New Roman", 14, "bold"))
    register_button.place(x=1200, y=18)

    # Run the Tkinter event loop
    root.mainloop()

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
