sudo raspi-config nonint do_ssh 0
sudo apt-get install -y vsftpd
sudo service vsftpd start
sudo apt-get install -y python3-pip 
sudo apt-get install -y libglib2.0-dev
sudo pip3 install flask
sudo pip3 install bluepy
pip install mysql-connector-python
mkdir /tmp/projmet
cd /tmp/projmet
wget https://github.com/Taekwmay/Projet_Poulailleau/archive/refs/heads/main.tar.gz
tar -xzvf main.tar.gz
cd /tmp/projmet/Projet_Poulailleau-main
chmod 766 meteo.py
chmod 766 BDD.sh
sudo ./BDD.sh
sudo python3 meteo.py 2>&1
