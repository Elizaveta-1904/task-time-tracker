
"""
Файл: test_main.py

Назначение:
Проверка запуска главного модуля программы.

Описание:
Проверяет, что приложение запускается без ошибок,
отображает главное меню и корректно завершает работу.
"""

import unittest
import subprocess
import sys


class TestMain(unittest.TestCase):

    def test_program_starts_and_exits(self):
        result = subprocess.run(
            [sys.executable, "main.py"],
            input="0\n",
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=10
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("СИСТЕМА УЧЁТА ВРЕМЕНИ", result.stdout)
        self.assertIn("Работа программы завершена.", result.stdout)


if __name__ == "__main__":
    unittest.main()
