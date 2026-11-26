from src.sections.user.user_model import *
from src.utils import get_db_connection, load_sql_file
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, password_hash: str) -> bool:
    return pwd_context.verify(plain_password, password_hash)

def hash_password(password: str) -> str:
    if len(password.encode("utf-8")) > 72:
        raise ValueError("Passwort darf maximal 72 Bytes lang sein.")
    return pwd_context.hash(password)

def check_login_request(data: LoginRequest):
    user = get_user_by_email(data.email)
    if not user:
        print("User nicht gefunden")
        return False
    if not verify_password(data.password, user["password_hash"]):
        return False
    return {
        "user_id": user["user_id"],
        "email": user["email"],
        "role": user["role_id"],
    }

def create_user(data: CreateRequest):
    hashed_password = hash_password(data.password)
    sql = load_sql_file("sql/create_user.sql", __file__)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [data.username, data.email, hashed_password])
        created_user = cursor.fetchone()
        conn.commit()
        cursor.close()
        return created_user
    except Exception as e:
        print("Fehler beim Erstellen des Users:", e)
        return False
    
def delete_user(user_id: int):
    sql = load_sql_file("sql/delete_user_by_id.sql", __file__)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [user_id, user_id, user_id, user_id, user_id, user_id, user_id])
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Fehler beim Löschen des Users: ", e)
        return False
    
def edit_user_by_id(user_id: int, data: EditRequest):
    sql = load_sql_file("sql/edit_user_by_id.sql", __file__)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [data.username,data.email, data.role_id, user_id])
        user = cursor.fetchone
        conn.commit()
        cursor.close()
        return user
    except Exception as e:
        print("Fehler beim Updaten des Users: ", e)
        return False    

def get_all_users():
    sql = load_sql_file("sql/get_all_users.sql", __file__)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        users = cursor.fetchall()
        return users
    except Exception as e:
        print("Fehler beim Laden der User: ", e)
        return False
    
def get_user_by_email(email: str):
    sql = load_sql_file("sql/get_user_by_email.sql", __file__)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [email])
        user = cursor.fetchone()
        #notwendig um auf die einzelnen Elemente, bpw. email zugreifen zu können
        column_names = [column[0] for column in cursor.description]
        user = dict(zip(column_names, user)) if user is not None else None    
        conn.commit()
        cursor.close()
        return user
    except Exception as e:
        print("Fehler beim Laden des Users: ", e)
        return False
    
def get_user_by_id(user_id: int):
    sql = load_sql_file("sql/get_user_by_id.sql", __file__)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [user_id])
        user = cursor.fetchone()
        conn.commit()
        cursor.close()
        return user
    except Exception as e:
        print("Fehler beim Laden des Users: ", e)
        return False