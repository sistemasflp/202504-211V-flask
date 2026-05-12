from flask import Blueprint, render_template, request, redirect, url_for, abort
from app.models.post import (
    fetch_all_posts,
    fetch_post_by_id,
    create_post as create_post_model,
    update_post as update_post_model,
    delete_post as delete_post_model,
)

post_bp = Blueprint('post', __name__, url_prefix='/post')


@post_bp.route("/list")
def get_all_posts():
    posts = fetch_all_posts()
    return render_template("post/list.html", post_list=posts)


@post_bp.route("/api/list", methods=["GET"])
def get_all_posts_json():
    posts = fetch_all_posts()
    return render_template("partials/datos-json.html", post_list=posts)


@post_bp.route("/<int:post_id>")
def get_single_post(post_id):
    post = fetch_post_by_id(post_id)
    if post is None:
        abort(404)
    return render_template("post/single.html", post_single=post)


@post_bp.route("/create", methods=("GET", "POST"))
def create_post():
    if request.method == "GET":
        return render_template("post/create.html")
    title = request.form["title_title"]
    content = request.form["content_content"]
    create_post_model(title, content)
    return redirect(url_for("post.get_all_posts"))


@post_bp.route("/update/<int:post_id>", methods=("GET", "POST"))
def update_post(post_id):
    post = fetch_post_by_id(post_id)
    if post is None:
        abort(404)
    if request.method == "GET":
        return render_template("post/update.html", single_post=post)
    title = request.form["title_title"]
    content = request.form["content_content"]
    update_post_model(post_id, title, content)
    return redirect(url_for("post.get_all_posts"))


@post_bp.route("/delete/<int:post_id>", methods=["POST"])
def delete_one_post(post_id):
    post = fetch_post_by_id(post_id)
    if post is None:
        abort(404)
    delete_post_model(post_id)
    return redirect(url_for("post.get_all_posts"))


@post_bp.route("/delete/<int:post_id>/htmx", methods=["DELETE"])
def delete_one_post_htmx(post_id):
    post = fetch_post_by_id(post_id)
    if post is None:
        abort(404)
    delete_post_model(post_id)
    return ""
