from english import app_ctx
from english.views import IndexView, AboutView, AddView, ChangeView, DeleteView, ShowView

app_ctx.add_url_rule('/',
                     view_func=IndexView.as_view(name='index',
                                                 template_name='english/index.html', title='Главная страница'))
app_ctx.add_url_rule('/about', view_func=AboutView.as_view(name='about',
                                                           template_name='english/about.html', title='О проекте'))

app_ctx.add_url_rule('/add', view_func=AddView.as_view(name='add',
                                                       template_name='english/add.html', title='Добавить запись'))

app_ctx.add_url_rule('/update', view_func=ChangeView.as_view(name='update',
                                                             template_name='english/update.html',
                                                             title='Обновить запись'))

app_ctx.add_url_rule('/delete', view_func=DeleteView.as_view(name='delete',
                                                             template_name='english/delete.html',
                                                             title='Удалить запись'))

app_ctx.add_url_rule('/show', view_func=ShowView.as_view(name='show',
                                                         template_name='english/show.html',
                                                         title='Посмотреть данные'))
