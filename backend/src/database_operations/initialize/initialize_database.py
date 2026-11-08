from src.utils import get_db_connection, load_sql_file

def init_db():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(load_sql_file("seed.sql", __file__))

if __name__ == "__main__":
    init_db()
    print("Datenbank wurde befüllt")