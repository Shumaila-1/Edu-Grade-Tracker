import tkinter as tk

root = tk.Tk()
root.title("Edu Grade Tracker")
root.geometry("600x500")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

header = tk.Label(root, text="Edu Grade Tracker", bg="#2c3e50", fg="white", pady=15)
header.configure(font=("Helvetica", 18, "bold"))
header.pack(fill=tk.X)

form_frame = tk.Frame(root, bg="#f0f4f8", pady=20)
form_frame.pack()

subject_label = tk.Label(form_frame, text="Subject Name:", bg="#f0f4f8", font=("Helvetica", 11))
subject_label.grid(row=0, column=0, padx=10, pady=8, sticky="w")

subject_entry = tk.Entry(form_frame, width=30, font=("Helvetica", 11))
subject_entry.grid(row=0, column=1, padx=10, pady=8)

gpa_label = tk.Label(form_frame, text="Earned GPA (0.0 - 4.0):", bg="#f0f4f8", font=("Helvetica", 11))
gpa_label.grid(row=1, column=0, padx=10, pady=8, sticky="w")

gpa_entry = tk.Entry(form_frame, width=30, font=("Helvetica", 11))
gpa_entry.grid(row=1, column=1, padx=10, pady=8)

credit_label = tk.Label(form_frame, text="Credit Hours:", bg="#f0f4f8", font=("Helvetica", 11))
credit_label.grid(row=2, column=0, padx=10, pady=8, sticky="w")

credit_entry = tk.Entry(form_frame, width=30, font=("Helvetica", 11))
credit_entry.grid(row=2, column=1, padx=10, pady=8)

add_btn = tk.Button(form_frame, text="Add Subject", bg="#2c3e50", fg="white", font=("Helvetica", 11, "bold"), padx=20, pady=5)
add_btn.grid(row=3, column=0, columnspan=2, pady=15)

root.mainloop()