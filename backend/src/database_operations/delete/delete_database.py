from src.utils import get_db_connection

def reset_database():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DROP SCHEMA public CASCADE;")
            cur.execute("CREATE SCHEMA public;")

if __name__ == "__main__":
    reset_database()
    print("Datenbank wurde gelöscht")