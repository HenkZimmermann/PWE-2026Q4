from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from database_connector import connectToDb
APP_DIR = Path(__file__).resolve().parent 
def load_sql(filename: str) -> str:
    return (APP_DIR / filename).read_text(encoding="utf-8")

def init_db():
    with connectToDb() as conn:
        with conn.cursor() as cur:
            cur.execute(load_sql("seed.sql"))
if __name__ == "__main__":
    init_db()
    print("Datenbank wurde mit Seed-Daten initialisiert.")