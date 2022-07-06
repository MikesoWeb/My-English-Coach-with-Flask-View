from flask.views import View, MethodView
from markupsafe import Markup
from sqlalchemy.exc import IntegrityError

from english import app_ctx
from english.models import English, db
from flask import render_template, request, flash, url_for, redirect


@app_ctx.errorhandler(404)
def page_not_found(e):
    return render_template('english/404.html')


@app_ctx.errorhandler(500)
def page_not_found(e):
    return render_template('english/500.html')


class IndexView(View):
    def __init__(self, template_name, title):
        self.template_name = template_name
        self.title = title

    def dispatch_request(self):
        count = English.query.count()
        from sqlalchemy.sql.expression import func, select
        random_word = English.query.order_by(func.random()).first()
        return render_template(self.template_name, title=self.title, count=count, random_word=random_word)


class AddView(MethodView):

    def __init__(self, template_name, title):
        self.template_name = template_name
        self.title = title

    def get(self):
        return render_template(self.template_name, title=self.title)

    def post(self):
        if request.method == 'POST':
            word = request.form['word'].capitalize()
            translate = request.form['translate'].capitalize()
            print(word, translate)
            try:
                add_word = English(word=word, translate=translate)
                db.session.add(add_word)
                db.session.commit()
                message = Markup(f'Слово <mark>{word}</mark> и его перевод <mark>{translate}</mark> добавлено')
                flash(message, category='success')
                return redirect(url_for('add'))

            except IntegrityError:
                flash(f'Слово {word} в базе существует!', category='danger')

        return render_template(self.template_name, title=self.title)


class ChangeView(MethodView):

    def __init__(self, template_name, title):
        self.template_name = template_name
        self.title = title

    def get(self):
        return render_template(self.template_name, title=self.title)

    def post(self):
        if request.method == 'POST':
            word = request.form['word'].capitalize()
            word_update = English.query.filter_by(word=word).first()
            if word_update:
                translate_update = request.form['translate']
                word_update.translate = translate_update
                db.session.commit()
                message = Markup(f'У слова <mark>{word}</mark> был обновлен перевод на <mark>{translate_update}</mark>')
                flash(message, category='warning')
            else:
                message = Markup(f'Слово <mark>{word}</mark> не найдено в базе!')
                flash(message, category='error')

        return render_template(self.template_name, title=self.title)


class DeleteView(MethodView):
    def __init__(self, template_name, title):
        self.template_name = template_name
        self.title = title

    def get(self):
        return render_template(self.template_name, title=self.title)

    def post(self):
        if request.method == 'POST':
            word = request.form['word']
            print(word)
            word_delete = English.query.filter_by(word=word).first()
            if word_delete:
                db.session.delete(word_delete)
                db.session.commit()
                message = Markup(f'Слово <mark>{word}</mark> удалено!')
                flash(message, category='success')
            else:
                message = Markup(f'Слово <mark>{word}</mark> в базе не найдено!')
                flash(message, category='error')

        return render_template(self.template_name, title=self.title)


class ShowView(MethodView):
    def __init__(self, template_name, title):
        self.template_name = template_name
        self.title = title

    def dispatch_request(self, *args, **kwargs):
        page = request.args.get('page', 1, type=int)
        posts = English.query.paginate(page=page, per_page=10)

        return render_template(self.template_name, title=self.title, posts=posts)


#  https://github.com/MikesoWeb/my_english_couch_flask_peewee


class AboutView(View):
    def __init__(self, template_name, title):
        self.template_name = template_name
        self.title = title

    def dispatch_request(self):
        return render_template(self.template_name, title=self.title)


@app_ctx.route('/search')
def search():
    try:
        keyword = request.args.get('q')
        print('keyword', keyword)
        searching = English.query.msearch(keyword, fields=['word', 'translate'], limit=10)
        if not searching:
            message = Markup(f'Слово <mark>{keyword}</mark> в базе не найдено!')
            flash(message, category='error')
        return render_template('english/result_search.html', searching=searching, keyword=keyword)
    except AttributeError:
        return redirect(url_for('index'))
