from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class English(db.Model):
    __searchable__ = ['word', 'translate']
    db_table = '__english__'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(), unique=True)
    translate = db.Column(db.String(), unique=True)

    def __str__(self):
        return f'{self.word} - {self.translate}'
