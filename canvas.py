from tkinter import *
root=Tk()
canvas=Canvas(root,bg="red",height=1000,width=1000)
canvas.create_line(0,0,400,400,fill="white")
canvas.create_rectangle(0,0,200,200,fill="yellow")
canvas.create_oval(0,0,200,300,fill="blue",outline="white",width=20)
points=[250,110,480,200,280,280,250,110]
poly=canvas.create_polygon(points,fill="blue",outline="white",width=5)
photo=PhotoImage(file=r"C:\Users\Ashwani\PycharmProjects\batch89\test.gif")
canvas.create_image(10,100,image=photo,anchor=S)
canvas.pack()
mainloop()