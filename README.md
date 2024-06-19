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
Настройте переменные окружения:
```
SECRET_KEY='<Ваш секретный ключ проекта>'
ALLOWED_HOSTS=hosts.com
DB_ENGINE=db
DB_NAME=<Имя вашей бд>
STATIC_URL=<Адрес статики>
MEDIA_URL=<Адрес медиа файлов>
STATICFILES_DIRS=<Директория хранения статики>
STATIC_ROOT=<Путь к статике>
```
Подрбное описание переменных окружения:

`SECRET_KEY`: Секретный ключ вашего Django проекта, который используется для криптографических подписей. Он должен быть уникальным и сохранён в секрете.

`ALLOWED_HOSTS`: Список хостов/доменов, которые Django будет обслуживать. Включение вашего домена в этот список защищает от некоторых атак.

`DB_ENGINE`: Движок базы данных, который используется вашим проектом (например, 'django.db.backends.postgresql' для PostgreSQL).

`DB_NAME`: Имя базы данных, которая используется вашим проектом.

`STATIC_URL`: URL-адрес, по которому будут доступны ваши статические файлы.

`MEDIA_URL`: URL-адрес, по которому будут доступны ваши медиа файлы, загружаемые пользователями.

`STATICFILES_DIRS`: Список директорий (кроме STATIC_ROOT), где Django будет искать статические файлы.

`MEDIA_ROOT`: Абсолютный путь к директории на файловой системе, где будут храниться загружаемые медиа файлы.


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
В терминале вы увидите такое сообщение
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

Чтобы быстро добавить интересные места из JSON файла, нужно запустить команду 
```commandline
python manage.py load_place http://адрес/файла.json
```
Пример того, как должна выглядеть стуктура json файла
```commandline
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```

