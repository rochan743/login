from tkinter import *
window = Tk()

window.title('sample')

window.geometry('400x400')

greeting = Label(text = "Hi", fg="black", bg='white')

greeting.pack()

bt = Button(text="Click me", bg= "black",fg= 'white')

bt.pack(pady = 5)

input1 = Entry(bg = 'white')

input1.pack(pady=10)

window.mainloop()