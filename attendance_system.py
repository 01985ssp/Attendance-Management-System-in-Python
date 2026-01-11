 ###Used to get current date and time when attendance is marked.
import datetime
###Data Storage
students = []
attendance = []
##Add Student Function
def add_student():
    name = input("Enter student name: ")  ##Takes student name from user
    students.append(name)   ###Adds it into students list
    print("Student added successfully!\n")  ###Prints confirmation message
##Mark Attendance Function
def mark_attendance():
    name = input("Enter student name: ")
    time = datetime.datetime.now()   ##Gets current date & time
    attendance.append((name, time))  ##Stores both as a tuple in attendance list
    print("Attendance marked!\n")
##View Attendance Function
def view_attendance():   ###Checks if attendance list is empty
    print("\n--- Attendance Records ---")
    if len(attendance) == 0:     ###If empty → prints message
        print("No attendance records found")
    else:                  ###Else → loops through attendance list
        for record in attendance:
            print(record[0], " - ", record[1])  ###Prints name and time separately

while True:   ###This creates an infinite loop so program keeps running.
    print("\n===== Attendance System =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        view_attendance()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
