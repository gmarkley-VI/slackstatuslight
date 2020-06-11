import RPi.GPIO as GPIO
import time
import sys

import os
from slack import WebClient
from slack.errors import SlackApiError

#LED hardware settings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

slack_token = os.environ["SLACK_API_TOKEN"]
user = os.environ["SLACK_USER_ID"]


client = WebClient(token=slack_token)

while True:
  try:
    response = client.users_info(user=user)
  except SlackApiError as e:
      if e.response["error"] == "ratelimited":
        # The `Retry-After` header will tell you how long to wait before retrying
        delay = int(e.response.headers['Retry-After'])
        print(f"Rate limited. Retrying in {delay} seconds")
        time.sleep(delay)
        response = client.users_info(user=user)
  except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

  userdata = response.data['user']
  userprofile = userdata['profile']
  status = userprofile['status_text']

  if status != "":
    GPIO.output(18, GPIO.HIGH)
  else:
    GPIO.output(18, GPIO.LOW)

  time.sleep(15)