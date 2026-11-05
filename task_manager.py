"""
Файл: task_manager.py

Назначение:
Модуль управления задачами системы.

Описание:
Модуль предназначен для создания, хранения
и управления задачами. Обеспечивает просмотр
списка задач, изменение их статусов,
запуск и остановку таймера.

Основные возможности:
- Создание новых задач.
- Получение информации о задачах.
- Просмотр списка задач.
- Запуск и остановка учёта времени.
- Завершение задач.
- Получение общего затраченного времени.
"""
"""
Файл: task_manager.py

Назначение:
Модуль управления задачами системы.
"""
from timer import Timer


class TaskManager:
    """Класс для управления задачами и учёта времени."""

    def __init__(self):
        self.tasks = {}
        self.timer = Timer()
        self.next_id = 1

    def create_task(self, title, description=""):
        """Создаёт новую задачу."""
        if not title.strip():
            raise ValueError("Название задачи не может быть пустым.")

        task_id = self.next_id

        self.tasks[task_id] = {
            "id": task_id,
            "title": title,
            "description": description,
            "status": "Новая"
        }

        self.next_id += 1

        print(f"Задача '{title}' создана. ID: {task_id}")
        return task_id

    def get_task(self, task_id):
        """Возвращает информацию о задаче."""
        if task_id not in self.tasks:
            raise ValueError("Задача не найдена.")

        return self.tasks[task_id]

    def list_tasks(self):
        """Возвращает список всех задач."""
        return list(self.tasks.values())

    def start_task(self, task_id):
        """Запускает учёт времени по задаче."""
        task = self.get_task(task_id)

        if task["status"] == "Завершена":
            raise ValueError("Нельзя запустить завершённую задачу.")

        self.timer.start(task_id)
        task["status"] = "В работе"

    def stop_task(self):
        """Останавливает таймер текущей задачи."""
        if self.timer.active_task is None:
            raise ValueError("Нет активной задачи.")

        task_id = self.timer.active_task
        elapsed = self.timer.stop()

        self.tasks[task_id]["status"] = "Приостановлена"

        return elapsed

    def complete_task(self, task_id):
        """Завершает выполнение задачи."""
        task = self.get_task(task_id)

        if self.timer.active_task == task_id:
            self.timer.stop()

        task["status"] = "Завершена"

        print(f"Задача '{task['title']}' завершена.")

    def get_task_time(self, task_id):
        """Возвращает затраченное на задачу время."""
        self.get_task(task_id)
        return self.timer.get_total_time(task_id)

