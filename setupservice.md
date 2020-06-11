##Python3 steup on pi
`sudo pip3 install slackclient RPi.GPIO`
##Env OS variables storred in Rasberrypi at end of
`sudo vim /etc/profile`
Add the following at the ned of the file and add your Token and ID you are monitoring

`export SLACK_API_TOKEN=`Token

`export SLACK_USER_ID=`ID

##The service definition must be on the /etc/systemd/system folder. Our service is going to be called "slackstatuslight.service":

`sudo chmod 644 /etc/systemd/system/slackstatuslight.service
chmod +x /home/pi/slackstatuslight.py
sudo systemctl daemon-reload
sudo systemctl enable slackstatuslight.service
sudo systemctl start slackstatuslight.service`

###General Commands
**Check status**
`sudo systemctl status hello.service`

**Start service**
`sudo systemctl start hello.service`

**Stop service**
`sudo systemctl stop hello.service`

**Check service's log**
`sudo journalctl -f -u hello.service`