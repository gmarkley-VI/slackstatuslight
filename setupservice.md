##Python3 steup on pi
`sudo pip3 install slackclient RPi.GPIO`

##The service definition must be on the /etc/systemd/system folder. Our service is going to be called "slackstatuslight.service":
Make sure to add your API token and UserID in the service file.

`sudo chmod 644 /etc/systemd/system/slackstatuslight.service`

`sudo systemctl daemon-reload`

`sudo systemctl enable slackstatuslight.service`

`sudo systemctl start slackstatuslight.service`


###General Commands
**Check status**
`sudo systemctl status slackstatuslight.service`

**Start service**
`sudo systemctl start slackstatuslight.service`

**Stop service**
`sudo systemctl stop slackstatuslight.service`

**Check service's log**
`sudo journalctl -f -u slackstatuslight.service`