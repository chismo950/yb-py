from database import create_connection, course_table_name
import sqlite3

def add_course(name: str, unit: int):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(f"INSERT INTO {course_table_name} (name, unit) VALUES (?, ?)", (name, unit))
        conn.commit()
        print(" Course added successfully.")
    except sqlite3.IntegrityError:
        print(" name must be unique.")
    conn.close()

def view_courses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {course_table_name}")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_course(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {course_table_name} WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_course(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {course_table_name} WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("🗑️ course deleted.")