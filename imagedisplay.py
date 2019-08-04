from tkinter import *
from PIL import Image, ImageTk
root=Tk()

'''luck = Button(root, text="LUCK", bg="black", fg="green", width=20,
                 command=lambda: ImageShow("test.gif"))
luck.place(x=35, y=200)'''


def ImageShow(path):
    label = Label(root, bg="black", width=40, height=40)
    label.place(x=215, y=75)

    image = Image.open(path)
    photo = ImageTk.PhotoImage(image)

    label = Label(root, image=photo, bg="black", fg="white")
    label.image = photo  # keeping refrence
    label.place(x=200, y=75)

ImageShow("test.gif")
root.mainloop()
