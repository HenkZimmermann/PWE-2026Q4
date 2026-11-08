from src.sections.role.role_model import *
from src.utils import get_db_connection, load_sql_file

def create_role(request: RoleModel):
    sql = load_sql_file("create_role.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [
            request.name, 
            request.permissions, 
        ])
        created_role = cursor.fetchone()
        conn.commit()
        cursor.close()
        return created_role
    except Exception as e:
        print("Fehler beim Erstellen der Rolle: ", e)
        return False
    
def edit_role_by_id(role_id: int, request: RoleModel):
    sql = load_sql_file("edit_role_by_id.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [
            request.name, 
            request.permissions, 
            role_id
        ])
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Fehler beim Bearbeiten der Rolle: ", e)
        return False
    
def get_all_roles():
    sql = load_sql_file("get_all_roles.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        roles = cursor.fetchall()
        cursor.close()
        return roles
    except Exception as e:
        print("Fehler beim Abrufen der Rollen: ", e)
        return False
    
def get_role_by_id(role_id: int):
    sql = load_sql_file("get_role_by_id.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [role_id])
        role = cursor.fetchone()
        cursor.close()
        return role
    except Exception as e:
        print("Fehler beim Abrufen der Rolle: ", e)
        return False
