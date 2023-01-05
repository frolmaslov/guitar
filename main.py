from app import app
import views
from app import db
from posts.blueprint import posts


app.register_blueprint(posts, url_prefix='/blog')


if __name__ == '__main__':
    app.run(debug=False)