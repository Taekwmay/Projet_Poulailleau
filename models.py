import mysql.connector


def get_db_connection():
    connection = mysql.connector.connect(
        host="192.168.233.153",
        user="mariadb",
        password="mariadb",
        database="mariadb"
    )
    return connection

def get_data_from_mysql(table_name):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data
