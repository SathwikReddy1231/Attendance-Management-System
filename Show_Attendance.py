from tkinter import *
from tkinter import ttk
from main import datewise_attendance
from main import attendance_percentage


def datewise_attendance_window():
    import Dashboard
    root = Tk()
    root.title("Date-wise Attendance")
    root.geometry("700x500")
    root.resizable(False, False)
    root.config(bg="lightgrey")

    Label(root,text="DATE-WISE ATTENDANCE",font=("Georgia",18,"bold"), bg="lightgrey",fg="DarkBlue").pack(pady=15)

    top_frame = Frame(root,bg="lightgrey")
    top_frame.pack()

    Label(top_frame,text="Date",font=("Arial",12,"bold"),bg="lightgrey").grid(row=0,column=0,padx=10)

    date_entry = Entry(top_frame,width=20)
    date_entry.grid(row=0,column=1,padx=10)

    frame = Frame(root,bg="white",bd=2,relief=RIDGE)
    frame.pack(padx=20,pady=20,fill=BOTH,expand=True)

    tree = ttk.Treeview(frame,columns=("Roll","Name","Status"),show="headings")

    tree.heading("Roll",text="Roll Number")
    tree.heading("Name",text="Student Name")
    tree.heading("Status",text="Status")

    tree.column("Roll",width=120,anchor=CENTER)
    tree.column("Name",width=300,anchor=CENTER)
    tree.column("Status",width=150,anchor=CENTER)

    scrollbar = Scrollbar(frame, orient=VERTICAL,command=tree.yview)

    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(side=LEFT,fill=BOTH,expand=True)
    scrollbar.pack(side=RIGHT,fill=Y)

    def search():
        for item in tree.get_children():
            tree.delete(item)
        records = datewise_attendance(date_entry.get())
        for row in records:
            tree.insert("",END,values=row)

    Button(top_frame, text="Search",bg="royalblue",fg="white",command=search).grid(row=0,column=2,padx=10)

    def back():
        root.destroy()
        Dashboard.main()
    Button(root,text="Back", width=15,bg="royalblue",fg="white",command=back).pack(pady=10)
    root.mainloop()

def attendance_percentage_window():
    import Dashboard

    root = Tk()
    root.title("Attendance Percentage")
    root.geometry("450x400")
    root.resizable(False,False)
    root.config(bg="lightgrey")

    Label(root, text="ATTENDANCE PERCENTAGE",font=("Georgia",18,"bold"), bg="lightgrey",fg="DarkBlue").pack(pady=20)
    frame = Frame(root, bg="white",bd=2,relief=RIDGE, padx=20,pady=20)
    frame.place(relx=0.5,rely=0.5,anchor=CENTER)

    Label(frame,text="Roll Number",font=("Arial",12,"bold"),bg="white").grid(row=0,column=0,pady=10)

    roll = Entry(frame)
    roll.grid(row=0,column=1,padx=10)

    result = Label(frame, text="",bg="white",justify=LEFT,font=("Arial",11))
    result.grid(row=2,column=0,columnspan=2,pady=20)

    def calculate():
        name,present,absent,percentage = attendance_percentage(roll.get())
        result.config(
            text=f"Student Name : {name}\n\n"
                 f"Present : {present}\nAbsent : {absent}\n\n"
                 f"Attendance : {percentage:.2f} %\n\n")

    Button(frame, text="Calculate", width=20, bg="royalblue",fg="white", command=calculate).grid(row=1,column=0,columnspan=2,pady=10)

    def back():
        root.destroy()
        Dashboard.main()

    Button(frame, text="Back", width=20,bg="royalblue", fg="white", command=back).grid(row=3,column=0,columnspan=2,pady=10)

    root.mainloop()

