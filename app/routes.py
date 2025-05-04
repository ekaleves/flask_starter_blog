from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Post
from .crud import create_post as save_post, get_post_by_id, update_post, delete_post
from . import db


main = Blueprint("main", __name__)


@main.route("/")
def home():
    posts = Post.query.order_by(Post.date_created.desc()).all()
    return render_template("index.html", posts=posts)


@main.route("/create", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if not title or not content:
            flash("Title and content are required!")
            return redirect(url_for("main.create_post"))

        save_post(title, content)

        return redirect(url_for("main.home"))

    return render_template("create.html")


@main.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_post(id):

    post = get_post_by_id(id)

    if request.method == "POST":
        new_title = request.form['title']
        new_content = request.form['content']

        update_post(post, new_title, new_content)

        return redirect(url_for("main.home"))

    return render_template("edit.html", post=post)


@main.route("/delete<int:id>", methods=["POST"])
def delete_post_route(id):
    post = get_post_by_id(id)
    delete_post(post)
    return redirect(url_for("main.home"))










