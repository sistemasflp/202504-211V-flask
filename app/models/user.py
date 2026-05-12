from app.utils.db import get_db_connection


def ensure_user_table():
    db = get_db_connection()
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        );
        """
    )
    db.commit()


def fetch_all_users():
    db = get_db_connection()
    return db.execute("SELECT * FROM User;").fetchall()


def fetch_user_by_id(user_id):
    db = get_db_connection()
    return db.execute("SELECT * FROM User WHERE id = ?", (user_id,)).fetchone()


def create_user(username, email, password):
    db = get_db_connection()
    cursor = db.execute(
        "INSERT INTO User (username, email, password) VALUES (?, ?, ?)",
        (username, email, password),
    )
    db.commit()
    return cursor.lastrowid


def update_user(user_id, username, email, password):
    db = get_db_connection()
    db.execute(
        "UPDATE User SET username = ?, email = ?, password = ? WHERE id = ?",
        (username, email, password, user_id),
    )
    db.commit()


def delete_user(user_id):
    db = get_db_connection()
    db.execute("DELETE FROM User WHERE id = ?", (user_id,))
    db.commit()
