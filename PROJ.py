import random
import sqlite3
import tkinter
from tkinter import messagebox

# Database setup
conn = sqlite3.connect('blood_donation.db')
cursor = conn.cursor()
with open('example.sql', 'r') as f:
    sql_script = f.read()
cursor.executescript(sql_script)
conn.commit()

window=tkinter.Tk()
window.title("Login form")
window.geometry('340x440')
window.configure(bg='#333333')
def login():
    username = username_entry.get()
    password = password_entry.get()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    if cursor.fetchone():
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        window.quit()
    else:
        messagebox.showerror(title="Error", message="Invalid login")

frame=tkinter.Frame(bg='#333333')


login_label=tkinter.Label(frame,text="Login", bg='#333333', fg="#FFFFFF", font=("Arial", 30))
username_label=tkinter.Label(frame,text="Username",bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry=tkinter.Entry(frame, font=("Arial", 16))
password_entry=tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label=tkinter.Label(frame,text="Password",bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button=tkinter.Button(frame,text="Login", font=("Arial", 16), command=login)

login_label.grid(row=0,column=0,columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)
def Donor_details():
  """Registers new donor"""
  d_id= random.randint(1,201)
  print("Donor id: ",d_id)
  dname = input("Enter donor name: ")
  age=int(input("Enter donor age: "))
  if age<18:
    print("You are not eligible to donate blood")
    return
  gender=input("Enter gender: ")
  b_grp=input("Enter Blood group type(A+/A-/B+/B-/O+/O-/AB+/AB-): ")
  ph_no=input("Enter Phone number: ")
  if len(ph_no)!=10 or not ph_no.isdigit():
    print("Invalid contact number")
    return
  H_issue=input("Any Health issues(Y/N): ").upper()
  if H_issue=="Y":
    issue=input("Enter health issue: ")
    H_issue = issue
  elif H_issue=="N":
    print("You are healthy")
  try:
    cursor.execute("INSERT INTO donors (d_id, dname, age, gender, b_grp, ph_no, H_issue) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (d_id, dname, age, gender, b_grp, ph_no, H_issue))
    conn.commit()
    print(f"Donor '{dname}' added successfully")
  except sqlite3.IntegrityError:
    print("Donor ID already exists, try again")

def D_records():
  """Records donation by donor"""
  dname=input("Enter donor name: ")
  d_id=int(input("Enter Donor id of donor: "))
  cursor.execute("SELECT * FROM donors WHERE d_id = ?", (d_id,))
  if cursor.fetchone():
    Donation_Date=input("Enter donation date(format:YYYY-MM-DD): ")
    cursor.execute("INSERT INTO records (d_id, dname, Donation_Date) VALUES (?, ?, ?)", (d_id, dname, Donation_Date))
    conn.commit()
    print(f"Donation by '{dname}' recorded successfully")
  else:
    print(f"Donor '{dname}' not found")
      
def show_donors():
  """Shows all registered donors"""
  cursor.execute("SELECT * FROM donors")
  donors = cursor.fetchall()
  if donors:
    print("List of all registered donors: ")
    for donor in donors:
      print(f" - {donor[1]} (Donor_ID: {donor[0]}, Age: {donor[2]}, Gender: {donor[3]}, Blood Type: {donor[4]}, Ph_no: {donor[5]})")
  else:
      print("No donors registered yet.")  
def search_bloodgrp():
  """Searches for donor based on blood grp."""
  grp = input("Enter blood group to be searched: ")
  cursor.execute("SELECT * FROM donors WHERE b_grp = ?", (grp,))
  results = cursor.fetchall()
  if results:
    print(f"Found Donors with blood group '{grp}':")
    for donor in results:
      print(f"- {donor[1]} available")
  else:
    print(f"No Donor found with blood group '{grp}'.")

def show_all_Donations():
  """Displays information of all donations."""
  cursor.execute("SELECT * FROM records")
  records = cursor.fetchall()
  if records:
    print("All donation records:")
    for record in records:
      print(f"- Donor: {record[2]} (ID: {record[1]}), Date: {record[3]}")
  else:
    print("No donation records yet.")

def main():
  frame.pack()
  window.mainloop()
  while True:
    print("Welcome to the Blood Donation Management System!")
    print("1. Donor Details")
    print("2. Record Donation")
    print("3. Show All Donors")
    print("4. Search Donors")
    print("5. Show All Donations")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
      Donor_details()
    elif choice == "2":
      D_records()
    elif choice == "3":
      show_donors()
    elif choice == "4":
      search_bloodgrp()
    elif choice == "5":
      show_all_Donations()
    elif choice == "6":
      print("Thank you for using the Blood Donation Management System!")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 6.")
  conn.close()

if __name__ == "__main__":
  main()
