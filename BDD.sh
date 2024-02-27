#!/bin/bash

# Vérification et installation de debconf-utils si nécessaire
if ! dpkg -l | grep -q debconf-utils; then
    sudo apt-get update
    sudo apt-get install -y debconf-utils
fi

# Définition des mots de passe et du nom de la base de données
MYSQL_ROOT_PASSWORD="mariadb"
MYSQL_USER="mariadb"
MYSQL_USER_PASSWORD="mariadb"
DATABASE_NAME="mariadb"

# Configuration des mots de passe pour l'installation MySQL
echo "mysql-server mysql-server/root_password password $MYSQL_ROOT_PASSWORD" > mysql-config.cfg
echo "mysql-server mysql-server/root_password_again password $MYSQL_ROOT_PASSWORD" >> mysql-config.cfg

# Application des configurations
sudo debconf-set-selections < mysql-config.cfg

# Mise à jour et installation de MySQL
sudo apt-get update
sudo apt-get install -y default-mysql-server

# Création de la base de données
echo "CREATE DATABASE IF NOT EXISTS $DATABASE_NAME;" | sudo mysql -u root -p"$MYSQL_ROOT_PASSWORD"

# Création d'un utilisateur MySQL avec les droits appropriés
echo "CREATE USER '$MYSQL_USER'@'localhost' IDENTIFIED BY '$MYSQL_USER_PASSWORD';" | sudo mysql -u root -p"$MYSQL_ROOT_PASSWORD"
echo "GRANT ALL PRIVILEGES ON $DATABASE_NAME.* TO '$MYSQL_USER'@'localhost';" | sudo mysql -u root -p"$MYSQL_ROOT_PASSWORD"
echo "FLUSH PRIVILEGES;" | sudo mysql -u root -p"$MYSQL_ROOT_PASSWORD"

# Création des tables pour les capteurs DEMO 1, DEMO 2 et DEMO 3
echo "USE $DATABASE_NAME;
CREATE TABLE IF NOT EXISTS DEMO1 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperature FLOAT,
    humidity FLOAT,
    battery FLOAT
);
CREATE TABLE IF NOT EXISTS DEMO2 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperature FLOAT,
    humidity FLOAT,
    battery FLOAT
);
CREATE TABLE IF NOT EXISTS DEMO3 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperature FLOAT,
    humidity FLOAT,
    battery FLOAT
);
CREATE TABLE IF NOT EXISTS Sensors (
    device_addr VARCHAR(17) PRIMARY KEY,
    sensor_name VARCHAR(255) NOT NULL
);"| sudo mysql -u root -p"$MYSQL_ROOT_PASSWORD"

# Suppression du fichier de configuration temporaire
rm mysql-config.cfg

# Affichage des informations de configuration
echo "MySQL a été installé avec le mot de passe root : $MYSQL_ROOT_PASSWORD"
echo "La base de données $DATABASE_NAME a été créée."
echo "Un utilisateur MySQL '$MYSQL_USER' a été créé avec le mot de passe '$MYSQL_USER_PASSWORD' et les droits appropriés."
echo "Les tables pour les capteurs DEMO1, DEMO2 et DEMO3 ont été créées."
