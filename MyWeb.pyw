import Manager
import Manager_Page
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


import sys

akun_no = 0
akun_type = ''

def Login():
    global akun_no, akun_type
    akun_type = "Manager"
    manager_list = Manager.Manager.list_manager
    usernameInput = EntryUsername.get()
    passwordInput = EntryPassword.get()
    for i in range(len(manager_list)):
        if manager_list[i].getUsername() == usernameInput:
            if manager_list[i].getPassword() == passwordInput:
                print(akun_no)
                Manager_Page.create_Toplevel1(jendela)
        akun_no += 1
            
def getAkunNameAndDepartment():
    global akun_no
    Name = Manager.Manager.list_manager[akun_no].getName()
    Department = Manager.Manager.list_manager[akun_no].getDepartment()
    return [Name, Department]
    
        

#def loginJendela():
jendela = tk.Tk()
jendela.wm_iconbitmap("icon.ico")
jendela.title("Easy Time Clock")
jendela.geometry("400x400")

LabelLogo = tk.Label(jendela, text = "Easy Time Clock")
LabelLogo.configure(font=("Times New Roman", 24))
LabelLogo.place(x = 100, y = 50)
               
LabelUsername = tk.Label(jendela, text = "Username:")
LabelUsername.configure(font=("Arial", 12))
EntryUsername = tk.Entry(jendela, width = 30)
LabelUsername.place(x = 60, y = 150)
EntryUsername.place(x = 150, y = 154)

LabelPassword = tk.Label(jendela, text = "Password:")
LabelPassword.configure(font=("Arial", 12))
EntryPassword = tk.Entry(jendela, width = 30, show="*")
LabelPassword.place(x = 60, y = 190)
EntryPassword.place(x = 150, y = 194)

LoginButton = tk.Button(jendela, text = "Login as Manager", command=Login, width = 30)
LoginButton.config(font=("Arial", 12))
LoginButton.place(x = 60, y = 240)

jendela.mainloop()


