import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=50, height=100, bg="black")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=50, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

button1 = tk.Button(text="Belgium",bg="white")
button1.place(x=50, y=60)

frame3 = tk.Frame(master=window, width=50, bg="red")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()