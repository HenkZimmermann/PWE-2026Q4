from contextlib import closing
from psycopg2.extras import RealDictCursor
from src.sections.comment.comment_model import *
from src.utils import get_db_connection, load_sql_file

def create_comment(request: CommentModel):
    sql = load_sql_file("sql/create_comment.sql", __file__)
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
    
def delete_comment_by_id(comment_id: int, user_id: int, is_admin: bool):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM comments WHERE comment_id = %s AND deleted_at IS NULL FOR UPDATE", [comment_id])
        comment = cursor.fetchone()
        if comment is None:
            return None
        if comment[0] != user_id and not is_admin:
            return False

        cursor.execute("SELECT 1 FROM comments WHERE parent_comment_id = %s LIMIT 1", [comment_id])
        has_replies = cursor.fetchone() is not None
        filename = "mark_comment_deleted.sql" if has_replies else "delete_comment_by_id.sql"
        sql = load_sql_file(f"sql/{filename}", __file__)
        cursor.execute(sql, [comment_id])
        conn.commit()
        return {"removed": not has_replies}
    finally:
        conn.close()
    
def edit_comment_by_id(comment_id: int, request: EditCommentModel, user_id: int, is_admin: bool):
    sql = load_sql_file("sql/edit_comment_by_id.sql", __file__)
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM comments WHERE comment_id = %s AND deleted_at IS NULL FOR UPDATE", [comment_id])
        comment = cursor.fetchone()
        if comment is None:
            return None
        if comment[0] != user_id and not is_admin:
            return False

        cursor.execute(sql, [request.message, comment_id])
        conn.commit()
        return True
    finally:
        conn.close()
    
def get_all_comments_by_thread_id(thread_id: int):
    sql = load_sql_file("sql/get_all_comments_by_thread_id.sql", __file__)
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(sql, [thread_id])
            return cursor.fetchall()
    except Exception as e:
        print("Fehler beim Abrufen der Thread Kommentare: ", e)
        return False
    
def get_all_comments_by_parent_comment_id(parent_comment_id: int):
    sql = load_sql_file("sql/get_all_child_comments_by_parent_id.sql", __file__)
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
    sql = load_sql_file("sql/get_comment_by_id.sql", __file__)
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
