from tkinter import *
from tkinter import messagebox
import Dashboard

def login():
    root = Tk()
    root.title("Attendance Management System")
    root.geometry("600x500")
    root.resizable(False, False)
    root.configure(bg="lightgrey")

    def open_Dashboard():
        root.destroy()
        Dashboard.main()

    main_frame = Frame(root, bg="white", bd=2, relief=RIDGE, padx=30, pady=20)
    main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    heading_label = Label(main_frame,text="ATTENDANCE MANAGEMENT SYSTEM",font=("Georgia", 18, "bold"),bg="white",fg="darkblue")
    heading_label.pack(pady=(0, 25))

    username_label = Label(main_frame,text="Username",font=("Arial", 12),bg="white")
    username_label.pack(anchor="w")

    user_name = Entry(main_frame,width=30,font=("Arial", 12))
    user_name.pack(pady=(5, 15))
    user_name.focus()

    password_label = Label(main_frame,text="Password",font=("Arial", 12),bg="white")
    password_label.pack(anchor="w")

    password = Entry(main_frame,show="*",width=30,font=("Arial", 12))
    password.pack(pady=(5, 10))

    show_var = IntVar()
    def toggle_password():
        if show_var.get() == 1:
            password.config(show="")
        else:
            password.config(show="*")

    show_password = Checkbutton(main_frame,text="Show Password",variable=show_var,command=toggle_password,bg="white",font=("Arial", 10))
    show_password.pack(anchor="w", pady=(0, 20))

    def do_login():
        Username = user_name.get().strip()
        Password = password.get().strip()
        if Username =="admin123" and Password=="admin":
            messagebox.showinfo("Status", f"{Username} is logged in")
            open_Dashboard()
        else:
            messagebox.showwarning("Warning","Enter Correct366 Username or Password")
            
            
    login_button = Button(main_frame,text="LOGIN",width=18,font=("Arial", 12, "bold"),bg="royalblue",fg="white",command=do_login)
    login_button.pack(pady=10)
    root.bind("<Return>",lambda event:do_login())

    exit_button = Button(main_frame,text="EXIT",width=18,font=("Arial", 12, "bold"),bg="red",fg="white",command=root.destroy)
    exit_button.pack()

    root.mainloop()

if __name__=="__main__":
    login()