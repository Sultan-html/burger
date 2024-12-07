#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    
    # Если в аргументах передана команда для запуска бота
    if len(sys.argv) > 1 and sys.argv[1] == 'run_telegram_bot':
        # Импортируем функцию для запуска бота
        from apps.telegram import run_telegram_bot  # Заменить на правильный путь
        print("Starting Telegram bot...")
        run_telegram_bot()  # Запуск бота
    else:
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc
        execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
