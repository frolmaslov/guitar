from app import app, migrate
from main import *


def create_app():
    db.init_app(app)
    migrate.init_app(app, db)
    return app


if __name__ == '__main__':
    create_app()