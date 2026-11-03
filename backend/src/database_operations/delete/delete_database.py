from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from database_connector import connectToDb

def reset_database():
    with connectToDb() as conn:
        with conn.cursor() as cur:
            cur.execute("DROP SCHEMA public CASCADE;")
            cur.execute("CREATE SCHEMA public;")

if __name__ == "__main__":
    reset_database()
    print("Datenbank wurde gelöscht.")