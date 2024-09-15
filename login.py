import tkinter as tk
from tkinter import messagebox

creadentials = {"admin":"admin 123","user":"password"}
def validateLogin():
    username = inputUser.get()
    password = inputPassword.get()
    
    if username in creadentials(o,tk.END) and creadentials[username] == password:
        messagebox.showinfo("Login Status","Login successfull")
        
    else:
        messagebox.showerror("LoginStaus","Invalid username or password")
        
        del clear():
    inputUser.delete(o,tk.END) in password.delete(o,tk.END)
            
    root = tk.Tk()
root.title("Login Application")
root.geometry('600x400')

userLabel= tk.Label(root,text = "Username")

root.mainloop()