from .models import Post
from . import db
from flask import abort


def create_post(title, content):
    new_post = Post(title=title, content=content)
    db.session.add(new_post)
    db.session.commit()


def get_post_by_id(post_id):
    return Post.query.get_or_404(post_id)


def update_post(post, new_title, new_content):
    post.title = new_title
    post.content = new_content
    db.session.commit()


def delete_post(post):
    db.session.delete(post)
    db.session.commit()


