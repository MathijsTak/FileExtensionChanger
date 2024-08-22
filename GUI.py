import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
from ChangeFiles import change_extensions, count_files_with_extension
from CheckFile import count_video_files, check_files

def browse_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory)

def change_extensions_gui():
    directory = directory_entry.get()
    old_ext = old_ext_entry.get()
    new_ext = new_ext_entry.get()
    include_subdirs = subdirs_var_ext.get()

    if not directory or not old_ext or not new_ext:
        messagebox.showerror("Error", "Please fill in all fields")
        return

    total_files = count_files_with_extension(directory, old_ext, include_subdirs)
    if total_files == 0:
        messagebox.showinfo("No Files", f"No files with extension {old_ext} found in the selected directory.")
        return

    progress_window = tk.Toplevel(root)
    progress_window.title("Changing File Extensions")
    progress_label = tk.Label(progress_window, text="Changing file extensions...")
    progress_label.pack(pady=10)
    progress_bar = ttk.Progressbar(progress_window, mode='determinate', length=300, maximum=total_files)
    progress_bar.pack(pady=10, padx=20)

    def update_progress(value):
        progress_bar['value'] = value
        progress_label.config(text=f"Changing file extensions... ({value}/{total_files})")
        progress_window.update_idletasks()

    def run_change():
        nonlocal progress_window
        changed_files = change_extensions(directory, old_ext, new_ext, include_subdirs, update_progress)
        progress_window.destroy()
        messagebox.showinfo("Success", f"{changed_files} file(s) changed from {old_ext} to {new_ext} in {directory}")

    thread = threading.Thread(target=run_change)
    thread.start()

def check_files_gui():
    directory = directory_entry.get()
    include_subdirs = subdirs_var_check.get()

    if not directory:
        messagebox.showerror("Error", "Please select a directory")
        return

    total_files = count_video_files(directory, include_subdirs)
    if total_files == 0:
        messagebox.showinfo("No Video Files", "No video files found in the selected directory.")
        return

    progress_window = tk.Toplevel(root)
    progress_window.title("Checking Video Files")
    progress_label = tk.Label(progress_window, text="Checking video files...")
    progress_label.pack(pady=10)
    progress_bar = ttk.Progressbar(progress_window, mode='determinate', length=300, maximum=total_files)
    progress_bar.pack(pady=10, padx=20)

    def update_progress(value):
        progress_bar['value'] = value
        progress_label.config(text=f"Checking video files... ({value}/{total_files})")
        progress_window.update_idletasks()

    def run_check():
        nonlocal progress_window
        checked_files, corrupted_files = check_files(directory, include_subdirs, update_progress)
        progress_window.destroy()
        if corrupted_files:
            result = f"Found {len(corrupted_files)} corrupted video file(s) out of {checked_files} checked:\n\n"
            result += "\n".join(corrupted_files)
            messagebox.showwarning("Corrupted Video Files", result)
        else:
            messagebox.showinfo("Check Complete", f"All {checked_files} video files are openable and not corrupted.")

    thread = threading.Thread(target=run_check)
    thread.start()

# Create main window
root = tk.Tk()
root.title("File Operations")

# Create and place widgets
tk.Label(root, text="Directory:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
directory_entry = tk.Entry(root, width=50)
directory_entry.grid(row=0, column=1, columnspan=3, padx=5, pady=5)
tk.Button(root, text="Browse", command=browse_directory).grid(row=0, column=4, padx=5, pady=5)

# File Extension Changer section
tk.Label(root, text="File Extension Changer", font=("", 12, "bold")).grid(row=1, column=0, columnspan=2, pady=5)

tk.Label(root, text="Old Extension:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
old_ext_entry = tk.Entry(root)
old_ext_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

tk.Label(root, text="New Extension:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
new_ext_entry = tk.Entry(root)
new_ext_entry.grid(row=3, column=1, sticky="w", padx=5, pady=5)

subdirs_var_ext = tk.BooleanVar()
subdirs_check_ext = ttk.Checkbutton(root, text="Include Subdirectories", variable=subdirs_var_ext)
subdirs_check_ext.grid(row=4, column=1, sticky="w", padx=5, pady=5)

tk.Button(root, text="Change Extensions", command=change_extensions_gui).grid(row=5, column=1, pady=10)

# Vertical Separator
ttk.Separator(root, orient='vertical').grid(row=1, column=2, rowspan=5, sticky="ns", padx=10)

# Video File Checker section
tk.Label(root, text="Video File Checker", font=("", 12, "bold")).grid(row=1, column=3, columnspan=2, pady=5)

subdirs_var_check = tk.BooleanVar()
subdirs_check_check = ttk.Checkbutton(root, text="Include Subdirectories", variable=subdirs_var_check)
subdirs_check_check.grid(row=2, column=3, sticky="w", padx=5, pady=5)

tk.Button(root, text="Check Video Files", command=check_files_gui).grid(row=3, column=3, pady=10)

if __name__ == "__main__":
    root.mainloop()