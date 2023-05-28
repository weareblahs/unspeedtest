echo "unspeedtest by Tan (weareblahs)"
echo ''
echo "If you didn't install Speedtest yet (or you installed speedtest-cli instead of"
echo 'the official Ookla one), Please follow the steps on'
echo 'https://www.speedtest.net/apps/cli#Install_Options to install Speedtest, then'
echo 'run for the first time and accept EULA in order to let unspeedtest work'
echo 'properly.'
echo ''
read -p "Press any key to start installation of unspeedtest."
echo "Checking if required software is installed..."
sudo apt install python apache2
echo "Installing Python requirements..."
pip install -r requirements.txt
ln -s $(pwd)/apache /var/www/html/unspeedtest
echo $(pwd) >> dir
chmod +x *.sh
crontab cron
./clearresults.sh
echo "unspeedtest is accessible via http://[LOCAL_IP]/unspeedtest."