
"""
Файл: main.py

Назначение:
Главный модуль системы учёта времени.

Описание:
Обеспечивает взаимодействие пользователя с программой,
объединяет модули управления задачами, учёта времени
и формирования отчётов.

Основные возможности:
- Создание задач.
- Просмотр списка задач.
- Запуск и остановка таймера.
- Завершение задач.
- Формирование и сохранение отчётов.
"""

from task_manager import TaskManager
from reports import ReportGenerator


def main():
    """Запускает главное меню программы."""

    manager = TaskManager()
    reporter = ReportGenerator(manager)

    while True:
        print("\n===== СИСТЕМА УЧЁТА ВРЕМЕНИ =====")
        print("1. Создать задачу")
        print("2. Показать все задачи")
        print("3. Запустить таймер")
        print("4. Остановить таймер")
        print("5. Завершить задачу")
        print("6. Сформировать отчёт")
        print("7. Сохранить отчёт")
        print("0. Выход")

        choice = input("Выберите действие: ")

        try:
            if choice == "1":
                title = input("Введите название задачи: ")
                description = input("Описание задачи: ")

                manager.create_task(title, description)

            elif choice == "2":
                tasks = manager.list_tasks()

                if not tasks:
                    print("Список задач пуст.")
                else:
                    for task in tasks:
                        print(
                            f"ID: {task['id']} | "
                            f"Название: {task['title']} | "
                            f"Статус: {task['status']}"
                        )

            elif choice == "3":
                task_id = int(input("Введите ID задачи: "))
                manager.start_task(task_id)

            elif choice == "4":
                elapsed = manager.stop_task()
                print(f"Затрачено секунд: {elapsed:.2f}")

            elif choice == "5":
                task_id = int(input("Введите ID задачи: "))
                manager.complete_task(task_id)

            elif choice == "6":
                print("\n" + reporter.generate_report())

            elif choice == "7":
                filename = input(
                    "Введите имя файла (Enter — time_report.txt): "
                ).strip()

                if not filename:
                    filename = "time_report.txt"

                reporter.save_report(filename)

            elif choice == "0":
                print("Работа программы завершена.")
                break

            else:
                print("Неверный пункт меню.")

        except (ValueError, KeyError) as error:
            print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()

