from tkinter import *
from tkinter import ttk
from main import view_students
import Dashboard

def main():
    root = Tk()
    root.title("View Students")
    root.geometry("700x500")
    root.resizable(False, False)
    root.config(bg="lightgrey")

    heading = Label(root,text="VIEW STUDENTS",font=("Georgia", 18, "bold"),bg="lightgrey", fg="DarkBlue")
    heading.pack(pady=(15, 10))

    frame = Frame(root,bg="white",bd=2,relief=RIDGE,padx=10,pady=10)
    frame.pack(padx=20, pady=10, fill=BOTH, expand=True)

    tree = ttk.Treeview(frame,columns=("Roll", "Name", "Section"),show="headings",height=15)

    tree.heading("Roll", text="Roll Number")
    tree.heading("Name", text="Student Name")
    tree.heading("Section", text="Class-Sec")

    tree.column("Roll", width=120, anchor=CENTER)
    tree.column("Name", width=300, anchor=CENTER)
    tree.column("Section", width=150, anchor=CENTER)

    scrollbar = Scrollbar(frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    def load_students():
        for item in tree.get_children():
            tree.delete(item)

        students = view_students()

        for row in students:
            tree.insert("", END, values=row)
    
    

    button_frame = Frame(root, bg="lightgrey")
    button_frame.pack(pady=10)

    Button(button_frame,text="Refresh",width=15,bg="royalblue",fg="white",command=load_students).grid(row=0, column=0, padx=10)

    def back():
        root.destroy()
        Dashboard.main()
    Button(button_frame,text="Back",width=15,bg="royalblue",fg="white",command=back).grid(row=0, column=1, padx=10)
    load_students()
    root.mainloop()


if __name__ == "__main__":
    main()