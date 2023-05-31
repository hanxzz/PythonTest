import tkinter as tk
window = tk.Tk()
window.title("Yes")
window.geometry("500x400")
window.config(bg="red")
label1 = tk.Label(window, text = "Full Name:")
label1.place(x=10,y=20)

button=tk.Button(window, text="submit").place(x=100,y=300)

textbox1 = tk.Entry(window).place(x = 100, y = 20)

label2 = tk.Label(window, text = "Email:")
label2.place(x=10,y=60)
textbox2= tk.Entry(window).place(x = 100,y = 60)

label3 = tk.Label(window, text = "Gender:")
radiobuttonMale = tk.Radiobutton(window, text = "Male", value = 1).place(x = 10,y = 200)
radiobuttonFemale = tk.Radiobutton(window,text = "Female", value = 2).place(x = 80,y = 200)
window.mainloop()
