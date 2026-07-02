from tkinter import *
from tkinter import ttk
from datetime import date
import Dashboard
from main import mark_attendance

def main():
    root = Tk()
    root.title("Mark Attendance")
    root.geometry("500x450")
    root.resizable(False, False)
    root.config(bg="lightgrey")

    heading = Label(root,text="MARK ATTENDANCE",font=("Georgia", 18, "bold"), bg="lightgrey",fg="DarkBlue")
    heading.pack(pady=(15, 10))

    frame = Frame(root,bg="white", bd=2,relief=RIDGE,padx=20, pady=15)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    Label(frame,text="Roll Number",font=("Arial", 12, "bold"),bg="white").grid(row=0, column=0, padx=10, pady=10)

    roll = Entry(frame)
    roll.grid(row=0, column=1, padx=10, pady=10)

    Label(frame,text="Date",font=("Arial", 12, "bold"),bg="white").grid(row=1, column=0, padx=10, pady=10)

    today = Entry(frame)
    today.grid(row=1, column=1, padx=10, pady=10)
    today.insert(0, date.today().strftime("%d-%m-%Y"))

    Label(frame,text="Status", font=("Arial", 12, "bold"),bg="white").grid(row=2, column=0, padx=10, pady=10)

    status = ttk.Combobox(frame, values=["Present", "Absent"],state="readonly")
    status.grid(row=2, column=1, padx=10, pady=10)
    status.current(0)

    def clear():
        roll.delete(0, END)
        today.delete(0, END)
        today.insert(0, date.today().strftime("%d-%m-%Y"))
        status.current(0)

    def attendance():
        mark_attendance(
            roll.get(),
            today.get(),
            status.get()
        )

    def back():
        root.destroy()
        Dashboard.main()

    Button(frame,text="Mark Attendance", width=20, height=2,bg="royalblue", fg="white",command=attendance).grid(row=3, column=0,columnspan=2, pady=10)
    Button(frame,text="Clear", width=20, height=2, bg="royalblue",fg="white",command=clear).grid(row=4, column=0,columnspan=2, pady=10)
    Button(frame, text="Back", width=20, height=2, bg="royalblue",fg="white",command=back).grid(row=5, column=0,columnspan=2, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()