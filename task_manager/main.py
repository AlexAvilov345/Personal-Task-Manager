from customtkinter import *
from PIL import Image

class TaskManagerApp(CTk):
    def __init__(self):
        super().__init__()


        self.geometry("600x550")
        self.resizable(False, False)
        self.title("Personal Task Manager")

        

        self.title_label = CTkLabel(self, text="Personal Task Manager",  font=("Arial", 28, "bold"), )
        self.title_label.pack(pady=(20, 10))

        self.task_entry = CTkEntry(self,
            placeholder_text="Enter a new task...",
            height=40,
            corner_radius=10,
            border_width=2,
            border_color="#4a90e2",
        )
        self.task_entry.pack(pady=20, padx=20, fill="x")

        self.add_button = CTkButton(self, text="Add Task", command=self.add_task, border_width=2, border_color="#4a90e2", fg_color="#4a90e2", hover_color="#357ABD", height=40, corner_radius=10)
        self.add_button.pack(pady=10, padx=10)

        self.dark_icon = CTkImage(light_image=Image.open("task_manager//img//dark-mode.png"),dark_image=Image.open("task_manager//img//dark-mode.png"), size=(24, 24))
        self.light_icon = CTkImage(light_image=Image.open("task_manager//img//light-mode.png"),dark_image=Image.open("task_manager//img//light-mode.png"), size=(24, 24))

        self.theme_btn = CTkButton(self, text="",image=self.dark_icon, command=self.toggle_theme, width=40, height=40)
        self.theme_btn.place(x=540, y=10)

        self.is_dark_mode = True

        self.error_label = CTkLabel(self, text="", text_color="red")
        self.error_label.pack()

        self.tasks_frame = CTkScrollableFrame(self, width=500, height=200, corner_radius=10, border_width=2, border_color="#4a90e2")
        self.tasks_frame.pack(pady=10, padx=10)

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

    def toggle_theme(self):
        if self.is_dark_mode:
            set_appearance_mode("light")
            self.theme_btn.configure(image=self.light_icon)
            self.is_dark_mode = False
        else:
            set_appearance_mode("dark")
            self.theme_btn.configure(image=self.dark_icon)
            self.is_dark_mode = True

TaskManagerApp().mainloop()