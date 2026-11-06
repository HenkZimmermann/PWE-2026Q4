from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from src.database_connector import connectToDb

def get_app_dir():
    return Path(__file__).resolve().parent

def load_sql_file(filename: str, caller_file: str = None) -> str:
    if caller_file is None: # Fallback aktuelles Arbeitsverzeichnis
        base = Path.cwd()
    else:
        base = Path(caller_file).parent
    return (base / filename).read_text(encoding="utf-8")

def get_db_connection():
    return connectToDb()