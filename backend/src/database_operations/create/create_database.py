from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from database_connector import connectToDb
APP_DIR = Path(__file__).resolve().parent 

def load_sql(filename: str) -> str:
    return (APP_DIR / filename).read_text(encoding="utf-8")

def create_db():
    with connectToDb() as conn:
        with conn.cursor() as cur:
            cur.execute(load_sql("schema.sql"))
if __name__ == "__main__":
    create_db()
    print("Datenbank wurde gemäß dem Schema erstellt.")