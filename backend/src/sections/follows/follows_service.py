from src.database_connector import connectToDb
from pathlib import Path
SQL_DIR = Path(__file__).parent / "sql"

def load_sql_request(sqlFileName: str) -> str:
    return (SQL_DIR / sqlFileName).read_text(encoding="utf-8")

def create_follower(user_id:int, followed_user_id:int):
    sql = load_sql_request("create_follower.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (user_id, followed_user_id))
        created_follower = cursor.fetchone()
        conn.commit()
        cursor.close()
        return created_follower
    except Exception as e:
        print("Fehler beim Erstellen des Followers:", e)
        return False
def delete_follower(user_id:int, followed_user_id:int):
    sql = load_sql_request("delete_follower.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (user_id, followed_user_id))
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Fehler beim Löschen des Followers:", e)
        return False
def get_all_followers_of_user_id(user_id:int):
    sql = load_sql_request("get_all_followers_of_user_id.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (user_id,))
        followers = cursor.fetchall()
        cursor.close()
        return followers
    except Exception as e:
        print("Fehler beim Abrufen der Follower:", e)
        return False
def get_all_users_user_id_follows(user_id:int):
    sql = load_sql_request("get_users_user_id_follows.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (user_id,))
        follows = cursor.fetchall()
        cursor.close()
        return follows
    except Exception as e:
        print("Fehler beim Abrufen der Follows:", e)
        return False