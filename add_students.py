from tkinter import *
from tkinter import ttk
from main import add_students
import Dashboard

def main():
    root = Tk()
    root.title("Add Student")
    root.geometry("500x450")
    root.resizable(False, False)
    root.config(bg="lightgrey")
    def submit():
        roll = Roll.get()
        name = Name.get()
        sec = clasec.get()

        add_students(roll, name, sec)

    heading = Label(root, text="ADD STUDENT",
                    font=("Georgia", 18, "bold"),
                    bg="lightgrey", fg="Darkblue")
    heading.pack(pady=(10, 10))

    frame = Frame(root, bg="white", bd=2, relief=RIDGE, padx=15, pady=15)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    Label(frame, text="Roll Number", font=("Arial", 12, "bold"), bg="white").grid(row=0, column=0, pady=10)
    Roll = Entry(frame, bg="lightgrey")
    Roll.grid(row=0, column=1, pady=10, padx=10)

    Label(frame, text="Student Name", font=("Arial", 12, "bold"), bg="white").grid(row=1, column=0, pady=10)
    Name = Entry(frame, bg="lightgrey")
    Name.grid(row=1, column=1, pady=10, padx=10)

    Label(frame, text="Class-Sec", font=("Arial", 12, "bold"), bg="white").grid(row=2, column=0, pady=10)
    Values = ["CSE-A", "CSE-B", "AI-DS", "ECE"]
    clasec = ttk.Combobox(frame, values=Values,state="readonly")
    clasec.grid(row=2, column=1, pady=10, padx=10)

    def clear_fields():
        Roll.delete(0, END)
        Name.delete(0, END)
        clasec.set("")
    def back():
        root.destroy()
        Dashboard.main()

    Button(frame, text="Add Student", width=20, height=2,bg="royalblue", fg="white",command=submit).grid(row=3,column=0,pady=10,columnspan=2)
    Button(frame, text="Clear", width=20, height=2,bg="royalblue", fg="white", command=clear_fields).grid(row=4, column=0, pady=10,columnspan=2)
    Button(frame, text="Back", width=20, height=2,bg="royalblue", fg="white",command=back).grid(row=5, column=0, pady=10,columnspan=2)

    root.mainloop()

if __name__=="__main__":
    main()