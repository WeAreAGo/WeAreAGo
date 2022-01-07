import os, time
import discord
from discord.ext import tasks
client = discord.Client()


dm_message = open('message.txt', encoding='utf-8').read()
token = 'OTIwOTc2NDg1MTczNTYzNDIy.YdfTiw.vYjmLbVrhiyFOVR5KB0uKYUsWaI'
wait = 240
relog_sent = False

users = []
users_send = []
messaging = False


@client.event
async def on_ready():
  print("Bot User:",client.user)
  print()

@client.event
async def on_message(message):
  global users
  global users_send
  global messaging
  if message.author != client.user:
    if not message.author.bot:
      if(message.author.id not in users):
        if(not messaging):
          print("Logged:",message.author)
          users.append(message.author.id)
          users_send.append(message.author.send)


@tasks.loop(seconds=30)
async def start_dms():
  global users_send
  messaging = True
  print("Messaging...")
  success = 0
  fails = 0
  for user_send in reversed(users_send):
    time.sleep(wait)
    try:
      await user_send(dm_message)
      success += 1
    except Exception as e:
      fails += 1
      print("Error:",e)
  print("---------------")
  print(success,"Success")
  print(fails,"Fails")
  print("---------------")
  users_send = []
  if(relog_sent): users = []
  messaging = False
  print("Logging...")

start_dms.start()
client.run(token, bot = False)
