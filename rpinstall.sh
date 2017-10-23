
#!/bin/bash
echo "+++++++++++++++ install update"
apt-get update

echo "+++++++++++++++ install git"
apt-get install -y git

echo "+++++++++++++++ install python-pip"
apt-get install -y python-pip

echo "+++++++++++++++ install python-pycurl"
apt-get install -y python-pycurl

echo "+++++++++++++++ install python-pyqtgraph"
cd /usr/src/
wget http://www.pyqtgraph.org/downloads/0.10.0/pyqtgraph-0.10.0.tar.gz
tar -xzvf pyqtgraph-0.10.0.tar.gz
cd pyqtgraph-0.10.0
python setup.py install
cd /usr/src/

echo "+++++++++++++++ install python-qt4"
apt-get -y install python-qt4

echo "+++++++++++++++ install websocket-client"
git clone https://github.com/websocket-client/websocket-client.git
cd websocket-client/
python setup.py install
cd /usr/src/

#echo "+++++++++++++++ setup screen for BBB"
#bash /opt/scripts/tools/graphics/ti-tilcdc.sh

echo "+++++++++++++++ install numpy"
apt-get install -y python-numpy

echo "+++++++++++++++ install python-yaml"
apt-get install -y python-yaml

echo "+++++++++++++++ install xinit et unclutter"
apt-get install -y xinit unclutter

echo "+++++++++++++++ auto-launch at boot"
cp /usr/src/AkexUI/akexui.service /lib/systemd/system
cp /usr/src/AkexUI/akexui.timer /lib/systemd/system
systemctl enable akexui.timer
cd /usr/src/
chmod +x akexUI.py
chmod +x StartakexUI

rm -r pyqtgraph*
rm pyqtgraph*
rm -r websocket-client

echo "all is done"
echo "you can reboot"
echo "this UI need Octoprint installed, put your ApiKey and some setup in /usr/src/AkexUI/akexUI.yaml"

exit 0
