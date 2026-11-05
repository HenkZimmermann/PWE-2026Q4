from src.sections.thread.thread_model import *
from src.database_connector import connectToDb
from pathlib import Path
SQL_DIR = Path(__file__).parent / "sql"

def load_sql_request(sqlFileName: str) -> str:
    return (SQL_DIR / sqlFileName).read_text(encoding="utf-8")

def create_thread(request: threadCreateModel):
    sql = load_sql_request("create_thread.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (
            request.message,
            request.user_id,
            request.votes,
            request.group_id,
            request.title
        ),)
        created_thread = cursor.fetchone()
        conn.commit()
        cursor.close()
        return created_thread
    except Exception as e:
        print("Fehler beim Erstellen des Threads:", e)
        return False
def delete_thread_by_id(thread_id:int):
    sql = load_sql_request("delete_thread_by_id.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (thread_id,))
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Fehler beim Löschen des Threads:", e)
        return False
def edit_thread_by_id(thread_id:int, request: threadCreateModel):
    sql = load_sql_request("edit_thread_by_id.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (
            request.group_id,
            request.title,
            request.message,
            request.votes,
            request.user_id,
            thread_id
        ),)
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Fehler beim Bearbeiten des Threads:", e)
        return False
def get_all_threads_by_name(name:str):
    sql = load_sql_request("get_all_threads_by_name.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (f"%{name}%",))
        threads = cursor.fetchall()
        cursor.close()
        return threads
    except Exception as e:
        print("Fehler beim Abrufen der Threads:", e)
        return False
def get_all_threads_by_user_id(user_id:int):
    sql = load_sql_request("get_all_threads_by_user_id.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (user_id,))
        threads = cursor.fetchall()
        cursor.close()
        return threads
    except Exception as e:
        print("Fehler beim Abrufen der Threads:", e)
        return False
def get_all_threads_order_by_votes():
    sql = load_sql_request("get_all_threads_order_by_votes.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql,)
        threads = cursor.fetchall()
        cursor.close()
        return threads
    except Exception as e:
        print("Fehler beim Abrufen der Threads:", e)
        return False
def get_thread_by_id(thread_id:int):
    sql = load_sql_request("get_thread_by_id.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (thread_id,))
        thread = cursor.fetchone()
        cursor.close()
        return thread
    except Exception as e:
        print("Fehler beim Abrufen des Threads:", e)
        return False
def get_threads_of_group_order_by_date(group_id:int):
    sql = load_sql_request("get_threads_of_group_order_by_date.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (group_id,))
        threads = cursor.fetchall()
        cursor.close()
        return threads
    except Exception as e:
        print("Fehler beim Abrufen der Threads:", e)
        return False