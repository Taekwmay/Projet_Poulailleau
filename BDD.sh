if ! dpkg -l | grep -q debconf-utils; then
    sudo apt-get update
    sudo apt-get install -y debconf-utils
fi
MYSQL_ROOT_PASSWORD="mariadb"

echo "mysql-server mysql-server/root_password password $MYSQL_ROOT_PASSWORD" > mysql-config.cfg
echo "mysql-server mysql-server/root_password_again password $MYSQL_ROOT_PASSWORD" >> mysql-config.cfg

sudo debconf-set-selections < mysql-config.cfg

sudo apt-get update
sudo apt-get install -y default-mysql-server

rm mysql-config.cfg

echo "MySQL a été installé avec le mot de passe root : $MYSQL_ROOT_PASSWORD"

