from flask import Flask, render_template, url_for, request, redirect, g, session, flash
from form_contact import ContactForm, csrf
from flask_mail import Mail, Message
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemyUserDatastore, Security, current_user
from config import Config
from flask_migrate import Migrate
from flask_babelex import Babel



app = Flask(__name__)


babel = Babel(app)

csrf.init_app(app)
app.config.from_object(Config)


db = SQLAlchemy(app)
from models import *
migrate = Migrate(app, db)


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin,AdminIndexView):
    pass


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        if is_created:
            model.generate_slug()
        return super().on_model_change(form, model, is_created)


class PostAdminView(AdminMixin, BaseModelView):
    pass


class TagAdminView(AdminMixin, BaseModelView):
    pass


admin = Admin(app, 'Гитара', url='/', index_view=HomeAdminView(name='Home'))

admin.add_view(PostAdminView(Post, db.session))
admin.add_view(TagAdminView(Tag, db.session))

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'frolmaslov@gmail.com'
app.config['MAIL_PASSWORD'] = 'jonyofpcuovqrtpi'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['SESSION_COOKIE_SECURE'] = False

mail = Mail()
mail.init_app(app)

# Flask Security

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


@babel.localeselector
def get_locale():
    if request.args.get('lang'):
        session['lang'] = request.args.get('lang')
    return session.get('lang', 'ru')



#
# class Article(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     intro = db.Column(db.String(300), nullable=False)
#     text = db.Column(db.Text, nullable=False)
#     date = db.Column(db.DateTime, default=datetime.utcnow)









