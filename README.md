#Old Project Moving to Archive

# slackstatuslight
Have you ever wanted to let your family know when you're on a call? But want to keep the door open to let the summer air flow through. Well, you're in luck. This hack and hustle project did precisely that. Credit goes to my wife for asking me to tackle this one.
  Slack has an excellent integration with google calendar to auto-set your status based on your current meetings. I know you can go to Google directly. But I wanted the option to have an easy override for impromptu conversations that tend to start in slack. So I decided to use the slack API and status to notify my door light when I was busy or in a meeting.
First, I started by using a raspberry pi and a breadboard to drive 2 LED lights using a 220ohm resistors in parallel to protect the board. A few lines of code write a service and boom. You have slack status light with vintage housing. Some poor soldering on an old board and small mod to install it on my door. Now everyone but my dog knows when I am quietly listening away on a conf call.
  Thank you, Red Hat - OpenShift hack and hustle in action.

Here is the board pin outs to use for this.
<img src="pics/board.jpg">

Here is the board mounted to the wall and wired up
<img src="pics/mount.jpg">

Here is the light off
<img src="pics/off.jpg">

And last but not least here is the light on
<img src="pics/on.jpg">
