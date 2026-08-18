from customtkinter import *

class TaskManagerApp(CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x500")
        self.title("Personal Task Manager")

        self.title_label = CTkLabel(self, text="Personal Task Manager", font=("Arial", 24))
        self.title_label.pack(pady=(20, 10))

        self.task_entry = CTkEntry(self, placeholder_text="Enter a new task...")
        self.task_entry.pack(pady=20, padx=20, fill="x")

        self.add_button = CTkButton(self, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=10, padx=10)

        self.error_label = CTkLabel(self, text="", text_color="red")
        self.error_label.pack()

        self.tasks_frame = CTkScrollableFrame(self, width=500, height=200)
        self.tasks_frame.pack(pady=15, padx=10)

        self.total_tasks = 0
        self.completed_tasks = 0
        self.stats_label = CTkLabel(self, text="Tasks: 0 | Completed: 0", font=("Arial", 14))
        self.stats_label.pack(pady=10)
        
    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text == "":
            self.error_label.configure(text="Завдання не може бути порожнім!")
            return
        
        self.error_label.configure(text="")

        

        task_frame = CTkFrame(self.tasks_frame)
        task_frame.pack(pady=5, padx=10, fill="x")

        task_checkbox = CTkCheckBox(task_frame, text=task_text, font=("Arial", 16),command=lambda: self.complete_task(task_checkbox))
        task_checkbox.pack(pady=5, padx=20, side="left")

        delete_button = CTkButton(task_frame, text="Delete", width=80,fg_color="red", hover_color="darkred", command=lambda: self.delete_task(task_frame, task_checkbox))
        delete_button.pack(side="right", padx=10, pady=5)

        self.total_tasks += 1
        self.update_stats()

        self.task_entry.delete(0, "end")
    def delete_task(self, task_frame, task_checkbox):
        self.total_tasks -= 1

        if task_checkbox.get() == 1:
            self.completed_tasks -= 1

        task_frame.destroy()
        self.update_stats()

    def complete_task(self, checkbox):
        if checkbox.get() == 1:
            checkbox.configure(text_color = "grey")
            self.completed_tasks += 1
        else:
            checkbox.configure(text_color = "white")
            self.completed_tasks -= 1
        self.update_stats()
    def update_stats(self):
        self.stats_label.configure(text=f"Tasks: {self.total_tasks} | Completed: {self.completed_tasks}")
TaskManagerApp().mainloop()