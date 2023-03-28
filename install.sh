#!/bin/bash

apt update
apt install python3 python3-pip -y
apt install python3-opencv -y

pip3 install -r requirements.txt

mkdir /usr/bin/cctmk
cp config.py /usr/bin/cctmk/
cp cctmk.py /usr/bin/cctmk/
cp app.py /usr/bin/cctmk/
cp templates/* /usr/bin/cctmk/templates/

cp cctmk.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable cctmk.service
systemctl start cctmk.service