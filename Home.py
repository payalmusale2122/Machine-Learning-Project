import tkinter as tk
from tkinter import messagebox as ms
from PIL import Image, ImageTk
from subprocess import call

# Global variable
fn = ""

# --- Main Window ---
root = tk.Tk()
root.configure(background="brown")

# Get screen width and height for full-screen size
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Yoga Pose Detection Using Machine Learning")

# --- Background Image ---
try:
    image2 = Image.open('a1.jpg')
    image2 = image2.resize((1530, 1000), Image.Resampling.LANCZOS)
    background_image = ImageTk.PhotoImage(image2)
    background_label = tk.Label(root, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0)
except Exception as e:
    ms.showerror("Image Load Error", f"Could not load background image: {e}")

# --- Header Label ---
label_l1 = tk.Label(root, text="Yoga Pose Detection Using Machine Learning", 
                    font=("Times New Roman", 35, 'bold'), 
                    background="#152238", fg="white", width=50, height=2)
label_l1.place(x=0, y=0)

# --- Help Function ---
def help():
    frame_alpr = tk.LabelFrame(root, text=" --Yoga Poses-- ", width=900, height=550, bd=5, 
                               font=('times', 14, ' bold '), bg="SeaGreen1")
    frame_alpr.grid(row=0, column=0, sticky='nw')
    frame_alpr.place(x=450, y=120)

    # List of yoga poses and corresponding images
    poses = [("Vajrasan", 'v.jpg', 500, 150),
             ("Sarvangasan", 'sar.jpg', 700, 150),
             ("Shirsasan", 'shi.jpg', 900, 150),
             ("Chakrasan", 'ch.jpg', 1100, 150),
             ("Shavasan", 's.jpg', 500, 400),
             ("Gomukhaasan", 'g.jpg', 700, 400),
             ("Bhadraasan", 'b.jpg', 900, 400),
             ("Dhanurasan", 'd.jpg', 1100, 400)]

    for pose, image_file, x, y in poses:
        try:
            image = Image.open(image_file)
            image = image.resize((200, 200), Image.Resampling.LANCZOS)
            background_image = ImageTk.PhotoImage(image)
            background_label = tk.Label(root, image=background_image, text=pose, compound='bottom')
            background_label.image = background_image
            background_label.place(x=x, y=y)
        except Exception as e:
            ms.showerror("Image Load Error", f"Could not load {pose} image: {e}")

# --- Action Function (Opens a new Python script) ---
def action():
    try:
        call(["python", "GUI_Master.py"])
    except Exception as e:
        ms.showerror("Action Error", f"Failed to open GUI_Master.py: {e}")

# --- Exit Function ---
def window():
    root.destroy()

# --- Buttons ---
button1 = tk.Button(root, text="Recognize Yoga Pose", command=action, width=20, height=1, 
                   bg="#152238", fg="white", font=('times', 20, 'bold'))
button1.place(x=100, y=220)

button3 = tk.Button(root, text="Help", command=help, width=20, height=1, 
                   bg="#152238", fg="white", font=('times', 20, 'bold'))
button3.place(x=100, y=320)

exit_button = tk.Button(root, text="Exit", command=window, width=14, height=1, 
                        font=('times', 20, 'bold'), bg="cyan", fg="white")
exit_button.place(x=140, y=420)

# --- Mainloop ---
root.mainloop()
