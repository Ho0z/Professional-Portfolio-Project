from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Typig Speed Test")
window.minsize(width=600, height=400)

bg_image = Image.open("/Users/hozaifaabdrabou/Desktop/Paython/Professional Portfolio Project/5. Typing Speed Test/image.png")
bg_photo = ImageTk.PhotoImage(bg_image)

my_label = Label(text="asdasd", font=("Arial", 24), anchor="center")
my_label.grid(column=1, row=0)
# Label
my_label = Label(text="Start Typing", font=("Arial", 24), anchor="center")
my_label.grid(column=0, row=1)

# Entry
input = Entry(width=30)
input.grid(column=1, row=1)

# Button function
def button_clicked():
    my_label.config(text=input.get())

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=1)

window.mainloop()