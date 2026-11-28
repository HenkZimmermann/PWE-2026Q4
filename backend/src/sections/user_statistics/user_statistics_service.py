from src.utils import get_db_connection, load_sql_file
def get_user_stats(user_id):
    sql = load_sql_file("sql/get_user_stats_by_id.sql", __file__)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [user_id])
        stats = cursor.fetchone()
        if stats is None:
            return None
        #notwendig um auf die einzelnen Elemente zugreifen zu können, siehe User
        column_names = [column[0] for column in cursor.description]
        stats = dict(zip(column_names, stats)) if stats is not None else None    
        conn.commit()
        cursor.close()
        return stats
    except Exception as e:
        print("Fehler beim Laden der User Statistiken: ", e)
        return False
    

