![image](https://github.com/weareblahs/unspeedtest/assets/37889443/faae9bfa-a247-42fb-b0f4-945ccb89a400)
# Note
Although this script is written on Python, I suggest you to run it on a Raspberry Pi as the setup scripts are optimized for Raspberry Pi OS (Debian).
# Why did I do this?
I actually appreciate Fing's automated speedtest feature, but the software itself is only available on Windows and Mac computers. This is a Linux-based equivalent of the daily speedtest feature on Fing, powered by Speedtest.net from Ookla.
# Setup
1. Install `git` and clone this repository on your home directory (example: `/home/(USERNAME)`).
```bash
sudo apt-get install git
cd ~
git clone https://github.com/weareblahs/unspeedtest
```
2. Install Ookla's Speedtest CLI by running these commands:
```bash
sudo apt-get install curl
curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | sudo bash
sudo apt-get install speedtest
```
 - After running these commands, run `speedtest` and accept EULA. It is recommended to let the first speedtest end to see if it's working from your side.
## OPTIONAL: Before setup starts
To modify when will the automated speedtest starts, edit `cron` from the `unspeedtest` directory. 
 - By default, `0 0 0 0 0` means that unspeedtest will run automated speedtests on 12am everyday if the device is turned on. To generate cron expressions, use `https://crontab.guru/` or `https://crontab.cronhub.io/` and replace `0 0 0 0 0` with what you've got from the generators.
3. Make `setup.sh` executable and start the setup. Do note that the setup script won't work if you're not running with `sudo` permissions.
```bash
chmod +x setup.sh
sudo ./setup.sh
```
4. Visit `http://raspberrypi.local/unspeedtest` (or replace `raspberrypi.local` with the IP address you got from `hostname -I`) to see if it's working. If it's working, you'll see this page:![image](https://github.com/weareblahs/unspeedtest/assets/37889443/b4af3e59-0be9-4e46-8176-0e79bde65d39)
5. Go to terminal and start your first manual unspeedtest session.
```bash
cd ~/unspeedtest
./unspeedtest.sh
```

# License
See [here](https://github.com/weareblahs/unspeedtest/blob/main/LICENSE.md).
