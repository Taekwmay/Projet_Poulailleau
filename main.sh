sudo raspi-config nonint do_ssh 0
sudo apt-get install -y vsftpd python3-pip libglib2.0-dev
sudo service vsftpd start
sudo pip3 install bluepy  mysql-connector-python requests
chmod 766 meteo.py
chmod 766 BDD.sh
sudo ./BDD.sh
password="mariadb"
mysql -u root -p$password <<EOF
GRANT ALL ON mariadb.* TO 'mariadb'@'192.168.233.41' IDENTIFIED BY 'mariadb';
FLUSH PRIVILEGES;
GRANT ALL ON mariadb.* TO 'mariadb'@'192.168.233.153' IDENTIFIED BY 'mariadb';
FLUSH PRIVILEGES;
EOF
sudo mv /tmp/projmet/Projet_Poulailleau-main/50-server.cnf /etc/mysql/mariadb.conf.d/50-server.cnf
sudo service mysql restart
python3 -m venv .venv
. .venv/bin/activate
pip install Flask mysql-connector-python
flask --app app run --host=0.0.0.0 &
sudo python3 meteo.py 2>&1

