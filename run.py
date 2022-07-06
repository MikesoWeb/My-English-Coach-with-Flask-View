from english import app_ctx, db

# импорт марншрутов для работы приложения
from english.routes import IndexView

if __name__ == '__main__':
    with app_ctx.app_context():
        db.create_all()
    app_ctx.run()
