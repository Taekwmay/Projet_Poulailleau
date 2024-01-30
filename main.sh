sudo raspi-config nonint do_ssh 0
sudo apt-get install -y vsftpd
sudo service vsftpd start
sudo apt-get install -y python3-pip 
sudo apt-get install -y libglib2.0-dev
sudo pip3 install flask
sudo pip3 install bluepy
mkdir /home/projmet
cd /home/projmet
wget https://github.com/Taekwmay/Projet_Poulailleau/archive/refs/heads/main.tar.gz
tar -xzvf main.tar.gz
cd /home/projmet/Projet_Poulailleau-main
chmod 766 meteo.py
sudo python3 meteo.py 2>&1 | tee -a data.log