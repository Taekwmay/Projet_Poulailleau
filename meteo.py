from bluepy.btle import Scanner
import mysql.connector

# Fonction pour insérer les données dans la base de données
def insert_data(device_addr, temperature, humidity, battery):
    try:
        # Connexion à la base de données
        connection = mysql.connector.connect(
            host="localhost",
            user="mariadb",  # Utilisateur MySQL que vous avez créé
            password="mariadb",  # Mot de passe MySQL que vous avez défini
            database="mariadb"  # Nom de la base de données que vous avez créée
        )

        cursor = connection.cursor()

        # Insérer les données dans la table correspondante au capteur
        if device_addr == "d6:1c:bf:b7:76:62":
            table_name = "DEMO1"
        elif device_addr == "d6:c6:c7:39:a2:e8":
            table_name = "DEMO2"
        elif device_addr == "d7:ef:13:27:15:29":
            table_name = "DEMO3"
        else:
            return  # Si l'adresse n'est pas reconnue, on quitte la fonction

        # Commande SQL pour insérer les données
        sql_insert_query = f"INSERT INTO {table_name} (temperature, humidity, battery) VALUES (%s, %s, %s)"
        insert_tuple = (temperature, humidity, battery)

        # Exécution de la requête SQL
        cursor.execute(sql_insert_query, insert_tuple)
        connection.commit()

        print("Données insérées avec succès dans la table", table_name)

    except mysql.connector.Error as error:
        print("Erreur lors de l'insertion des données:", error)

    finally:
        # Fermeture de la connexion
        if connection.is_connected():
            cursor.close()
            connection.close()

# Scanner BLE
scanner = Scanner()
print("Début de la recherche de périphériques")

while True:
    devices = scanner.scan(timeout=3.0)

    for device in devices:
        if device.addr in ["d6:c6:c7:39:a2:e8", "d6:1c:bf:b7:76:62", "d7:ef:13:27:15:29"]:
            print(
                f"Périphérique trouvé {device.addr} ({device.addrType}), "
                f"RSSI={device.rssi} dB"
            )
            for adtype, description, value in device.getScanData():
                if adtype == 22:
                    temp = int(value[24:28], 16) / 100
                    humidity = int(value[28:32], 16) / 100
                    battery = int(value[20:22], 16)
                    print("Température =", temp, "°C")
                    print("Taux d'humidité =", humidity, "%")
                    print("Batterie =", battery, "%")

                    # Insérer les données dans la base de données
                    insert_data(device.addr, temp, humidity, battery)
