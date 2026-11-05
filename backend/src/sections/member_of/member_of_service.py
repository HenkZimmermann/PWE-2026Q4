from src.database_connector import connectToDb
from pathlib import Path
SQL_DIR = Path(__file__).parent / "sql"

def load_sql_request(sqlFileName: str) -> str:
    return (SQL_DIR / sqlFileName).read_text(encoding="utf-8")

def create_group_membership(user_id:int, group_id:int):
    sql = load_sql_request("create_group_membership.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (user_id, group_id))
        created_member = cursor.fetchone()
        conn.commit()
        cursor.close()
        return created_member
    except Exception as e:
        print("Fehler beim Erstellen des Gruppenmitglieds:", e)
        return False
def delete_group_membership(user_id:int, group_id:int):
    sql = load_sql_request("delete_group_membership.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (user_id, group_id))
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Fehler beim Löschen des Gruppenmitglieds:", e)
        return False
def get_all_members_of_group_id(group_id:int):
    sql = load_sql_request("get_all_members_of_group_id.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (group_id,))
        members = cursor.fetchall()
        cursor.close()
        return members
    except Exception as e:
        print("Fehler beim Abrufen der Gruppenmitglieder:", e)
        return False
def get_memberships_from_user_id(user_id:int):
    sql = load_sql_request("get_memberships_from_user_id.sql")
    try:
        conn = connectToDb()
        cursor = conn.cursor()
        cursor.execute(sql, (user_id,))
        memberships = cursor.fetchall()
        cursor.close()
        return memberships
    except Exception as e:
        print("Fehler beim Abrufen der Gruppenmitgliedschaften:", e)
        return False