import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def change_extensions(directory, old_ext, new_ext, include_subdirs):
    changed_files = 0
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(old_ext):
                old_path = os.path.join(root, filename)
                new_filename = os.path.splitext(filename)[0] + new_ext
                new_path = os.path.join(root, new_filename)
                os.rename(old_path, new_path)
                changed_files += 1
        if not include_subdirs:
            break
    return changed_files

def browse_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory)

def change_extensions_gui():
    directory = directory_entry.get()
    old_ext = old_ext_entry.get()
    new_ext = new_ext_entry.get()
    include_subdirs = subdirs_var.get()

    if not directory or not old_ext or not new_ext:
        messagebox.showerror("Error", "Please fill in all fields")
        return

    changed_files = change_extensions(directory, old_ext, new_ext, include_subdirs)
    messagebox.showinfo("Success", f"{changed_files} file(s) changed from {old_ext} to {new_ext} in {directory}")

# Create main window
root = tk.Tk()
root.title("File Extension Changer")

# Create and place widgets
tk.Label(root, text="Directory:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
directory_entry = tk.Entry(root, width=50)
directory_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=browse_directory).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="Old Extension:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
old_ext_entry = tk.Entry(root)
old_ext_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

tk.Label(root, text="New Extension:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
new_ext_entry = tk.Entry(root)
new_ext_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

subdirs_var = tk.BooleanVar()
subdirs_check = ttk.Checkbutton(root, text="Include Subdirectories", variable=subdirs_var)
subdirs_check.grid(row=3, column=1, sticky="w", padx=5, pady=5)

tk.Button(root, text="Change Extensions", command=change_extensions_gui).grid(row=4, column=1, pady=10)

root.mainloop()