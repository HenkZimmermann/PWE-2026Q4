from src.sections.comment.comment_model import *
from src.database_connector import connectToDb
from pathlib import Path
SQL_DIR = Path(__file__).parent / "sql"

def load_sql_request(sqlFileName: str) -> str:
    return (SQL_DIR / sqlFileName).read_text(encoding="utf-8")

def create_comment(request: commentCreateModel):
    sql = load_sql_request("create_comment.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (
            request.thread_id, 
            request.parent_comment_id, 
            request.message, 
            request.votes,
            request.user_id
        ),)
        created_comment = cursor.fetchone()
        conn.commit()
        cursor.close()
        return created_comment
    except Exception as e:
        print("Fehler beim Erstellen des Kommentars:", e)
        return False
def delete_comment_by_id(comment_id:int):
    sql = load_sql_request("delete_comment_by_id.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (comment_id,))
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Fehler beim Löschen des Kommentars:", e)
        return False
def edit_comment_by_id(comment_id:int, request: commentCreateModel):
    sql = load_sql_request("edit_comment_by_id.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (
            request.thread_id, 
            request.parent_comment_id, 
            request.message, 
            request.votes,
            request.user_id,
            comment_id
        ),)
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Fehler beim Bearbeiten des Kommentars:", e)
        return False
def get_all_comments_by_thread_id(thread_id: int):
    sql = load_sql_request("get_all_comments_by_thread_id.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (thread_id,))
        comments = cursor.fetchall()
        cursor.close()
        return comments
    except Exception as e:
        print("Fehler beim Abrufen der Thread Kommentare:", e)
        return False
def get_all_comments_by_parent_comment_id(parent_comment_id: int):
    sql = load_sql_request("get_all_child_comments_by_parent_id.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (parent_comment_id,))
        comments = cursor.fetchall()
        cursor.close()
        return comments
    except Exception as e:
        print("Fehler beim Abrufen der Sub Kommentare:", e)
        return False
def get_comment_by_id(comment_id: int):
    sql = load_sql_request("get_comment_by_id.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (comment_id,))
        comment = cursor.fetchone()
        cursor.close()
        return comment
    except Exception as e:
        print("Fehler beim Abrufen des Kommentars:", e)
        return False