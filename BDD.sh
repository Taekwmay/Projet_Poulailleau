if ! dpkg -l | grep -q debconf-utils; then
    sudo apt-get update
    sudo apt-get install -y debconf-utils
fi

MYSQL_ROOT_PASSWORD="mariadb"
DATABASE_NAME="nom_de_votre_base_de_donnees"

echo "mysql-server mysql-server/root_password password $MYSQL_ROOT_PASSWORD" > mysql-config.cfg
echo "mysql-server mysql-server/root_password_again password $MYSQL_ROOT_PASSWORD" >> mysql-config.cfg

sudo debconf-set-selections < mysql-config.cfg

sudo apt-get update
sudo apt-get install -y default-mysql-server

# Création de la base de données
echo "CREATE DATABASE IF NOT EXISTS $DATABASE_NAME;" | sudo mysql -u root -p"$MYSQL_ROOT_PASSWORD"

rm mysql-config.cfg

echo "MySQL a été installé avec le mot de passe root : $MYSQL_ROOT_PASSWORD"
echo "La base de données $DATABASE_NAME a été créée."
