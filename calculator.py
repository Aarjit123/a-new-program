import customtkinter as ck
from tkinter import *

root = ck.CTk()
root.title("Calculator")
root.geometry("500x500")
root.config(bg="black")


# Creating an entry box
ent = ck.CTkEntry(root, font=("classic", 40), fg_color='lightgreen', text_color='black', height=50, width=450,
                  border_color='blue')
ent.pack(padx=5, pady=10)

last_key_time = 0  # Variable to track the last key press time


def order(number):
    data = ent.get()
    ent.delete(0, END)
    ent.insert(0, data + str(number))


def evaluation():
    try:
        data = ent.get()
        ent.delete(0, END)
        result = eval(data)
        ent.insert(0, result)
    except Exception:
        ent.delete(0, END)
        ent.insert(0, "Error")


def clear():
    ent.delete(0, END)


def key_press(event):
    global last_key_time
    current_time = event.time  # Get the current event time

    if current_time - last_key_time < 100:  # Check for rapid key presses
        return

    last_key_time = current_time  # Update the last key time

    key = event.char
    if key in '0123456789+-*/.':
        order(key)
    elif key in ['\r', '=', 'Return']:
        evaluation()
    elif key in ['c', 'C']:
        clear()
    elif key == '\x08':  # Backspace key
        current_data = ent.get()
        ent.delete(0, END)
        ent.insert(0, current_data[:-1])


# Bind key press events
root.bind('<Key>', key_press)

# Creating buttons
btn = ck.CTkButton(root, text="9", font=('classic', 60), width=60, bg_color="black", command=lambda: order(9))
btn.place(x=25, y=80)

btn = ck.CTkButton(root, text="8", font=('classic', 60), width=60, bg_color="black", command=lambda: order(8))
btn.place(x=155, y=80)

btn = ck.CTkButton(root, text="7", font=('classic', 60), width=60, bg_color="black", command=lambda: order(7))
btn.place(x=275, y=80)

btn = ck.CTkButton(root, text="+", font=('classic', 60), width=60, bg_color='black', fg_color="orange",
                   command=lambda: order('+'))
btn.place(x=395, y=80)

# Second row
btn = ck.CTkButton(root, text="4", font=('classic', 60), width=60, bg_color="black", command=lambda: order('4'))
btn.place(x=25, y=180)

btn = ck.CTkButton(root, text="5", font=('classic', 60), width=60, bg_color="black", command=lambda: order(5))
btn.place(x=155, y=180)

btn = ck.CTkButton(root, text="6", font=('classic', 60), width=60, bg_color="black", command=lambda: order(6))
btn.place(x=275, y=180)

btn = ck.CTkButton(root, text="-", font=('classic', 40), width=60, bg_color='black', fg_color="orange",
                   command=lambda: order('-'))
btn.place(x=395, y=180)

# Third row
btn = ck.CTkButton(root, text="1", font=('classic', 60), width=60, bg_color="black", command=lambda: order(1))
btn.place(x=25, y=280)

btn = ck.CTkButton(root, text="2", font=('classic', 60), width=60, bg_color="black", command=lambda: order(2))
btn.place(x=155, y=280)

btn = ck.CTkButton(root, text="3", font=('classic', 60), width=60, bg_color="black", command=lambda: order(3))
btn.place(x=275, y=280)

btn = ck.CTkButton(root, text="*", font=('classic', 30), width=60, bg_color='black', fg_color="orange",
                   command=lambda: order('*'))
btn.place(x=395, y=250)

btn = ck.CTkButton(root, text="/", font=('classic', 30), width=60, bg_color='black', fg_color="orange",
                   command=lambda: order('/'))
btn.place(x=395, y=300)

# Fourth row
btn = ck.CTkButton(root, text=".", font=('classic', 60), width=60, bg_color="black", command=lambda: order('.'))
btn.place(x=25, y=380)

btn = ck.CTkButton(root, text="0", font=('classic', 60), width=60, bg_color="black", command=lambda: order(0))
btn.place(x=155, y=380)

btn = ck.CTkButton(root, text="C", font=('classic', 60), width=60, bg_color="red", fg_color='red', command=clear)
btn.place(x=275, y=380)

btn = ck.CTkButton(root, text="=", font=('classic', 60), width=60, bg_color='black', fg_color="green",
                   command=evaluation)
btn.place(x=395, y=380)

root.mainloop()
