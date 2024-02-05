My English Coach on Flask View with PostgreSQL and Sqlite

![Image_alt](https://sun1.userapi.com/sun1-23/s/v1/ig2/KNHIgxcorRJxnGcSG2fk-JpuEhc97DYxnB9TycC2ILZukM6nnK1GVtAzIcn6zy0mEB233GKME69R-Wsi5Kws5D5D.jpg?size=1280x690&quality=96&type=album)


Цель приложения:

    - Показать работу Flask View на реальном примере работающего веб-приложения на flask
    - Переписать своё старое приложение на flask, использующее ORM peewee
    - Показать работу как с PostgreSQL так и с Sqlite


Используются модули:

    flask
    flask-migrate
    flask-sqlalchemy
    flask-msearch
    bootstrap-flask
    python-dotenv
    psycopg2-binary
    gunicorn
    

Установка модулей 

    pip install flask flask-migrate flask-sqlalchemy flask-msearch bootstrap-flask python-dotenv psycopg2-binary gunicorn


Зависимости:

    pip install -r requirements.txt


Структура проекта

    Создадим пакет english (папка english с файлом __init__.py внутри)

    md english & cd english &
    md templates static & cd static &
    md css favicon img_404 img_500 search_404 &
    cd css & echo *{}> style.css & cd .. & cd ..&
    cd templates & md english & cd .. & cd .. &
    echo from flask import Flask >  run.py &
    echo .> .env & echo .> .gitignore

    Эту строку с циклом после создания основной структуры
    `for %i in (models routes views settings) do notepad %i.py`


Публикую базу данных, хотя в идеальном мире она должна находиться в файле `.gitignore`
Так же публикую файл `.env` с настройками, который не должен публиковаться в репозитории , а должен так же находиться в `.gitignore`. 
Но здесь я его публикую для примера использования переменных окружения проекта. Обычно это публикуется в файле `.env-example`


Для публикации на heroku

    Procfile
    pip install gunicorn


Ссылки:

1. [Ролик о Flask View] (https://youtu.be/iaHeGzg9H08)
2. [Ролик по этому приложению] (https://youtu.be/ve9xEMOQKeQ)
3. [Git repo] (https://github.com/MikesoWeb/My-English-Coach-with-Flask-View)
4. [Пост ВК] (https://vk.com/python_for_me?w=wall-184890296_694%2Fall)

    [Михаил Терехов 2022]  

