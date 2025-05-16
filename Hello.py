import tkinter as tk

def say_hello():
    label.config(text="What a nice day!")
    print("Hello World!")

root = tk.Tk()
root.title("SNF GUI Example")

label = tk.Label(root, text="Click the button!")
label.pack()

button = tk.Button(root, text="Hello World", command=say_hello)
button.pack()

root.mainloop()