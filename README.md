# women-site

Короткий опис проекту.

## Стек технологій

- Python
- SQLite
- Django

## Запуск проекту

Для запуску проекту вам слід виконати наступні кроки:

1. Крок один. Створення та активація віртуального середовища
   
```bash
python3.9 -m venv ../venv
source ../venv/bin/activate
```

2. Крок два. Встановлення залежностей
   Встановіть необхідні залежності, використовуючи:
   pip install --upgrade pip
   pip install -r requirements.txt
   
3. Крок три. Запустити залежності проекта, міграції, заповнити базу даних фікстурами і т.д.:
   ./manage.py migrate
   ./manage.py loaddata <path_to_fixture_files>
   ./manage.py runserver
