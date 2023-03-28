# CCP-Social-Credit-discord
A simple bot that mocks the CCP's Social credit system.
DISCLAIMER: The terms in the "good" and "bad" field here are meant to mock the CCP and in no way reflect the views of the author

Installation (Ubuntu Server):
```
sudo apt install git python3 python3-pip
```
```
git clone https://github.com/0xGingi/CCP-Social-Credit-discord
```
```
cd CCP-Social-Credit-discord
pip3 -r requirements.txt
```
In the main.py file, replace my discord user id with yours where required
Now invite the discord bot to your server and give basic permissions needed to read/send messages
```
python3 main.py
```
## Systemd service to autostart bot
```
sudo nano /etc/systemd/system/china.service
```
```
[Unit]
Description=social credit score

[Service]
Type=simple
Restart=always
User=user
Group=user
WorkingDirectory=/home/user/CCP-Social-Credit-discord
ExecStart=/usr/bin/python3 /home/user/CCP-Social-Credit-discord/main.py

[Install]
WantedBy=multi-user.target
```
Replace user and group with your username and change the workingdirectory and execstart with your locations
```
sudo systemctl enable --now china
```
