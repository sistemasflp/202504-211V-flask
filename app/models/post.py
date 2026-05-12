from app.utils.db import get_db_connection


def fetch_all_posts():
    db = get_db_connection()
    return db.execute("SELECT * FROM posts;")


def fetch_post_by_id(post_id):
    db = get_db_connection()
    return db.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()


def create_post(title, content):
    db = get_db_connection()
    db.execute(
        "INSERT INTO posts (title, content) VALUES (?, ?)",
        (title, content),
    )
    db.commit()


def update_post(post_id, title, content):
    db = get_db_connection()
    db.execute(
        "UPDATE posts SET title = ?, content = ? WHERE id = ?",
        (title, content, post_id),
    )
    db.commit()


def delete_post(post_id):
    db = get_db_connection()
    db.execute("DELETE FROM posts WHERE id = ?", (post_id,))
    db.commit()
