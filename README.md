# Блог про відомих жінок

Проект представляє собою блог, присвячений визначним жінкам.

## Стек технологій

- Python
- SQLite
- Django

## Запуск проекту

Для запуску проекту вам слід виконати наступні кроки:

1. **Створення та активація віртуального середовища:**
   ```bash
   python3.9 -m venv ../venv
   source ../venv/bin/activate

2. **Встановлення залежностей**
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
3. **Запуск міграцій, заповнення бази даних фікстурами та запуск сервера**
    ```bash
    ./manage.py migrate
    ./manage.py loaddata <path_to_fixture_files>
    ./manage.py runserver
    ```
