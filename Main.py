from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.listview import ListView
from kivy.adapters.listadapter import ListAdapter
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
import json
from datetime import datetime

# Класс для управления списком задач
class TaskList(BoxLayout):
    def __init__(self, **kwargs):
        super(TaskList, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.spacing = 10
        self.padding = 10

        # Загрузка задач из файла
        self.tasks = self.load_tasks()

        # Создание списка задач
        self.list_adapter = ListAdapter(
            data=[f"{task['task']} ({task['category']})" for task in self.tasks],
            cls=TaskItem,
            selection_mode="single",
            allow_empty_selection=True
        )
        self.list_view = ListView(adapter=self.list_adapter)
        self.add_widget(self.list_view)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def add_task(self, task, category, repeat, start_date):
        new_task = {
            "task": task,
            "category": category,
            "repeat": repeat,
            "start_date": start_date,
            "completed": False
        }
        self.tasks.append(new_task)
        self.list_adapter.data.append(f"{task} ({category})")
        self.list_adapter.data_changed()
        self.save_tasks()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            del self.list_adapter.data[index]
            self.list_adapter.data_changed()
            self.save_tasks()


class TaskItem(BoxLayout):
    text = StringProperty("")
    completed = BooleanProperty(False)

    def toggle_completed(self, index, task_list):
        task_list.tasks[index]["completed"] = not task_list.tasks[index]["completed"]
        task_list.save_tasks()


class ToDoApp(App):
    def build(self):
        self.title = "To-Do List"
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        # Ввод новой задачи
        input_layout = BoxLayout(orientation="horizontal", spacing=10)
        self.task_input = TextInput(hint_text="Enter task", multiline=False)
        self.category_spinner = Spinner(text="Work", values=("Work", "Personal", "Shopping"))
        self.repeat_spinner = Spinner(text="None", values=("None", "Daily", "Weekly", "Monthly", "Yearly"))
        self.date_button = Button(text="Select Date", size_hint=(None, 1), width=100, on_release=self.show_date_picker)
        self.add_button = Button(text="Add Task", on_release=self.add_task)
        input_layout.add_widget(self.task_input)
        input_layout.add_widget(self.category_spinner)
        input_layout.add_widget(self.repeat_spinner)
        input_layout.add_widget(self.date_button)
        input_layout.add_widget(self.add_button)

        # Список задач
        self.task_list = TaskList()
        layout.add_widget(input_layout)
        layout.add_widget(self.task_list)

        return layout

    def show_date_picker(self, instance):
        content = BoxLayout(orientation="vertical")
        date_input = TextInput(hint_text="YYYY-MM-DD", multiline=False)
        save_button = Button(text="Save", size_hint=(1, None), height=50, on_release=lambda btn: self.set_date(date_input.text))
        content.add_widget(date_input)
        content.add_widget(save_button)

        popup = Popup(title="Select Date", content=content, size_hint=(None, None), size=(300, 200))
        save_button.bind(on_release=popup.dismiss)
        popup.open()

    def set_date(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            self.date_button.text = date_str
        except ValueError:
            self.date_button.text = "Invalid Date"

    def add_task(self, instance):
        task = self.task_input.text.strip()
        category = self.category_spinner.text
        repeat = self.repeat_spinner.text
        start_date = self.date_button.text

        if task and start_date != "Select Date" and start_date != "Invalid Date":
            self.task_list.add_task(task, category, repeat, start_date)
            self.task_input.text = ""
            self.date_button.text = "Select Date"


if __name__ == "__main__":
    ToDoApp().run()
