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
        self.add_button.pack(pady=20, padx=10)

        self.error_label = CTkLabel(self, text="", text_color="red")
        self.error_label.pack()

        self.tasks_frame = CTkScrollableFrame(self, width=500, height=300)
        self.tasks_frame.pack(pady=15, padx=10)

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

        delete_button = CTkButton(task_frame, text="Delete", width=80,fg_color="red", hover_color="darkred", command=task_frame.destroy)
        delete_button.pack(side="right", padx=10, pady=5)

        self.task_entry.delete(0, "end")

    def complete_task(self, checkbox):
        if checkbox.get() == 1:
            checkbox.configure(text_color = "grey")
        else:
            checkbox.configure(text_color = "white")
TaskManagerApp().mainloop()