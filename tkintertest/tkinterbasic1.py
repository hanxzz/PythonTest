import tkinter as tk
window = tk.Tk()        #for window
greeting = tk.Label(text="hello",
foreground="white",
background="maroon", # can also use fg and bg
width = 10, height = 10) # text units
greeting.pack()
window.mainloop()
