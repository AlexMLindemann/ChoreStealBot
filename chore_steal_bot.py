import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os 
import time
from datetime import datetime 
import schedule
import re

token = "xoxe.xoxp-1-Mi0yLTk2NDg2ODczMTIzNS0zMDE2MjA3MzMwMTQ0LTY3Njc1NDM1NTM2MjAtNjc4Nzg3MzEzNTUyMC1jYzExZjE4MGUzM2JjNGU2YjM3YmJmMmNjZWZlYTQxOGRmODgxNjdkMTk3NGYyYWU1NGNlYzJjOGZlYTM5Yjg2"

client = WebClient(token=token)

# channel_id = "CUBGKFCJW"
channel_id = "C06NKN4RM44"

chore_rankings = {
    "Collect and organize mail from around the first": 1,
    "Wipe off fingerprints on elevator buttons, walls and ceiling": 2,
    "Wipe down serving room counters": 3,
    "Pick up all trash around brick walkway": 4,
    "Clean and Wipe Study Room counters": 5,
    "Refill and report 2nd/3rd Bathroom and women's bathroom consumables (paper towels, toilet paper, etx)":6,
    "Take out and replace trash in 2nd and 3rd floor bathrooms, women's bathroom included": 7,
    "Clean Dishes and unclog Kitchen Sink": 8,
    "Sweep / Mop Elevator": 9,
    "Clean and organize 2nd floor balcony": 10
}
message_text = "collect and organize"

def process_chore_message(message_text):
    chores = message_text.split('\n')
    scored_chores = []

    for c in chores:
        score = float('inf')
        easiest_chore = ""
        #chore_description = " ".join(c.split()[4:])
        chore_description = c[4:]
        if chore_description in chore_rankings:
            rank = chore_rankings[chore_description]
            
            if rank < score:
                easiest_chore = chore_description
                score = rank


    return easiest_chore

def wait_for_message():
    try:
        now = datetime.now()
        curr_time = now.strftime("%H:%M")
        channel_id = "CUBGKFCJW"

        #if now.weekday() in [1, 3] and curr_time.startswith("21"):
        if curr_time.startswith("16"):
            response = client.conversations_history(channel=channel_id, limit=10)
            messages = response.data['messages']

            for m in messages:
                if m['user'] == "U04CN22H22C":
                    process_chore_message(m['text'])
                    break


    except SlackApiError as e:
        print(f"No Messages sent: {e}")






def job_that_executes_once():
    #wait_for_message()
    print("exeing at ", datetime.now())
    return schedule.CancelJob  # If you only want to execute this job once at the specified time

# Assuming you want to check every Tuesday and Thursday at 9 PM
schedule.every().tuesday.at("21:00").do(job_that_executes_once)
schedule.every().thursday.at("21:00").do(job_that_executes_once)


while True:
    schedule.run_pending()
    time.sleep(1)








#testing
message_text = None