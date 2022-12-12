from flask import Blueprint, render_template
from models import *
from flask import request
from flask_security import login_required

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def posts_list():
    q = request.args.get('q')
    if q:
        posts = Post.query.filter(Post.title.contains(q) |
                                  Post.body.contains(q))
    else:
        posts = Post.query.order_by(Post.created.desc())

    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    pages = posts.paginate(page=page, per_page=2)

    return render_template('posts/posts.html', posts=posts, pages=pages)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first_or_404()
    return render_template('posts/post_detail.html', post=post)


@posts.route('/tags/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first_or_404()
    return render_template('posts/tag_detail.html', tag=tag)



