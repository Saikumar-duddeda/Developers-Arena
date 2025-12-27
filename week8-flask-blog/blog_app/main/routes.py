from flask import Blueprint, render_template
from blog_app.models import Post

main = Blueprint('main', __name__)

@main.route('/')
def index():
    posts = Post.query.all()
    return render_template('main/index.html', posts=posts)