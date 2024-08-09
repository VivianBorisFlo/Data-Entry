import tkinter as tk  # Importing Tkinter for GUI
from tkinter import messagebox  # Importing messagebox for alerts
import mysql.connector  # Importing MySQL connector for database operations

# Function to connect to MySQL database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # MySQL username
        password="1999",  # MySQL password
        database="vivian"  # MySQL database name
    )

# Function to handle data submission
def submit_data():
    # Get user input from the entry fields
    sno = sno_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    mail = mail_entry.get()
    mobile = mobile_entry.get()

    # Check if all fields are filled
    if sno and name and age and mail and mobile:
        try:
            conn = connect_to_db()
            cursor = conn.cursor()

            # Insert the data into the DATAGRID table
            cursor.execute("INSERT INTO DATAGRID (Sno, Name, Age, Mail, Mobile) VALUES (%s, %s, %s, %s, %s)",
                           (sno, name, age, mail, mobile))
            conn.commit()  # Save changes to the database
            conn.close()  # Close the database connection

            # Show a success message
            messagebox.showinfo("Success", "Data inserted successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"An error occurred: {err}")
    else:
        # Show a warning if any fields are empty
        messagebox.showwarning("Input Error", "Please fill all fields")

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

# Add a button that calls submit_data when clicked
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=5, column=1)

# Start the Tkinter event loop (this makes the window appear)
root.mainloop()

# Connecting to MySQL and creating the DATAGRID table (if not already created)
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
