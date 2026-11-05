
"""
Файл: test_timer.py

Назначение:
Модуль автоматического тестирования системы учёта времени.

Описание:
Проверяет правильность запуска и остановки таймера,
подсчёт общего времени, обработку ошибок,
а также основные функции управления задачами.
"""

import unittest
from unittest.mock import patch

from timer import Timer
from task_manager import TaskManager


class TestTimer(unittest.TestCase):

    def setUp(self):
        self.timer = Timer()

    @patch("timer.time.monotonic", side_effect=[10, 15])
    def test_start_and_stop(self, mock_time):
        self.timer.start(1)
        elapsed = self.timer.stop()

        self.assertEqual(elapsed, 5)
        self.assertEqual(self.timer.get_total_time(1), 5)

    @patch("timer.time.monotonic", side_effect=[10, 15, 20, 27])
    def test_total_time_after_two_sessions(self, mock_time):
        self.timer.start(1)
        self.timer.stop()

        self.timer.start(1)
        self.timer.stop()

        self.assertEqual(self.timer.get_total_time(1), 12)

    def test_stop_without_start(self):
        with self.assertRaises(ValueError):
            self.timer.stop()

    def test_start_second_timer(self):
        self.timer.start(1)

        with self.assertRaises(ValueError):
            self.timer.start(2)

    @patch("timer.time.monotonic", side_effect=[10, 15])
    def test_format_time(self, mock_time):
        self.timer.start(1)
        self.timer.stop()

        self.assertEqual(self.timer.format_time(1), "00:00:05")


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_create_task(self):
        task_id = self.manager.create_task("Тестовая задача")

        self.assertEqual(task_id, 1)
        self.assertEqual(
            self.manager.get_task(task_id)["title"],
            "Тестовая задача"
        )

    def test_create_empty_task(self):
        with self.assertRaises(ValueError):
            self.manager.create_task("   ")

    def test_task_status(self):
        task_id = self.manager.create_task("Проверка статуса")

        self.manager.start_task(task_id)

        self.assertEqual(
            self.manager.get_task(task_id)["status"],
            "В работе"
        )

    def test_get_unknown_task(self):
        with self.assertRaises(ValueError):
            self.manager.get_task(999)


if __name__ == "__main__":
    unittest.main()

