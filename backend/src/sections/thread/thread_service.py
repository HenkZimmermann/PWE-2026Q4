from psycopg2.extras import RealDictCursor
from src.sections.thread.thread_model import *
from src.utils import get_db_connection, load_sql_file

def get_thread_feed(limit, group_id=None):
    sql = load_sql_file("sql/get_thread_feed.sql", __file__)
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(sql, {"limit": limit, "group_id": group_id})
        threads = cursor.fetchall()
        cursor.close()
        return threads
    except Exception as e:
        print("Fehler beim Abrufen des Feeds: ", e)
        return False

def create_thread(request: ThreadModel):
    sql = load_sql_file("sql/create_thread.sql", __file__)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [
            request.message,
            request.user_id,
            request.votes,
            request.group_id,
            request.title
        ])
        created_thread = cursor.fetchone()
        conn.commit()
        cursor.close()
        return created_thread
    except Exception as e:
        print("Fehler beim Erstellen des Threads: ", e)
        return False
    
def delete_thread_by_id(thread_id: int):
    sql = load_sql_file("sql/delete_thread_by_id.sql", __file__)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [thread_id])
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Fehler beim Löschen des Threads: ", e)
        return False
    
def edit_thread_by_id(thread_id: int, request: EditThreadModel, user_id: int, is_admin: bool):
    sql = load_sql_file("sql/edit_thread_by_id.sql", __file__)
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM threads WHERE thread_id = %s FOR UPDATE", [thread_id])
        thread = cursor.fetchone()
        if thread is None:
            return None
        if thread[0] != user_id and not is_admin:
            return False

        cursor.execute(sql, [request.title, request.message, thread_id])
        conn.commit()
        return True
    finally:
        conn.close()
    
def search_threads(term, limit, group_id=None):
    sql = load_sql_file("sql/search_threads.sql", __file__)
    count_sql = load_sql_file("sql/count_search_threads.sql", __file__)

    # SQL Escapen!!!
    term = term.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        params = {
            "pattern": f"%{term}%",
            "limit": limit,
            "group_id": group_id
        }

        # Eigentlich Suche
        cursor.execute(sql, params)
        threads = cursor.fetchall()

        # Anzahl Ergebnisse
        cursor.execute(count_sql, params)
        total_count = cursor.fetchone()["totalCount"]
        
        cursor.close()
        return {"threads": threads, "totalCount": total_count}
    except Exception as e:
        print("Fehler beim Suchen der Threads: ", e)
        return False
    
def get_all_threads_by_user_id(user_id: int):
    sql = load_sql_file("sql/get_all_threads_by_user_id.sql", __file__)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [user_id])
        threads = cursor.fetchall()
        cursor.close()
        return threads
    except Exception as e:
        print("Fehler beim Abrufen der Threads: ", e)
        return False
    
def get_all_threads_order_by_votes():
    sql = load_sql_file("sql/get_all_threads_order_by_votes.sql", __file__)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        threads = cursor.fetchall()
        cursor.close()
        return threads
    except Exception as e:
        print("Fehler beim Abrufen der Threads: ", e)
        return False
    
def get_thread_by_id(thread_id: int):
    sql = load_sql_file("sql/get_thread_by_id.sql", __file__)
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(sql, [thread_id])
        thread =  cursor.fetchone()
        cursor.close()
        return thread
    except Exception as e:
        print("Fehler beim Abrufen des Threads:", e)
        return False
    
def get_threads_of_group_order_by_date(group_id: int):
    sql = load_sql_file("sql/get_threads_of_group_order_by_date.sql", __file__)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [group_id])
        threads = cursor.fetchall()
        cursor.close()
        return threads
    except Exception as e:
        print("Fehler beim Abrufen der Threads: ", e)
        return False
