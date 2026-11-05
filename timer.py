
import time


class Timer:
    """Класс для учёта времени выполнения задач."""

    def __init__(self):
        self.active_task = None
        self.start_time = None
        self.total_time = {}

    def start(self, task_id):
        """Запускает таймер для выбранной задачи."""
        if self.active_task is not None:
            raise ValueError("Сначала остановите предыдущий таймер.")

        self.active_task = task_id
        self.start_time = time.monotonic()

        print(f"Таймер задачи {task_id} запущен.")

    def stop(self):
        """Останавливает таймер и сохраняет затраченное время."""
        if self.active_task is None:
            raise ValueError("Нет активного таймера.")

        elapsed = time.monotonic() - self.start_time

        self.total_time[self.active_task] = (
            self.total_time.get(self.active_task, 0) + elapsed
        )

        task_id = self.active_task
        self.active_task = None
        self.start_time = None

        print(f"Таймер задачи {task_id} остановлен.")
        return elapsed

    def get_total_time(self, task_id):
        """Возвращает общее время выполнения задачи."""
        total = self.total_time.get(task_id, 0)

        if self.active_task == task_id:
            total += time.monotonic() - self.start_time

        return total

    def format_time(self, task_id):
        """Форматирует время в часы, минуты и секунды."""
        seconds = int(self.get_total_time(task_id))

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60

        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
