import tkinter as tk
from tkinter import messagebox, ttk

subjects = []

def calculate_cgpa():
    if len(subjects) == 0:
        return 0.0
    total_points = 0
    total_credits = 0
    for subject in subjects:
        total_points += subject["gpa"] * subject["credits"]
        total_credits += subject["credits"]
    return round(total_points / total_credits, 2)

def add_subject():
    name = subject_entry.get()
    gpa = gpa_entry.get()
    credits = credit_entry.get()
    if not name or not gpa or not credits:
        messagebox.showerror("Missing Fields", "Please fill in all fields.")
        return
    if not name.replace(' ', '').isalpha():
        messagebox.showerror("Invalid Name", "Subject name must contain letters only.")
        return
    if not gpa.replace('.', '', 1).isdigit():
        messagebox.showerror("Invalid GPA", "GPA must be a number.")
        return
    if not credits.isdigit():
        messagebox.showerror("Invalid Credits", "Credit Hours must be a whole number.")
        return
    gpa_value = float(gpa)
    if gpa_value < 0.0 or gpa_value > 4.0:
        messagebox.showerror("Invalid GPA", "GPA must be between 0.0 and 4.0.")
        return
    if int(credits) not in [1, 2, 3]:
        messagebox.showerror("Invalid Credits", "Credit Hours must be 1, 2 or 3.")
        return
    subjects.append({"name": name, "gpa": gpa_value, "credits": int(credits)})
    table.insert("", tk.END, values=(name, gpa_value, int(credits)))
    subject_entry.delete(0, tk.END)
    gpa_entry.delete(0, tk.END)
    credit_entry.delete(0, tk.END)
    cgpa_label.config(text=f"Current CGPA: {calculate_cgpa()}")

root = tk.Tk()
root.title("Edu Grade Tracker")
root.geometry("600x650")
root.resizable(False, False)
root.configure(bg="#e8f8f5")

header = tk.Label(root, text="Edu Grade Tracker", bg="#0e6655", fg="white", pady=15)
header.configure(font=("Helvetica", 18, "bold"))
header.pack(fill=tk.X)

form_frame = tk.Frame(root, bg="#e8f8f5", pady=20)
form_frame.pack()

subject_label = tk.Label(form_frame, text="Subject Name:", bg="#e8f8f5", font=("Helvetica", 11))
subject_label.grid(row=0, column=0, padx=10, pady=8, sticky="w")

subject_entry = tk.Entry(form_frame, width=30, font=("Helvetica", 11))
subject_entry.grid(row=0, column=1, padx=10, pady=8)

gpa_label = tk.Label(form_frame, text="Earned GPA (0.0 - 4.0):", bg="#e8f8f5", font=("Helvetica", 11))
gpa_label.grid(row=1, column=0, padx=10, pady=8, sticky="w")

gpa_entry = tk.Entry(form_frame, width=30, font=("Helvetica", 11))
gpa_entry.grid(row=1, column=1, padx=10, pady=8)

credit_label = tk.Label(form_frame, text="Credit Hours:", bg="#e8f8f5", font=("Helvetica", 11))
credit_label.grid(row=2, column=0, padx=10, pady=8, sticky="w")

credit_entry = tk.Entry(form_frame, width=30, font=("Helvetica", 11))
credit_entry.grid(row=2, column=1, padx=10, pady=8)

add_btn = tk.Button(form_frame, text="Add Subject", bg="#0e6655", fg="white", font=("Helvetica", 11, "bold"), padx=20, pady=5, command=add_subject)
add_btn.grid(row=3, column=0, columnspan=2, pady=15)

history_label = tk.Label(root, text="Added Subjects:", bg="#e8f8f5", font=("Helvetica", 12, "bold"))
history_label.pack()

style = ttk.Style()
style.configure("Treeview.Heading", font=("Helvetica", 11, "bold"))
style.configure("Treeview", font=("Helvetica", 10), rowheight=25)

table = ttk.Treeview(root, columns=("Subject", "GPA", "Credits"), show="headings", height=8)
table.heading("Subject", text="Subject Name", anchor="center")
table.heading("GPA", text="GPA", anchor="center")
table.heading("Credits", text="Credit Hours", anchor="center")
table.column("Subject", width=250, anchor="center")
table.column("GPA", width=150, anchor="center")
table.column("Credits", width=150, anchor="center")
table.pack(pady=10)

cgpa_label = tk.Label(root, text="Current CGPA: 0.0", bg="#e8f8f5", font=("Helvetica", 13, "bold"), fg="#0e6655")
cgpa_label.pack(pady=10)

root.mainloop()