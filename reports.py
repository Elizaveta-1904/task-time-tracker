"""
Файл: reports.py

Назначение:
Модуль формирования отчётов о затраченном времени.

Описание:
Модуль собирает информацию о задачах,
их статусах и затраченном времени.
Позволяет формировать общий отчёт
и сохранять его в текстовый файл.
"""
from datetime import datetime


class ReportGenerator:
    """Класс для формирования отчётов о затраченном времени."""

    def __init__(self, task_manager):
        self.task_manager = task_manager

    def generate_report(self):
        """Формирует общий отчёт по всем задачам."""
        tasks = self.task_manager.list_tasks()

        if not tasks:
            return "Нет задач для формирования отчёта."

        report = []
        report.append("ОТЧЁТ ПО УЧЁТУ РАБОЧЕГО ВРЕМЕНИ")
        report.append("=" * 45)
        report.append(
            f"Дата формирования: {datetime.now().strftime('%d.%m.%Y %H:%M')}"
        )
        report.append("")

        total_time = 0

        for task in tasks:
            task_id = task["id"]
            task_time = self.task_manager.get_task_time(task_id)
            formatted_time = self.task_manager.timer.format_time(task_id)

            total_time += task_time

            report.append(f"Задача: {task['title']}")
            report.append(f"ID: {task_id}")
            report.append(f"Статус: {task['status']}")
            report.append(f"Затраченное время: {formatted_time}")
            report.append("-" * 45)

        hours = int(total_time) // 3600
        minutes = (int(total_time) % 3600) // 60
        seconds = int(total_time) % 60

        report.append(
            f"Общее время: {hours:02d}:{minutes:02d}:{seconds:02d}"
        )

        return "\n".join(report)

    def save_report(self, filename="time_report.txt"):
        """Сохраняет отчёт в текстовый файл."""
        report = self.generate_report()

        with open(filename, "w", encoding="utf-8") as file:
            file.write(report)

        print(f"Отчёт сохранён в файл: {filename}")

