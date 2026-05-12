from flask import Blueprint, render_template
from app.models.comment import fetch_all_comments

comments_bp = Blueprint('comments', __name__, url_prefix='/comments')


@comments_bp.route("/list")
def get_all_comments():
    comments = fetch_all_comments()
    return render_template("comment/list.html", comments=comments)

