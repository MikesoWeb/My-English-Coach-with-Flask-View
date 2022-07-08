from flask import Flask
from english.models import db, English
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
from flask_msearch import Search

bootstrap5 = Bootstrap5()
migrate = Migrate()
search = Search()


def create_app():
    app = Flask(__name__)
    app.config.from_object('english.settings.ConfigDebug')
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
