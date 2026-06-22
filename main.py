import csv
import os
import time
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def add_students():
    rollno = input("Enter Roll Number: ").strip()
    name = input("Enter Name: ").strip()
    sec = input("Enter Class and Section (e.g. CSE-A): ").strip()
    if not rollno or not name or not sec:
        print("All fields are required")
        speaker.Speak("All fields are required")
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
                    print("Student with this Roll Number already exists!")
                    speaker.Speak("Student with this Roll Number already exists!")
                    return

    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["rollno", "name", "section"])

        writer.writerow([rollno, name, sec])

    print("Student added successfully")
    speaker.Speak("Student added successfully")


def remove_students():
    remove_roll = input("Enter the roll number to remove: ").strip()
    if not remove_roll:
        print("All fields are required")
        speaker.Speak("All fields are required")
        return

    if not os.path.exists("students.csv"):
        print("No student records found")
        speaker.Speak("No student records found")
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
        print("Roll number not exist")
        speaker.Speak("Roll number not exists")
        return

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        if header:
            writer.writerow(header)

        writer.writerows(students)

    print("Student removed")
    speaker.Speak("Student removed")

def mark_attendance():
    today = time.strftime("%d-%m-%Y")
    mark_roll = input("Enter the roll number to mark attendance: ").strip()
    status = input("Enter (P/A): ").strip().upper()
    if not mark_roll:
        print("All fields are required")
        speaker.Speak("All fields are required")
        return
    if status not in ["P", "A"] :
        print("Invalid status. Enter only P or A.")
        speaker.Speak("Invalid status")
        return
    if not os.path.exists("students.csv"):
        print("No students registered")
        speaker.Speak("No students registered")
        return
    file_exist = os.path.exists("attendance.csv")
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        next(reader, None)
        for rows in reader:
            if not rows:
                continue
            if rows[0] == mark_roll:
                student = rows
                break
        else:
            speaker.Speak("Student not registered")
            print("Student not registered")
            return
    name = student[1]
    if file_exist:
        with open("attendance.csv", "r") as file:
            reader = csv.reader(file)
            next(reader, None)
            for rows in reader:
                if not rows:
                  continue
                if rows[1] == mark_roll and rows[0] == today:
                    speaker.Speak("Attendance already marked")
                    print("Attendance already marked")
                    return
    with open("attendance.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exist:
            writer.writerow(["date", "rollno", "name", "status"])
        writer.writerow([today, mark_roll, name, status])
    speaker.Speak("Attendance marked successfully")
    print("Attendance marked successfully")

def view_students():
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            header = next(reader, None)  # skip header
            print("\n===== STUDENT LIST =====\n")
            found = False
            for row in reader:
                if not row:
                    continue
                found = True
                print("--------------------------------")
                print(f"Roll No : {row[0]}")
                print(f"Name    : {row[1]}")
                print(f"Section : {row[2]}")
                print("--------------------------------")
            if not found:
                print("No students found!")
    except FileNotFoundError:
        print("students.csv file not found. Add students first.")

def view_student_attendance():
    rollno = input("Enter Roll Number: ").strip()
    if not rollno:
        print("All fields are required")
        speaker.Speak("All fields are required")
        return
    try:
        with open("attendance.csv", "r") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            print(f"\n===== Attendance for Roll No: {rollno} =====\n")
            found = False
            for row in reader:
                if not row:
                    continue
                # row format: date, rollno, name, status
                if row[1] == rollno:
                    found = True
                    print(f"Date: {row[0]} | Name: {row[2]} | Status: {row[3]}")
            if not found:
                print("No attendance records found for this student.")
    except FileNotFoundError:
        print("attendance.csv file not found. Mark attendance first.")

def view_date_attendance():
    date = input("Enter Date (DD-MM-YYYY): ").strip()
    if not date:
        print("All fields are required")
        speaker.Speak("All fields are required")
        return
    try:
        with open("attendance.csv", "r") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            print(f"\n===== Attendance for Date: {date} =====\n")
            found = False
            for row in reader:
                if not row:
                    continue
                # CSV format: date, rollno, name, status
                if row[0] == date:
                    found = True
                    print(f"Roll No: {row[1]} | Name: {row[2]} | Status: {row[3]}")
            if not found:
                print("No attendance records found for this date.")
    except FileNotFoundError:
        print("attendance.csv file not found. Mark attendance first.")
def attendance_percentage():
    rollno = input("Enter Roll Number: ").strip()
    if not rollno:
        print("All fields are required")
        speaker.Speak("All fields are required")
        return
    try:
        with open("attendance.csv", "r") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            present = 0
            absent = 0
            total = 0
            name = ""
            for row in reader:
                if not row:
                    continue
                if row[1] == rollno:
                    total += 1
                    name = row[2]
                    if row[3] == "P":
                        present += 1
                    elif row[3] == "A":
                        absent += 1
            if total == 0:
                print("No attendance records found for this student.")
                speaker.Speak("No attendance records found for this student")
                return
            percentage = (present / total) * 100
            print("\n===== ATTENDANCE REPORT =====")
            print(f"Roll No            : {rollno}")
            print(f"Name               : {name}")
            print(f"Present Days       : {present}")
            print(f"Absent Days        : {absent}")
            print(f"Total Attendance   : {total}")
            print(f"Attendance %       : {percentage:.2f}%")
            if percentage < 75:
                print("WARNING: Attendance below 75%")
                speaker.Speak("Warning. Attendance below 75 percent")
    except FileNotFoundError:
        print("attendance.csv file not found.")
        speaker.Speak("Attendance file not found")


""""-----------------------------------------------------------------------------------------------------------------------------------------"""
while True:
    print("===== ATTENDANCE MANAGEMENT SYSTEM =====")
    print("1. Add Student\n2. Remove Student\n3. Mark attendance\n4. View Students\n5. View Student Attendance\n6. View Attendance By Date\n" \
    "7. view attendace percentage\n8. Exit")
    choice=input("enter any option from 1 to 8: ").strip()
    if(choice  not in ["1","2","3","4","5","6","7","8"]):
        print("please enter a value between 1 to 8")
        continue
    match(choice):
        case "1":
            add_students()
        case "2":
            remove_students()
        case "3":
            mark_attendance()
        case "4":
            view_students()
        case "5":
            view_student_attendance()
        case "6":
            view_date_attendance()
        case "7":
            attendance_percentage()
        case "8":
            print("Thank you for using the Attendance Management System")
            speaker.Speak("Thank you for using the Attendance Management System")
            break
    


