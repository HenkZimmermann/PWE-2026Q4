from src.utils import get_db_connection, load_sql_file

def _read_thread_vote_summary(cursor, user_id: int, thread_id: int):
    sql = load_sql_file("sql/get_thread_vote_summary.sql", __file__)
    cursor.execute(sql, [user_id, thread_id])
    row = cursor.fetchone()
    return {"score": row[0], "ownVote": row[1]} if row is not None else None

def get_thread_vote_summary(user_id: int, thread_id: int):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        return _read_thread_vote_summary(cursor, user_id, thread_id)
    finally:
        conn.close()

def set_thread_vote(user_id: int, thread_id: int, direction: int):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        if direction == 0:
            sql = load_sql_file("sql/delete_vote.sql", __file__)
            cursor.execute(sql, [user_id, thread_id])
        else:
            sql = load_sql_file("sql/set_thread_vote.sql", __file__)
            cursor.execute(sql, [user_id, direction, thread_id])

        vote = _read_thread_vote_summary(cursor, user_id, thread_id)
        conn.commit()
        return vote
    finally:
        conn.close()

def create_vote(user_id: int, thread_id: int):
    sql = load_sql_file("sql/create_vote.sql", __file__)
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
    sql = load_sql_file("sql/delete_vote.sql", __file__)
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
    sql = load_sql_file("sql/get_thread_votes_by_thread_id.sql", __file__)
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
    sql = load_sql_file("sql/get_votes_from_user_id.sql", __file__)
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
