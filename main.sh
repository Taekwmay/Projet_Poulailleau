sudo raspi-config nonint do_ssh 0
sudo apt-get install -y vsftpd
sudo service vsftpd start
sudo apt-get install -y python3-pip 
sudo apt-get install -y libglib2.0-dev
sudo pip3 install bluepy
sudo pip3 install mysql-connector-python
sudo pip3 install requests
chmod 766 meteo.py
chmod 766 BDD.sh
sudo ./BDD.sh
python3 -m venv .venv
. .venv/bin/activate
pip install Flask
pip install mysql-connector-python
flask --app app run --host=0.0.0.0
sudo python3 meteo.py 2>&1

