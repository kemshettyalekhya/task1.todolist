import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")
root.resizable(False, False)

# List to hold tasks
tasks = []

# Function to update the listbox with current tasks
def update_listbox():
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        task_listbox.insert(tk.END, f"{i+1}. {task['text']} [{status}]")

# Add new task
def add_task():
    task_text = task_entry.get().strip()
    if task_text == "":
        messagebox.showwarning("Warning", "Task cannot be empty.")
    else:
        tasks.append({"text": task_text, "completed": False})
        task_entry.delete(0, tk.END)
        update_listbox()

# Mark task as completed
def complete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["completed"] = True
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

# Delete selected task
def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        del tasks[selected_index]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# GUI Layout
title = tk.Label(root, text="To-Do List", font=("Helvetica", 20, "bold"))
title.pack(pady=10)

task_entry = tk.Entry(root, font=("Helvetica", 14))
task_entry.pack(pady=10, padx=20, fill=tk.X)

add_button = tk.Button(root, text="Add Task", font=("Helvetica", 12), command=add_task)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, font=("Helvetica", 12), height=10)
task_listbox.pack(pady=10, padx=20, fill=tk.BOTH)

complete_button = tk.Button(root, text="Mark as Completed", font=("Helvetica", 12), command=complete_task)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", font=("Helvetica", 12), command=delete_task)
delete_button.pack(pady=5)

# Start the main GUI loop
root.mainloop()
