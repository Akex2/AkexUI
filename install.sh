#!/bin/bash
sudo su
echo "update"
apt-get update
echo "git"
apt-get install git
echo "python-pip"
apt-get install python-pip
echo "python-pycurl"
apt-get install python-pycurl
echo "python-pyqtgraph"
apt-get install python-pyqtgraph
echo "python-qt4"
apt-get -y install python-qt4
#sudo apt-get install xorg
echo "xinit et unclutter"
apt-get install xinit unclutter
echo "cd root"
cd /root/
echo "clone"
git clone https://github.com/Akex2/AkexUI.git
cd AkexUI/
exit 0
