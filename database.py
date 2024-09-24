import mysql.connector
from config import DB_HOST,DB_NAME,database_name,DB_PASSWORD,DB_USER
import logging

def connect_to_db():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    print("Connected to MySQL database")


def add_user_to_db(user_id: int, username: str, full_name: str) -> bool:
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # Check if user is new
        cursor.execute("SELECT 1 FROM bot_users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()

        if result is None:
            # User is new, add to the database
            cursor.execute(
                "INSERT INTO bot_users (user_id, user_name, username) VALUES (%s, %s, %s)",
                (user_id, full_name, username)
            )
            conn.commit()
            print(f'User {user_id} added successfully.')
            is_new = True
        else:
            print(f'User {user_id} already exists in the database.')
            is_new = False

    except Exception as e:
        logging.error(f'Database error: {e}')
        print(f'Database error: {e}')
        is_new = False

    finally:
        if conn:
            conn.close()

    return is_new

#chang status of recived column to yes in certificates table in mysql

def update_status(user_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "UPDATE certificates SET recieved = 'yes' WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        conn.commit()
        print("Status updated successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if conn:
            conn.close()

def count_bot_users():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # Execute the COUNT(*) query
        cursor.execute(f"SELECT COUNT(*) FROM bot_users")
        row_count = cursor.fetchone()[0]
        cursor.close()
        return(row_count)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if conn:
            conn.close()