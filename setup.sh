#!/bin/bash
echo "unspeedtest by Tan (weareblahs)"
echo ''
echo "If you didn't install Speedtest yet (or you installed speedtest-cli instead of"
echo 'the official Ookla one), Please follow the steps on'
echo 'https://www.speedtest.net/apps/cli#Install_Options to install Speedtest, then'
echo 'run for the first time and accept EULA in order to let unspeedtest work'
echo 'properly.'
echo ''
read -n 1 -s -r -p "Press any key to start installation of unspeedtest."
echo "Checking if required software is installed..."
sudo apt install python3 apache2 python3-pip
echo "Installing Python requirements..."
pip install -r requirements.txt --break-system-packages
ln -s $(pwd)/apache /var/www/html/unspeedtest
echo $(pwd) >> dir
chmod +x *.sh
echo "Setting up cronjob..."
crontab cron
./clearresults.sh
echo "unspeedtest is accessible via http://$(hostname).local/unspeedtest."
echo "If you can't access it, try replacing $(hostname).local to $(hostname -I)and try again."