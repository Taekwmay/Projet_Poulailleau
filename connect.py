import mysql.connector
from mysql.connector import Error

def get_data_from_mysql():
    try:
        conn = mysql.connector.connect(
            host="192.168.94.153",
            user="mariadb",
            password="mariadb",
            database="mariadb"
        )
        if conn.is_connected():
            cursor = conn.cursor()

            # Récupération des données de la table DEMO1
            cursor.execute("SELECT * FROM DEMO1")
            data_demo1 = cursor.fetchall()

            # Récupération des données de la table DEMO2
            cursor.execute("SELECT * FROM DEMO2")
            data_demo2 = cursor.fetchall()

            # Récupération des données de la table DEMO3
            cursor.execute("SELECT * FROM DEMO3")
            data_demo3 = cursor.fetchall()

            cursor.close()
            conn.close()
            
            return data_demo1, data_demo2, data_demo3
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None
