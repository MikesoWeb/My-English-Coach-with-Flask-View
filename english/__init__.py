import os

from flask import Flask
from flask_bootstrap import Bootstrap5
from english.models import db, English
from flask_msearch import Search
from flask_migrate import Migrate

bootstrap5 = Bootstrap5()
search = Search()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object('english.settings.ConfigProd')
    db.init_app(app)
    with app.app_context():
        if db.engine.url.drivername == 'sqlite':
            migrate.init_app(app, db, render_as_batch=True)
        else:
            migrate.init_app(app, db)

    bootstrap5.init_app(app)
    search.init_app(app)
    return app


app_ctx = create_app()
