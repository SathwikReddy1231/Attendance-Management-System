from tkinter import *
import Dashboard
from main import remove_students

def main():
    root = Tk()
    root.title("Remove Student")
    root.geometry("500x350")
    root.resizable(False, False)
    root.config(bg="lightgrey")

    heading = Label(root,text="REMOVE STUDENT", font=("Georgia", 18, "bold"), bg="lightgrey",fg="DarkBlue")
    heading.pack(pady=(15, 10))

    frame = Frame(root, bg="white", bd=2, relief=RIDGE, padx=20, pady=10)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    Label(frame,text="Roll Number", font=("Arial", 12, "bold"),bg="white").grid(row=0, column=0, padx=10, pady=10)

    roll = Entry(frame, bg="lightgrey")
    roll.grid(row=0, column=1, padx=10, pady=10)
    def clear():
        roll.delete(0, END)

    def back():
        root.destroy()
        Dashboard.main()

    Button(frame,text="Remove Student",width=20,height=2,bg="royalblue", fg="white",command=lambda : remove_students(roll.get())).grid(row=1, column=0, columnspan=2, pady=10)
    Button(frame,text="Clear", width=20,height=2, bg="royalblue", fg="white",command=clear).grid(row=2, column=0, columnspan=2, pady=10)
    Button(frame, text="Back",width=20, height=2,bg="royalblue",fg="white",command=back).grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()
if __name__ == "__main__":
    main()