from english import app_ctx, db

from english.routes import IndexView

if __name__ == '__main__':
    with app_ctx.app_context():
        db.create_all()
    app_ctx.run()
