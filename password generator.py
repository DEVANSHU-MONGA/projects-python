from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip

root = Tk()
root.title("Random Password Generator")
root.geometry("500x500+100+200")
root.config(bg="powder blue")
root.resizable(False, False)

frame_options = Frame(root, bg="#f0f0f0")
frame_options.pack(pady=10)

def generate_password():
    try:
        length = int(entry_length.get())
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number for password length")
        return
    
    characters = ""
    
    if var_lower.get():
        characters += string.ascii_lowercase
    if var_upper.get():
        characters += string.ascii_uppercase
    if var_numbers.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation
    
    if not characters:
        messagebox.showwarning("Selection Error", "Please select at least one character set")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    entry_password.delete(0, END)
    entry_password.insert(0, password)

def copy_to_clipboard():
    if not entry_password.get():
        messagebox.showwarning("Copy Error", "No password to copy. Please generate a password first.")
        return
    pyperclip.copy(entry_password.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")

def clear_fields():
    entry_length.delete(0, END)
    entry_password.delete(0, END)
    var_lower.set(0)
    var_upper.set(0)
    var_numbers.set(0)
    var_symbols.set(0)

var_lower = IntVar()
var_upper = IntVar()
var_numbers = IntVar()
var_symbols = IntVar()

Checkbutton(frame_options, text="Include Lowercase Letters", font=("arial 15 bold"), bd=9, variable=var_lower, bg="#f0f0f0").grid(row=0, column=0, sticky='w')
Checkbutton(frame_options, text="Include Uppercase Letters", font=("arial 15 bold"), bd=9, variable=var_upper, bg="#f0f0f0").grid(row=2, column=0, sticky='w')
Checkbutton(frame_options, text="Include Numbers", font=("arial 15 bold"), bd=9, variable=var_numbers, bg="#f0f0f0").grid(row=4, column=0, sticky='w')
Checkbutton(frame_options, text="Include Symbols", font=("arial 15 bold"), bd=9, variable=var_symbols, bg="#f0f0f0").grid(row=6, column=0, sticky='w')

Label(root, text="Password Length:", bg="#f0f0f0", bd=9, font=("arial 15 bold")).pack(pady=5)
entry_length = Entry(root, font=("arial 15 bold"), bd=9, relief=SUNKEN)
entry_length.pack(pady=5)

entry_password = Entry(root, width=30, bg="white", bd=9, font=("arial 15 bold"), relief=SUNKEN)
entry_password.pack(pady=10)

frame_buttons = Frame(root, bg="powder blue")
frame_buttons.pack(pady=10)

Button(frame_buttons, text="Generate", command=generate_password, width=7, height=1, font=("arial 25 bold"), bd=7, fg="#fff", bg="#3697f5").grid(row=0, column=0, padx=5)
Button(frame_buttons, text="Copy", command=copy_to_clipboard, width=5, height=1, font=("arial 25 bold"), bd=7, fg="#fff", bg="light green").grid(row=0, column=2, padx=5)
Button(frame_buttons, text="Clear", command=clear_fields, width=5, height=1, font=("arial 25 bold"), bd=7, fg="#fff", bg="#2a2d36").grid(row=0, column=4, padx=5)

root.mainloop()
