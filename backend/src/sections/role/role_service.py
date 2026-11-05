from src.sections.role.role_model import *
from src.database_connector import connectToDb
from pathlib import Path
SQL_DIR = Path(__file__).parent / "sql"

def load_sql_request(sqlFileName: str) -> str:
    return (SQL_DIR / sqlFileName).read_text(encoding="utf-8")

def create_role(request: roleCreateModel):
    sql = load_sql_request("create_role.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (
            request.name, 
            request.permissions, 
        ),)
        created_role = cursor.fetchone()
        conn.commit()
        cursor.close()
        return created_role
    except Exception as e:
        print("Fehler beim Erstellen der Rolle:", e)
        return False
def edit_role_by_id(role_id:int, request: roleCreateModel):
    sql = load_sql_request("edit_role_by_id.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (
            request.name, 
            request.permissions, 
            role_id
        ),)
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Fehler beim Bearbeiten der Rolle:", e)
        return False
def get_all_roles():
    sql = load_sql_request("get_all_roles.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql)
        roles = cursor.fetchall()
        cursor.close()
        return roles
    except Exception as e:
        print("Fehler beim Abrufen der Rollen:", e)
        return False
def get_role_by_id(role_id:int):
    sql = load_sql_request("get_role_by_id.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (role_id,))
        role = cursor.fetchone()
        cursor.close()
        return role
    except Exception as e:
        print("Fehler beim Abrufen der Rolle:", e)
        return False
