#!/usr/bin/env python3
"""
    Copyright (c) 2024 suwa, chocorho
"""

import datetime
import discord
from discord.ext import commands
import secret

"""
    A discord bot to be used by Moderators to manage messages in large numbers.
"""
class CleanSlateBot:
  def __init__(self):
    @bot.event
    async def on_ready():
      print(f'We have logged in as {bot.user}')
    
    @bot.event
    async def on_disconnect():
      print("Bot has disconnected.")
  
  def commands(self):
    @bot.command()
    async def ping(message):
      await message.channel.send('Pong!')
    
    @bot.command()
    async def redact(message, target):
      if (None == target):
        await message.channel.send('target not specified. Try again.')
      else:
        end_date = datetime.datetime(2021, 5, 1)
        async for historical_message in message.channel.history(limit=None, before=end_date):
          if (target == message.author.id):
            print(f"now deleting the next message, from {message.created_at}")
            message.delete()
            time.sleep(5)
  
  def run(self):
    self.commands()
    bot.run(secret.credentials.bottoken)


if __name__ == '__main__':
  CleanSlateBot.run()
