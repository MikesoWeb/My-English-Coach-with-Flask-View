My English Coach on Flask View with PostgreSQL and Sqlite

![Image_alt](https://sun1.userapi.com/sun1-23/s/v1/ig2/KNHIgxcorRJxnGcSG2fk-JpuEhc97DYxnB9TycC2ILZukM6nnK1GVtAzIcn6zy0mEB233GKME69R-Wsi5Kws5D5D.jpg?size=1280x690&quality=96&type=album)

Цель приложения:

    Показать работу Flask View на реальном примере работающего веб-приложения на flask
    Переписать своё старое приложение на flask, использующее ORM peewee
    Работа как с PostgreSQL так и с Sqlite

Используются модули:

    flask
    flask-migrate
    flask-sqlalchemy
    flask-msearch
    bootstrap-flask
    python-dotenv

Установка модулей 

    pip install flask flask-migrate flask-sqlalchemy flask-msearch bootstrap-flask python-dotenv psycopg2-binary gunicorn

Зависимости:

    pip install -r requirements.txt

Структура проекта

    cd english &
    md templates static & cd static &
    md css favicon img_404 img_500 search_404 &
    cd css & echo *{}> style.css & cd .. & cd ..&
    cd templates & md english & cd .. & cd .. &
    echo from flask import Flask >  run.py &
    echo .> .env & echo .> .gitignore
    
    for %i in (models routes views settings) do notepad %i.py

Публикую базу данных, хотя в идеальном мире она должна находиться в файле .gitignore
Так же публикую файл .env с настройками, который должен так же находиться в .gitignore

Для публикации на heroku

    Procfile
    pip install gunicorn

Ссылки:

1. [Ролик о Flask View] (https://github.com/MikesoWeb/flask_view_CRUD_app)
2. [Ролик по этому приложению] (https://youtu.be/ve9xEMOQKeQ)
3. [Git repo] (https://github.com/MikesoWeb/My-English-Coach-with-Flask-View)
4. [Пост ВК] (https://vk.com/python_for_me?w=wall-184890296_694%2Fall)
5. [На pythonanywhere] (http://doyouknow.pythonanywhere.com/)
6. [На heroku] (https://my-english-coach.herokuapp.com/)

    [Михаил Терехов 2022]  

