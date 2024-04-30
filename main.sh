sudo raspi-config nonint do_ssh 0
sudo apt-get install -y vsftpd python3-pip libglib2.0-dev
sudo service vsftpd start
sudo pip3 install bluepy  mysql-connector-python
chmod 766 meteo.py
chmod 766 BDD.sh
sudo ./BDD.sh
sudo mv /tmp/projmet/Projet_Poulailleau-main/50-server.cnf /etc/mysql/mariadb.conf.d/50-server.cnf
sudo service mysql restart
python3 -m venv .venv
. .venv/bin/activate
pip install Flask mysql-connector-python requests
flask --app app run --host=0.0.0.0 &
pip install Flask-Mail
python3 meteo.py 2>&1 &
python3 alert_mail.py &
python3 webbrowser.py