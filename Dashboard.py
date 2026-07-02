from tkinter import *
def main():
       root=Tk()
       import add_students
       import Remove_students
       import view_students
       import Mark_attendance
       import Show_Attendance
       import Login
       def open_add_student():
              root.destroy()
              add_students.main()
       def open_remove_students():
              root.destroy()
              Remove_students.main()
       def open_view_students():
              root.destroy()
              view_students.main()
       def open_mark_attendance():
              root.destroy()
              Mark_attendance.main()
       def open_datewise_window():
              root.destroy()
              Show_Attendance.datewise_attendance_window()
       def open_percentage_window():
              root.destroy()
              Show_Attendance.attendance_percentage_window()
       def login_window():
              root.destroy()
              Login.login()


       root.title("Attendance Management System")
       root.geometry("800x550")
       root.resizable(False,False)
       root.config(bg="lightgrey")

       heading=Label(root,text="ATTENDANCE MANAGEMENT SYSTEM",font=("Georgia",18,"bold"),bg="lightgrey",fg="Darkblue")
       heading.pack(pady=(25,25))
       frame=Frame(root,bg="white",bd=2,relief=RIDGE,padx=40,pady=25)
       frame.place(relx=0.5,rely=0.58,anchor="center")
       Label(frame, text="Student Management",
       font=("Arial",12,"bold"), bg="white").grid(row=0, column=0, pady=(0,20),padx=30)

       Button(frame, text="Add Student", width=20,height=2,
              bg="royalblue", fg="white",command=open_add_student).grid(row=1, column=0, pady=8,padx=30)

       Button(frame, text="Remove Student", width=20,height=2,
              bg="royalblue", fg="white",command=open_remove_students).grid(row=2, column=0, pady=8,padx=30)

       Button(frame, text="View Students", width=20,height=2,command=open_view_students,
              bg="royalblue", fg="white").grid(row=3, column=0, pady=8,padx=30)


       Label(frame, text="Attendance",
       font=("Arial",12,"bold"), bg="white").grid(row=0, column=2, padx=80, pady=(0,20))

       Button(frame, text="Mark Attendance", width=20,height=2,command=open_mark_attendance,
              bg="royalblue", fg="white").grid(row=1, column=2, pady=5,padx=30)

       Button(frame, text="Date-wise Attendance", width=20,height=2,command=open_datewise_window,
              bg="royalblue", fg="white").grid(row=2, column=2, pady=5,padx=30)

       Button(frame, text="Attendance Percentage", width=20,height=2,command=open_percentage_window,
              bg="royalblue", fg="white").grid(row=3, column=2, pady=5,padx=30)


       Button(frame, text="LOGOUT", width=20,height=2,
              font=("Arial",12,"bold"),
              bg="royalblue", fg="white",command=login_window).grid(row=4, column=0, columnspan=3, pady=(30,10))

       Button(frame, text="EXIT", width=20,height=2,
              font=("Arial",12,"bold"),
              bg="red", fg="white",
              command=root.destroy).grid(row=5, column=0, columnspan=3)
       root.mainloop()
if __name__=="__main__":
       main()