import psycopg2
import os
from pathlib import Path
from dotenv import load_dotenv


ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT_DIR / ".env")


config_path = Path(__file__).resolve().parent / "postgresConfig.json"
def connectToDb():   
    return psycopg2.connect(database = os.getenv("POSTGRES_DB"),
        user = os.getenv("POSTGRES_USER"),
        host= os.getenv("POSTGRES_HOST"),
        password = os.getenv("POSTGRES_PASSWORD"),
        port = os.getenv("POSTGRES_PORT"))
