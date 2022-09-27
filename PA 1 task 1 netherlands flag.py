from pickle import TRUE
import tkinter 

window = tkinter.Tk()

frame1 = tkinter.Frame(window, height=50, bg="red")
frame1.pack(fill=tkinter.BOTH,expand=True)

frame2 = tkinter.Frame(window, height=50, bg="white")
frame2.pack(fill=tkinter.BOTH,expand=True)

button1 = tkinter.Button(text="Netherlands",bg="white")
button1.place(x=25, y=60)

frame3 = tkinter.Frame(window, height=50, bg="blue")
frame3.pack(fill=tkinter.BOTH, expand=True)

window.mainloop()