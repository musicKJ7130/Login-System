from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title('Login System')
        self.root.geometry('1350x700+0+0')

        #--------------All Images--------------------------

        self.bg_icon = ImageTk.PhotoImage(file="images\\Background.png")
        self.user_icon = ImageTk.PhotoImage(file='images\\username.png')
        self.pass_icon = ImageTk.PhotoImage(file="images\\pass.png")
        self.logo = ImageTk.PhotoImage(file="images\\Logo.png")
        #---------------------------------------


        #--------------Variables-----------------
        self.uname = StringVar()
        self.pas = StringVar()

        #-----------------------------------------

        bg_lbl = Label(self.root, image=self.bg_icon).pack()

        title =  Label(self.root, text="Login", font=('Arial',40,'bold'), bg="cyan", fg="black", bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=400, y=150)

        logolbl = Label(login_frame, image=self.logo, bd=0, bg="white").grid(row=0, columnspan=2, pady=20, padx=20)  

        lbluser = Label(login_frame, text="Username", image=self.user_icon, compound=LEFT, font=("times new roman",20,"bold"), bg="white").grid(row=1, column=0, padx=20, pady=10)

        txtuser = Entry(login_frame, bd=5, relief=GROOVE, font=("",15), textvariable=self.uname).grid(row=1, column=1, padx=20, pady=10)
        
        lblpass = Label(login_frame, text="Password", image=self.pass_icon, compound=LEFT, font=("times new roman",20,"bold"), bg="white").grid(row=2, column=0, padx=20, pady=10)

        txtpass = Entry(login_frame, bd=5, relief=GROOVE, textvariable=self.pas, font=("",15)).grid(row=2, column=1, padx=20, pady=10)

        btn_login = Button(login_frame, text="Login", width=20, font=("times new roman", 14, "bold"), command=self.login,bg="skyblue", fg="black").grid(row=3, column=1, pady=10, padx=10)
        

    def login(self):
        if self.uname.get() == "" or self.pas == "":
            messagebox.showerror("Error", "All Fields are Required!")
        
        elif self.uname.get() == "Karan" and self.pas == "2018" or self.uname.get() == "karan":
            messagebox.showinfo("Login Successful", f"Welcome {self.uname.get()}!")

        else:
            messagebox.showerror("Error", "Invalid Username or Password! Please try again!")

        
  
root=Tk()
obj=Login_System(root)
root.mainloop()
