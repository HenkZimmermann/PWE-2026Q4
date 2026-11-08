from src.sections.comment.comment_model import *
from src.utils import get_db_connection, load_sql_file

def create_comment(request: CommentModel):
    sql = load_sql_file("create_comment.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [
            request.thread_id, 
            request.parent_comment_id, 
            request.message, 
            request.votes,
            request.user_id
        ])
        created_comment = cursor.fetchone()
        conn.commit()
        cursor.close()
        return created_comment
    except Exception as e:
        print("Fehler beim Erstellen des Kommentars: ", e)
        return False
    
def delete_comment_by_id(comment_id: int):
    sql = load_sql_file("delete_comment_by_id.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [comment_id])
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Fehler beim Löschen des Kommentars: ", e)
        return False
    
def edit_comment_by_id(comment_id: int, request: CommentModel):
    sql = load_sql_file("edit_comment_by_id.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [
            request.thread_id, 
            request.parent_comment_id, 
            request.message, 
            request.votes,
            request.user_id,
            comment_id
        ])
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Fehler beim Bearbeiten des Kommentars: ", e)
        return False
    
def get_all_comments_by_thread_id(thread_id: int):
    sql = load_sql_file("get_all_comments_by_thread_id.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [thread_id])
        comments = cursor.fetchall()
        cursor.close()
        return comments
    except Exception as e:
        print("Fehler beim Abrufen der Thread Kommentare: ", e)
        return False
    
def get_all_comments_by_parent_comment_id(parent_comment_id: int):
    sql = load_sql_file("get_all_child_comments_by_parent_id.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [parent_comment_id])
        comments = cursor.fetchall()
        cursor.close()
        return comments
    except Exception as e:
        print("Fehler beim Abrufen der Sub Kommentare: ", e)
        return False
    
def get_comment_by_id(comment_id: int):
    sql = load_sql_file("get_comment_by_id.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [comment_id])
        comment = cursor.fetchone()
        cursor.close()
        return comment
    except Exception as e:
        print("Fehler beim Abrufen des Kommentars: ", e)
        return False