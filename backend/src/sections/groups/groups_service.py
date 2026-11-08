from src.sections.groups.groups_model import *
from src.utils import get_db_connection, load_sql_file

def create_group(request: GroupModel):
    sql = load_sql_file("create_group.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [
            request.group_name, 
            request.category, 
            request.members, 
            request.system_created,
            request.description,
        ])
        created_group = cursor.fetchone()
        conn.commit()
        cursor.close()
        return created_group
    except Exception as e:
        print("Fehler beim Erstellen der Gruppe: ", e)
        return False
    
def delete_group_by_id(group_id: int):
    sql = load_sql_file("delete_group_by_id.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [group_id])
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Fehler beim Löschen der Gruppe: ", e)
        return False
    
def edit_group_by_id(group_id: int, request: GroupModel):
    sql = load_sql_file("edit_group_by_id.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [
            request.group_name, 
            request.category, 
            request.members, 
            request.system_created,
            request.description,
            group_id
        ])
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Fehler beim Bearbeiten der Gruppe: ", e)
        return False
    
def get_all_groups_by_Category(category: str):
    sql = load_sql_file("get_all_groups_by_category.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [category])
        groups = cursor.fetchall()
        cursor.close()
        return groups
    except Exception as e:
        print("Fehler beim Abrufen der Gruppen nach Kategorie: ", e)
        return False
    
def get_all_groups_order_by_members():
    sql = load_sql_file("get_all_groups_order_by_members.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        groups = cursor.fetchall()
        cursor.close()
        return groups
    except Exception as e:
        print("Fehler beim Abrufen der Gruppen: ", e)
        return False
    
def get_all_groups():
    sql = load_sql_file("get_all_groups.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        groups = cursor.fetchall()
        cursor.close()
        return groups
    except Exception as e:
        print("Fehler beim Abrufen der Gruppen: ", e)
        return False
    
def get_group_by_id(group_id: int):
    sql = load_sql_file("get_group_by_id.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [group_id])
        group = cursor.fetchone()
        cursor.close()
        return group
    except Exception as e:
        print("Fehler beim Abrufen der Gruppe nach ID: ", e)
        return False
    
def get_group_by_name(group_name: str):
    sql = load_sql_file("get_group_by_name.sql")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [group_name])
        group = cursor.fetchone()
        cursor.close()
        return group
    except Exception as e:
        print("Fehler beim Abrufen der Gruppe nach Name: ", e)
        return False