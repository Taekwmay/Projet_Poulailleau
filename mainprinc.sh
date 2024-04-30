mkdir /tmp/projmet
cd /tmp/projmet
sudo rm -f main.tar.gz
wget https://github.com/Taekwmay/Projet_Poulailleau/archive/refs/heads/main.tar.gz
tar -xzvf main.tar.gz
cd /tmp/projmet/Projet_Poulailleau-main
sudo chmod 766 main.sh
sudo ./main.sh