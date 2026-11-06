from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from database_connector import connectToDb

def get_app_dir():
    return Path(__file__).resolve().parent

def load_sql_file(filename: str) -> str:
    return (get_app_dir() / filename).read_text(encoding="utf-8")

def get_db_connection():
    return connectToDb()