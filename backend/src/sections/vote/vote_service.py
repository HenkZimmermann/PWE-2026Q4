from src.utils import get_db_connection, load_sql_file

def create_vote(user_id: int, thread_id: int):
    sql = load_sql_file("create_vote.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [user_id, thread_id])
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Fehler beim Erstellen des Votes: ", e)
        return False
    
def delete_vote(user_id: int, thread_id: int):
    sql = load_sql_file("delete_vote.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [user_id, thread_id])
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Fehler beim Löschen des Votes: ", e)
        return False
    
def get_thread_votes(thread_id: int):
    sql = load_sql_file("get_thread_votes_by_thread_id.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [thread_id])
        votes = cursor.fetchall()
        cursor.close()
        return votes
    except Exception as e:
        print("Fehler beim Abrufen der Votes: ", e)
        return False
    
def get_votes_by_user_id(user_id: int):
    sql = load_sql_file("get_votes_from_user_id.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [user_id])
        votes = cursor.fetchall()
        cursor.close()
        return votes
    except Exception as e:
        print("Fehler beim Abrufen der Votes des Users: ", e)
        return False