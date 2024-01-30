# sandaruwan
secure system login page 

import tkinter
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk
import random

window = tkinter.Tk()
window.title("Multi-step Login Page")
window.geometry('550x550')
window.configure(bg='#808080')

selected_words = []  # Added this line to define selected_words globally

def login():
    # First step authentication with username and password
    username = "admin"
    password = "user"

    if username_entry.get() == username and password_entry.get() == password:
        # If the first step is successful, proceed to the second step
        second_authentication()
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

def second_authentication():
    global selected_words  # Added this line to access selected_words globally
    # Function for the second step of authentication
    second_window = tkinter.Toplevel(window)
    second_window.title("Second Authentication Step")
    second_window.geometry('400x300')
    second_window.configure(bg='#808080')

    # Generate a random image with words
    image_path = generate_random_image()
    img = Image.open(image_path)
    img = img.resize((300, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    image_label = tkinter.Label(second_window, image=img, bg='#808080')
    image_label.image = img

    auth_word_label = tkinter.Label(second_window, text="Enter the words from the image:", bg='#808080', fg="#FFFFFF", font=("Arial", 12))
    auth_word_entry = tkinter.Entry(second_window, font=("Arial", 12))
    auth_button = tkinter.Button(second_window, text="Authenticate", bg="#DC143C", fg="#FFFFFF", font=("Arial", 12), command=lambda: authenticate_words(auth_word_entry.get(), second_window))

    image_label.pack(pady=10)
    auth_word_label.pack(pady=10)
    auth_word_entry.pack(pady=10)
    auth_button.pack(pady=20)

def generate_random_image():
    global selected_words  # Added this line to access selected_words globally
    # Generate a random image with words (you can customize this function)
    words_list = ["apple", "banana", "cherry", "dog", "elephant", "flower", "guitar", "happy", "internet", "jungle"]
    selected_words = random.sample(words_list, 3)
    text = " ".join(selected_words)

    # Create an image with the text
    image = Image.new("RGB", (300, 200), color=(255, 255, 255))
    image_draw = ImageDraw.Draw(image)
    image_draw.text((10, 10), text, fill=(0, 0, 0), font=ImageFont.truetype("arial.ttf", 20))

    # Save the image temporarily
    image_path = "temp_image.png"
    image.save(image_path)

    return image_path

def authenticate_words(user_input, second_window):
    global selected_words  # Added this line to access selected_words globally
    # You can implement your specific authentication logic here
    # For example, check if user_input matches the words from the image
    if user_input.lower() == " ".join(selected_words):
        messagebox.showinfo(title="Login Successful!", message="You successfully logged in.")
        second_window.destroy()  # Close the second window after successful authentication
    else:
        messagebox.showerror(title="Error", message="Invalid words. Authentication failed.")

frame = tkinter.Frame(bg='#8F00FF')

login_label = tkinter.Label(frame, text="Login Page", bg='#000000', fg="#DC143C", font=("Arial", 30))
username_label = tkinter.Label(frame, text="Username", bg='#8F00FF', fg="#FFFFFF", font=("Arial", 16, 'bold'))
password_label = tkinter.Label(frame, text="Password", bg='#8F00FF', fg="#FFFFFF", font=("Arial", 16, 'bold'))

username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))

login_button = tkinter.Button(frame, text="Login", bg="#DC143C", fg="#FFFFFF", font=("Arial", 16), command=login)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()
window.mainloop()
