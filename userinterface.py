import tkinter as tk
from tkinter import messagebox
import cv2 as cv
import os
from PIL import Image
import numpy as np
from tkinter import simpledialog

window = tk.Tk()
window.title("Door Security")

# Function to be called when the button is clicked
def submit_info():
    first_name = txt_fname.get()
    last_name = txt_lname.get()
    mobile_number = txt_number.get()
    
    # Validate input
    if not first_name.replace(" ", "").isalpha():
        messagebox.showerror("Error", "First name should only contain alphabets")
        return
    if not last_name.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Last name should only contain alphabets")
        return
    if not mobile_number.replace(" ", "").isdigit():
        messagebox.showerror("Error", "Mobile number should only contain digits")
        return
    
    # Create a message box with name and mobile number
    message = f"Name: {first_name} {last_name}\nMobile Number: {mobile_number}"
    result = messagebox.askquestion("Submitted", message + "\n\nDo you want to edit fields?")
    
    # If the user clicks "Yes" button, allow editing
    if result == "yes":
        edit_fields()
    # If the user clicks "Train Model" button, train the model
    else:
        train_model()

# Function to train model (dummy function for demonstration)
def train_model():
    messagebox.showinfo("Model Training", "Model training in progress...")

# Function to edit input fields
def edit_fields():
    new_first_name = simpledialog.askstring("Edit", "Enter new First Name:")
    new_last_name = simpledialog.askstring("Edit", "Enter new Last Name:")
    new_mobile_number = simpledialog.askstring("Edit", "Enter new Mobile Number:")
    
    if new_first_name is not None:
        txt_fname.delete(0, tk.END)
        txt_fname.insert(0, new_first_name)
    if new_last_name is not None:
        txt_lname.delete(0, tk.END)
        txt_lname.insert(0, new_last_name)
    if new_mobile_number is not None:
        txt_number.delete(0, tk.END)
        txt_number.insert(0, new_mobile_number)

# Set column and row weights for responsiveness
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=2)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)

# Function to adjust font size based on window size
def adjust_font(event):
    font_size = max(10, int(event.height / 30))
    lb_fname.config(font=("Arial", font_size))
    lb_lname.config(font=("Arial", font_size))
    lb_number.config(font=("Arial", font_size))
    btn_submit.config(font=("Arial", font_size))

# Validation functions
def validate_name_input(text):
    if text.replace(" ", "").isalpha() or text == "":
        return True
    else:
        return False

def validate_mobile_input(text):
    if text.replace(" ", "").isdigit() or text == "":
        return True
    else:
        return False

# Label for First Name
lb_fname = tk.Label(window, text="First Name:", font=("Arial", 20))
lb_fname.grid(column=0, row=0, padx=10, pady=10)

# Entry widget for first name input
validate_name = window.register(validate_name_input)
txt_fname = tk.Entry(window, width=50, bd=5, validate="key", validatecommand=(validate_name, "%P"))
txt_fname.grid(column=1, row=0, padx=10, pady=10, sticky="ew")

# Label for Last Name
lb_lname = tk.Label(window, text="Last Name:", font=("Arial", 20))
lb_lname.grid(column=0, row=1, padx=10, pady=10)

# Entry widget for last name input
validate_name = window.register(validate_name_input)
txt_lname = tk.Entry(window, width=50, bd=5, validate="key", validatecommand=(validate_name, "%P"))
txt_lname.grid(column=1, row=1, padx=10, pady=10, sticky="ew")

# Label for Mobile Number
lb_number = tk.Label(window, text="Mobile Number:", font=("Arial", 20))
lb_number.grid(column=0, row=2, padx=10, pady=10)

# Entry widget for mobile number input
validate_mobile = window.register(validate_mobile_input)
txt_number = tk.Entry(window, width=50, bd=5, validate="key", validatecommand=(validate_mobile, "%P"))
txt_number.grid(column=1, row=2, padx=10, pady=10, sticky="ew")

# Button to submit information
btn_submit = tk.Button(window, text="Submit", font=("Arial", 20), bg="white", fg="black", command=submit_info)
btn_submit.grid(column=0, row=3, columnspan=2, padx=10, pady=10, sticky="ew")

# Bind function to window resize event
window.bind("<Configure>", adjust_font)

# Set minimum size limit
window.minsize(500, 200)

window.mainloop()
