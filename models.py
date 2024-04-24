#import mysql.connector

#def get_db_connection():
#    connection = mysql.connector.connect(
#        host="192.168.233.153",
#        user="mariadb",
#        password="mariadb",
#        database="mariadb"
#    )
#    return connection

#def get_data_from_mysql(table_name):
#    conn = get_db_connection()
#    cursor = conn.cursor(dictionary=True)
#    cursor.execute(f"SELECT * FROM {table_name}")
#    data = cursor.fetchall()
#    cursor.close()
#    conn.close()
#    return data

#def SensorInit(device_addr,sensor_name) :
#    with get_db_connection().cursor() as cursor:
#        cursor.execute("SELECT * FROM Sensors WHERE device_addr= %s",(device_addr,))
#        row=cursor.fetchone()
#        print("recuperation valeurs")

#        if not row :
#            sql_insert_query = f"INSERT INTO Sensors (device_addr, sensor_name) VALUES (%s, %s)"
#            cursor.execute(sql_insert_query,(device_addr,sensor_name))

#SensorInit("d6:1c:bf:b7:76:62","DEMO1")
#SensorInit("d6:1c:bf:b7:76:62","DEMO1")
#SensorInit("d6:1c:bf:b7:76:62","DEMO1")

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

def SensorInit(device_addr, sensor_name):
    conn = get_db_connection()
    with conn.cursor(buffered=True) as cursor:
        cursor.execute("SELECT * FROM Sensors WHERE device_addr=%s", (device_addr,))
        row = cursor.fetchone()
        print("recuperation valeurs",row)

        if not row:
            sql_insert_query = "INSERT INTO Sensors (device_addr, sensor_name) VALUES (%s, %s)"
            cursor.execute(sql_insert_query, (device_addr, sensor_name))
            print("valeur implantees")
            conn.commit()
    conn.close()

SensorInit("d6:1c:bf:b7:76:62","DEMO1")
print("1")
SensorInit("d6:c6:c7:39:a2:e8","DEMO2")
print("2")
SensorInit("d7:ef:13:27:15:29","DEMO3")
print("3")     
