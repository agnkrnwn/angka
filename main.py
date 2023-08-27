import tkinter as tk
from tkinter import filedialog
from collections import Counter
import random

# Fungsi untuk membaca angka dari file
def read_numbers(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        numbers = [int(number) for line in lines for number in line.strip()]
    return numbers

# Fungsi untuk memilih angka acak dari angka teratas
def select_random_numbers(top_numbers, count):
    return random.sample(top_numbers, count)

# Fungsi untuk menjalankan analisis dan menampilkan hasil
def analyze_and_display():
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filename:
        numbers = read_numbers(filename)
        total_numbers = len(numbers)
        number_counts = Counter(numbers)
        percentage_dict = {number: (count / total_numbers) * 100 for number, count in number_counts.items()}

        result_text.delete(1.0, tk.END)
        random_numbers_text.delete(1.0, tk.END)

        for number, percentage in sorted(percentage_dict.items(), key=lambda item: item[1], reverse=True):
            result_text.insert(tk.END, f"Angka {number}: {percentage:.2f}%\n", "result")

        top_numbers = [number for number, _ in sorted(percentage_dict.items(), key=lambda item: item[1], reverse=True)]
        num_of_random_numbers = num_of_random_var.get()
        random_selected_numbers = select_random_numbers(top_numbers, num_of_random_numbers)

        result_text.insert(tk.END, f"\n{num_of_random_numbers} Angka Acak dari Angka Teratas:\n", "result")

        for num in random_selected_numbers:
            random_numbers_text.insert(tk.END, f"{num} ", "big")

        filename_label.config(text=f"Nama File: {filename}", fg="green")

# Fungsi untuk membersihkan area hasil
def clear_result():
    result_text.delete(1.0, tk.END)
    random_numbers_text.delete(1.0, tk.END)

# Fungsi untuk keluar dari program
def exit_program():
    root.destroy()

# Membuat jendela utama
root = tk.Tk()
root.title("Analisis Angka")
root.configure(bg="white")

# Membuat frame untuk tombol-tombol
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10)

# Label untuk instruksi upload file
upload_label = tk.Label(root, text="Silahkan masukkan data angka Anda", font=("Helvetica", 14), bg="white")
upload_label.pack()

# Membuat tombol untuk memilih file
browse_button = tk.Button(button_frame, text="Upload File", command=analyze_and_display, font=("Helvetica", 12))
browse_button.pack(side=tk.LEFT, padx=5)

# Membuat tombol "Refresh" untuk membersihkan hasil
refresh_button = tk.Button(button_frame, text="Refresh", command=clear_result, font=("Helvetica", 12))
refresh_button.pack(side=tk.LEFT, padx=5)

# Membuat tombol "Keluar" untuk keluar dari program
exit_button = tk.Button(button_frame, text="Keluar", command=exit_program, font=("Helvetica", 12))
exit_button.pack(side=tk.LEFT, padx=5)

# Label untuk menampilkan nama file yang dipilih
filename_label = tk.Label(root, text="", font=("Helvetica", 12))
filename_label.pack()

# Membuat area teks untuk menampilkan hasil
result_text = tk.Text(root, height=10, width=40, wrap="word")
result_text.pack(pady=10)

# Membuat area teks terpisah untuk menampilkan hasil angka acak
random_numbers_text = tk.Text(root, height=2, width=40, wrap="word")
random_numbers_text.tag_configure("big", font=("Helvetica", 16, "bold"))
random_numbers_text.pack()

# Label dan pilihan untuk jumlah angka acak
num_of_random_label = tk.Label(root, text="Jumlah Angka Acak:", font=("Helvetica", 12), bg="white")
num_of_random_label.pack()

num_of_random_var = tk.IntVar()
num_of_random_var.set(4)  # Default value
num_of_random_entry = tk.Entry(root, textvariable=num_of_random_var, font=("Helvetica", 12))
num_of_random_entry.pack()

# Menjalankan GUI loop
root.mainloop()
