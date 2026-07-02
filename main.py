import csv
import os
import time
import tkinter
from tkinter import messagebox
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def add_students(rollno,name,sec):
    rollno = rollno.strip()
    name = name.strip()
    sec = sec.strip()
    if not rollno or not name or not sec:
        tkinter.messagebox.showwarning("warning","all fields are required")
        return

    file_exists = os.path.exists("students.csv")

    if file_exists:
        with open("students.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header

            for row in reader:
                if not row:
                    continue

                if row[0] == rollno:
                    tkinter.messagebox.showwarning("warning","Student with this Roll Number already exists!")
                    return

    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["rollno", "name", "section"])

        writer.writerow([rollno, name, sec])

    tkinter.messagebox.showinfo("status","Student added successfully")
    speaker.Speak("Student added successfully")


def remove_students(roll):
    remove_roll = roll.strip()
    if not remove_roll:
        tkinter.messagebox.showwarning("warning","All fields are required")
        return

    if not os.path.exists("students.csv"):
        tkinter.messagebox.showwarning("warning","No student records found")
        return

    with open("students.csv", "r") as file:
        reader = csv.reader(file)

        header = next(reader, None)
        students = []
        found=False

        for rows in reader:
            if not rows:
                continue

            if rows[0] == remove_roll:
                found=True

            if rows[0] != remove_roll:
                students.append(rows)

    if not found:
        tkinter.messagebox.showwarning("warning","Roll number not exist")
        return

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        if header:
            writer.writerow(header)

        writer.writerows(students)

    tkinter.messagebox.showinfo("status","Student removed")
    speaker.Speak("Student removed")
def mark_attendance(mark_roll, today, status):
    mark_roll = mark_roll.strip()

    if status == "Present":
        status = "P"
    else:
        status = "A"

    if not mark_roll:
        tkinter.messagebox.showwarning("Warning", "Roll Number is required")
        return

    if not os.path.exists("students.csv"):
        tkinter.messagebox.showwarning("Warning", "No students registered")
        return

    file_exists = os.path.exists("attendance.csv")

    student = None

    with open("students.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if row and row[0] == mark_roll:
                student = row
                break

    if student is None:
        tkinter.messagebox.showwarning("Warning", "Student not registered")
        return

    name = student[1]

    if file_exists:
        with open("attendance.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)

            for row in reader:
                if row and row[0].strip() == today.strip() and row[1].strip() == mark_roll:
                    tkinter.messagebox.showwarning("Warning", "Attendance already marked")
                    return

    with open("attendance.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["date", "rollno", "name", "status"])

        writer.writerow([today, mark_roll, name, status])

    tkinter.messagebox.showinfo("Success", "Attendance marked successfully")
    speaker.Speak("Attendance marked successfully")

def view_students():
    students = []
    with open("students.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if row:
                students.append(row)
    return students

def datewise_attendance(date):
    records = []

    if not os.path.exists("attendance.csv"):
        return records

    with open("attendance.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if len(row) >= 4 and row[0].strip() == date.strip():
                records.append([row[1], row[2], row[3]])
    return records

def attendance_percentage(roll):
    present = 0
    absent = 0
    name = None

    if not os.path.exists("attendance.csv"):
        return ("No attendance records", 0, 0, 0)

    with open("attendance.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if len(row) < 4:
                continue
            if row[1].strip() == roll.strip():
                name = row[2]
                if row[3].strip().upper() == "P":
                    present += 1
                elif row[3].strip().upper() == "A":
                    absent += 1
    total = present + absent
    if total == 0:
        return ("Student Not Found", 0, 0, 0)
    percentage = (present / total) * 100
    return (name, present, absent, round(percentage, 2))
        


