from flask import Blueprint, render_template, request, redirect, url_for
from blog_app import db
from blog_app.models import Post

posts = Blueprint('posts', __name__, url_prefix='/posts')

@posts.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        post = Post(title=request.form['title'], content=request.form['content'])
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('posts/create.html')