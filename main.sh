sudo raspi-config nonint do_ssh 0
sudo apt-get install vsftpd
sudo service vsftpd start
sudo apt-get install python3-pip
sudo apt-get install libglib2.0-dev
sudo pip3 install bluepy
mkdir ~/projmet
cd ~/projmet
wget https://github.com/Taekwmay/Projet_Poulailleau/archive/refs/heads/main.tar.gz
tar -xzvf main.tar.gz
sudo ./meteo.py 1>data.log 2>error.log
