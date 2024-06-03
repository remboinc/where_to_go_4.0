# Сайт для поиска интересных мест в Москве
Сайт предназначен для добавления и поиска интересных мест в Москве. 
Создан не фреймворке Django.

Ссылка на работающий сайт: https://remboinc.pythonanywhere.com/

Админ панель: https://remboinc.pythonanywhere.com/admin

Данные были взяты с сайта [kudago.com](https://kudago.com/)

## С чего начать
Склонируйте репозиторий

```
git clone https://github.com/remboinc/where_to_go_4.0.git
```
Перейдите в директорию проекта

```commandline
cd /where_to_go_4.0
```
Установите зависимости
```commandline
pip install -r requirements.txt
```
После вам нужно создать локальную базу данных
```commandline
python manage.py migrate
```
Создать суперюзера в ней 
```commandline
python manage.py createsuperuser
```
Следуйте инструкциям в терминале.

Все готово, осталось запустить локальный сервер
```commandline
python manage.py runserver
```
В терминале вы увидите тако сообщение
```commandline
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 03, 2024 - 20:39:23
Django version 4.2.13, using settings 'where_to_go.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

``` 
Все работает! Можно переходить в админку и добавлять интересные места.