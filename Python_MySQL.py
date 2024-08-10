import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

# Function to connect to MySQL database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # MySQL username
        password="1999",  # MySQL password
        database="vivian"  # MySQL database name
    )

# Function to create the DATAGRID table if it doesn't exist
def create_table():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS DATAGRID (
            Sno INT PRIMARY KEY,
            Name VARCHAR(255),
            Age INT,
            Mail VARCHAR(255),
            Mobile VARCHAR(15)
        )
    """)
    conn.close()

# Function to handle data submission
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

# Function to handle data deletion
def delete_data():
    sno = sno_entry.get().strip()  # Stripping any extra spaces
    name = name_entry.get().strip()
    age = age_entry.get().strip()

    if sno or name or age:
        try:
            conn = connect_to_db()
            cursor = conn.cursor()

            print(f"Attempting to delete record with Sno: {sno}, Name: {name}, Age: {age}")  # Debugging line

            cursor.execute("DELETE FROM DATAGRID WHERE Sno = %s OR Name = %s OR Age = %s", (sno, name, age))
            conn.commit()
            conn.close()

            if cursor.rowcount == 0:
                messagebox.showwarning("Not Found", "No record found with the provided Sno, Name, or Age")
            else:
                messagebox.showinfo("Success", "Data deleted successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"An error occurred: {err}")
    else:
        messagebox.showwarning("Input Error", "Please enter at least one field to delete")

# Function to display data in the grid
def display_data():
    for row in tree.get_children():
        tree.delete(row)
    
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DATAGRID")
    rows = cursor.fetchall()
    conn.close()
    
    for row in rows:
        tree.insert("", tk.END, values=row)

# Create the main application window
root = tk.Tk()
root.title("Data Entry")

# Add labels and entry fields for Sno, Name, Age, Mail, and Mobile
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

# Add buttons for Submit and Delete actions
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=5, column=0)

delete_button = tk.Button(root, text="Delete", command=delete_data)
delete_button.grid(row=5, column=1)

# Create a Treeview widget to display the data grid
tree = ttk.Treeview(root, columns=("Sno", "Name", "Age", "Mail", "Mobile"), show='headings')

tree.heading("Sno", text="Sno")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Mail", text="Mail")
tree.heading("Mobile", text="Mobile")

# Ensure the table is created when the script runs
create_table()

# Display initial data in the grid
display_data()

# Start the Tkinter event loop
root.mainloop()
