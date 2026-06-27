import tkinter as tk

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

def add_subject():
    name = subject_entry.get()
    gpa = gpa_entry.get()
    credits = credit_entry.get()
    if name and gpa and credits:
        subjects.append({"name": name, "gpa": float(gpa), "credits": int(credits)})
        history_list.insert(tk.END, f"{name} | GPA: {gpa} | Credits: {credits}")
        subject_entry.delete(0, tk.END)
        gpa_entry.delete(0, tk.END)
        credit_entry.delete(0, tk.END)

add_btn = tk.Button(form_frame, text="Add Subject", bg="#0e6655", fg="white", font=("Helvetica", 11, "bold"), padx=20, pady=5, command=add_subject)
add_btn.grid(row=3, column=0, columnspan=2, pady=15)

history_label = tk.Label(root, text="Added Subjects:", bg="#e8f8f5", font=("Helvetica", 12, "bold"))
history_label.pack()

history_list = tk.Listbox(root, width=70, height=8, font=("Helvetica", 10))
history_list.pack(pady=10)

cgpa_label = tk.Label(root, text="Current CGPA: 0.0", bg="#e8f8f5", font=("Helvetica", 13, "bold"), fg="#0e6655")
cgpa_label.pack(pady=10)

root.mainloop()