# Tkinter startup
import tkinter as tk
root = tk.Tk()
root.title("Reminders")
root.geometry("500x400")

# import reminders from JSON file
import json
file_name = 'reminders_storage.json'
try:
    with open(file_name, 'r') as file:
        reminders = json.load(file)
except FileNotFoundError:
    reminders = []
    with open(file_name, 'w') as file:
        json.dump(reminders, file)

# Create the plus widget, the text entry widget, and each reminder
def display():
    global plus_button, text_entry
    for widget in root.winfo_children():
        widget.destroy()
    plus_button = tk.Button(text="+", width=20, height=2, command=add_reminder)
    plus_button.pack()
    text_entry = tk.Text(root, height=1, width=29)
    text_entry.pack()

    for each_reminder in reminders:
        button = tk.Button(root, text=each_reminder.title(), width=20, height=2, command=lambda each_reminder=each_reminder: delete_reminder(each_reminder))
        button.pack()


# saves reminders to JSON file
def save():
    with open(file_name, 'w') as file:
        json.dump(reminders, file)

# deletes the reminder that is clicked on
def delete_reminder(each_reminder):
    reminders.remove(each_reminder)
    save()
    display()

# add a reminder if it is not blank text
def add_reminder():
    new_reminder_text = text_entry.get("1.0", tk.END).strip()
    if new_reminder_text:
        reminders.append(new_reminder_text.lower())
        save()
        display()

display()
root.mainloop()
