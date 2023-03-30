import tkinter
import tkinter as tk
window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg = "red")
frame1.pack(fill=tk.X, side=tk.LEFT)
# Fill= tk.X to fill the entire frame horizontally
# the frame will be packed from the left instead of TOP(which is default)
frame2 = tk.Frame(master=window, width=50, height=50, bg = "yellow")
frame2.pack(fill=tk.X, side= tk.LEFT)

frame3 = tk.Frame(master = window, width=25, height=25, bg = "blue")
frame3.pack(fill=tk.X, side = tk.LEFT)
window.mainloop()