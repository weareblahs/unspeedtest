#!/bin/bash
echo "unspeedtest by Tan (weareblahs)"
echo ''
echo "If you didn't install Speedtest yet (or you installed speedtest-cli instead of"
echo 'the official Ookla one), Please follow the steps on'
echo 'https://www.speedtest.net/apps/cli#Install_Options to install Speedtest, then'
echo 'run for the first time and accept EULA in order to let unspeedtest work'
echo 'properly.'
echo ''
echo 'unspeedtest does not work on 32-bit Raspberry Pi OS / Linux instances.'
echo ''
read -n 1 -s -r -p "Press any key to start installation of unspeedtest."
echo ''
echo "Checking if required software is installed..."
sudo apt install python3 apache2
echo "Installing Python requirements..."
sudo apt install pipx
pipx install cookiecutter
pipx runpip cookiecutter install -r requirements.txt
ln -s $(pwd)/apache /var/www/html/unspeedtest
echo $(pwd) >> dir
chmod +x *.sh
echo "Setting up cronjob..."
crontab cron
./clearresults.sh
echo "unspeedtest is accessible via http://[LOCAL_IP]/unspeedtest."