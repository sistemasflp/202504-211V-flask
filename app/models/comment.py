from app.utils.db import get_db_connection


def fetch_all_comments():
    db = get_db_connection()
    return db.execute("SELECT * FROM comments;")
