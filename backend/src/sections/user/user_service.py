from src.database_connector import connectToDb
from pathlib import Path
from src.sections.user.user_model import *
from passlib.context import CryptContext

SQL_DIR = Path(__file__).parent / "sql"

def load_sql(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="utf-8")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str) -> str:
    if len(password.encode("utf-8")) > 72:
        raise ValueError("Passwort darf maximal 72 Bytes lang sein.")
    return pwd_context.hash(password)

def create_user(data: CreateRequest):
    hashed_password = hash_password(data.password)
    sql = load_sql("create_user.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (data.username, data.email, hashed_password, data.role_id))
        created_user = cursor.fetchone()
        conn.commit()
        cursor.close()
        return created_user
    except Exception as e:
        print("Fehler beim Erstellen des Users:", e)
        return False
def delete_user(user_id: int):
    sql = load_sql("delete_user_by_id.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (user_id, user_id, user_id, user_id, user_id, user_id, user_id))
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Fehler beim Löschen des Users:", e)
        return False
def edit_user_by_id(user_id:int, data: EditRequest):
    sql = load_sql("edit_user_by_id.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (data.username,data.email, data.role_id, user_id),)
        user = cursor.fetchone
        conn.commit()
        cursor.close()
        return user
    except Exception as e:
        print("Fehler beim Updaten des Users:", e)
        return False    

def get_all_users():
    sql = load_sql("get_all_users.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql)
        users = cursor.fetchall()
        return users
    except Exception as e:
        print("Fehler beim Laden der User:", e)
        return False
def get_user_by_email(email: str):
    sql = load_sql("get_user_by_email.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (email,))
        user = cursor.fetchone()
        conn.commit()
        cursor.close()
        return user
    except Exception as e:
        print("Fehler beim Laden des Users:", e)
        return False
def get_user_by_id(user_id: int):
    sql = load_sql("get_user_by_id.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (user_id,))
        user = cursor.fetchone()
        conn.commit()
        cursor.close()
        return user
    except Exception as e:
        print("Fehler beim Laden des Users:", e)
        return False


