from src.utils import get_db_connection, load_sql_file

def create_db():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(load_sql_file("schema.sql", __file__))

if __name__ == "__main__":
    create_db()
    print("Datenbank wurde erstellt")