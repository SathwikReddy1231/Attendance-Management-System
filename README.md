# Attendance Management System

## Overview

The **Attendance Management System** is a desktop application developed using **Python** and **Tkinter**. It provides a simple and user-friendly interface for managing student records and attendance. All student and attendance data are stored using CSV files.

---

## Features

- Secure Login System
- Add New Students
- Remove Students
- View All Students
- Mark Daily Attendance
- Date-wise Attendance Report
- Attendance Percentage Calculation
- Voice Confirmation for Successful Operations
- Simple and User-Friendly GUI

---

## Technologies Used

- Python 3
- Tkinter (GUI)
- ttk (Treeview & Combobox)
- CSV (Data Storage)
- pywin32 (Text-to-Speech)

---

## Project Structure

```
Attendance_Management_System/
│
├── Login.py
├── Dashboard.py
├── add_students.py
├── Remove_students.py
├── view_students.py
├── Mark_attendance.py
├── Show_Attendance.py
├── main.py
├── students.csv
├── attendance.csv
└── README.md
```

---

## Functional Modules

### Login

Provides administrator authentication before accessing the system.

### Dashboard

Acts as the main menu and provides navigation to all modules.

### Add Student

- Adds a new student.
- Prevents duplicate roll numbers.
- Stores student details in `students.csv`.

### Remove Student

- Removes a student using the roll number.
- Updates the student records automatically.

### View Students

- Displays all registered students in a table.
- Allows refreshing the student list.

### Mark Attendance

- Marks each student as **Present** or **Absent**.
- Prevents duplicate attendance entries for the same student on the same date.

### Date-wise Attendance Report

- Displays attendance records for a selected date.

### Attendance Percentage

Calculates and displays:

- Student Name
- Number of Present Days
- Number of Absent Days
- Attendance Percentage

---

## Data Storage

### students.csv

Stores student information.

Columns:

- Roll Number
- Student Name
- Section

### attendance.csv

Stores attendance records.

Columns:

- Roll Number
- Student Name
- Date
- Status (Present/Absent)

---

## Requirements

Install the required package before running the project:

```bash
pip install pywin32
```

Tkinter is included with the standard Python installation.

---

## How to Run

1. Install Python 3.
2. Install the required package:

```bash
pip install pywin32
```

3. Run the application:

```bash
python Login.py
```

4. Login using the administrator credentials.

---

## Default Login Credentials

```
Username : admin123
Password : admin
```

---

## Future Enhancements

- Face Recognition Attendance
- Change Username and Password Functionality


---

## Author

**Sathwik Reddy**

**Attendance Management System** using Python & Tkinter
