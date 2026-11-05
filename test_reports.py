
"""
Файл: test_reports.py

Назначение:
Тестирование модуля формирования отчётов.

Описание:
Проверяет создание отчётов, отображение информации
о задачах и сохранение результатов в текстовый файл.
"""

import unittest
import os
import tempfile

from task_manager import TaskManager
from reports import ReportGenerator


class TestReportGenerator(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()
        self.reporter = ReportGenerator(self.manager)

    def test_empty_report(self):
        report = self.reporter.generate_report()

        self.assertEqual(
            report,
            "Нет задач для формирования отчёта."
        )

    def test_report_contains_task(self):
        self.manager.create_task("Подготовка проекта")

        report = self.reporter.generate_report()

        self.assertIn("Подготовка проекта", report)
        self.assertIn("ОТЧЁТ ПО УЧЁТУ РАБОЧЕГО ВРЕМЕНИ", report)

    def test_report_contains_total_time(self):
        self.manager.create_task("Тестовая задача")

        report = self.reporter.generate_report()

        self.assertIn("Общее время:", report)

    def test_save_report(self):
        self.manager.create_task("Сохранение отчёта")

        with tempfile.TemporaryDirectory() as directory:
            filename = os.path.join(directory, "report.txt")

            self.reporter.save_report(filename)

            self.assertTrue(os.path.exists(filename))

            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()

            self.assertIn("Сохранение отчёта", content)


if __name__ == "__main__":
    unittest.main()
