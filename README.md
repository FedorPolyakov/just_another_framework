# just_another_framework
**Для запуска сайта нужно запустить команды:**
1. Перейти в папку с проектом
1. открыть терминал
1. для запуска при помощи uwsgi ввести: sudo uwsgi --http :8000 --wsgi-file main.py
1. для запуска при помощи gunicorn ввести: sudo gunicorn main:application
