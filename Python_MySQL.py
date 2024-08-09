import tkinter as tk
from tkinter import messagebox
import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # MySQL username
        password="1999",  # MySQL password
        database="vivian"  # MySQL database name
    )
    
def submit_data():
    sno = sno_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    mail = mail_entry.get()
    mobile = mobile_entry.get()

    if sno and name and age and mail and mobile:
        try:
            conn = connect_to_db()
            cursor = conn.cursor()

            cursor.execute("INSERT INTO DATAGRID (Sno, Name, Age, Mail, Mobile) VALUES (%s, %s, %s, %s, %s)",
                           (sno, name, age, mail, mobile))
            conn.commit() 
            conn.close()  

            messagebox.showinfo("Success", "Data inserted successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"An error occurred: {err}")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")

root = tk.Tk()
root.title("Data Entry")

tk.Label(root, text="Sno").grid(row=0, column=0)
sno_entry = tk.Entry(root)
sno_entry.grid(row=0, column=1)

tk.Label(root, text="Name").grid(row=1, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1)

tk.Label(root, text="Age").grid(row=2, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1)

tk.Label(root, text="Mail").grid(row=3, column=0)
mail_entry = tk.Entry(root)
mail_entry.grid(row=3, column=1)

tk.Label(root, text="Mobile").grid(row=4, column=0)
mobile_entry = tk.Entry(root)
mobile_entry.grid(row=4, column=1)

submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=5, column=1)

root.mainloop()

def create_table():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS DATAGRID (
            Sno INT,
            Name VARCHAR(255),
            Age INT,
            Mail VARCHAR(255),
            Mobile INT
        )
    """)

    conn.close()
